# importing time and random to enhance the game
import time
import random


# print and then pause useing time
def print_pause(msg):
    print(msg + "\n")
    time.sleep(1)


# gets input from user and then also pause
def talk(msg):
    answer = input(msg + "\n").lower()
    time.sleep(1)
    return answer


# introduction to the ganme taking Player as an argument for customizing
def intro(player):
    print_pause("Welcome to the game of games")
    print_pause("You never know what might happen next")
    print_pause(f"You only have {player['lives']}")
    print_pause("Use them wisely.")
    print_pause("To win, aquire 3 items, pets do not count.")
    print_pause("It was a dark and stormy night....")
    print_pause("You get to choose where to go....")


# randomize and return whatever list is providded
def randomness(items):
    return random.choice(items)


# gets input and checks it against provided answer returning answer
def chooser(msg, items):
    prompt = talk(msg)
    for item in items:
        if "".join(item) == prompt:
            return prompt
    chooser(msg, items)


# checks reward type adds random reward or removes a life
def reward(item, player):
    treasures = ["Gold", "Torch", "Sword"]
    pets = ["Lion", "Tiger", "Bear", "Wolf"]
    if item == "Game Over":
        player["lives"] -= 1
        print_pause("You have been rewared with death")
        print_pause(f"You now have {player['lives']} lives left")
    elif item == "Tresure":
        item_gained = randomness(treasures)
        player["items"].append(item_gained)
        list = player["items"]
        print_pause(f"{item_gained} added to your items")
        print_pause(f"Your items: {', '.join(list)}")
    elif item == "Creature":
        pet_gained = randomness(pets)
        player["pets"].append(pet_gained)
        list = player["pets"]
        print_pause(f"{pet_gained} added to your pets")
        print_pause(f"Your Pets: {', '.join(list)}")


# gets user to choose a cave path from the list and randomizes what happens
def cave(player):
    print_pause("As you enter the cave splits into three directions.")
    chooser("""Do you go\n1. Left\n""" +
            """2. Center\n3. Right""", ["1", "2", "3"])
    rooms = [
        ["You emerge into a huge cavern, filled with treasure.", "Tresure"],
        ["YOu cannot see anything as it's to1o dark....", "Game Over"],
        ["You emerge into a small cavern where you see a creature", "Creature"]
    ]
    action = randomness(rooms)
    print_pause(action[0])
    return reward(''.join(action[1]), player)


# gets user to choose a cave path from the list and randomizes what happens
def castle(player):
    print_pause("The Castle has 3 floors.")
    chooser("""Do you explore the \n1. 1st floor\n""" +
            """2. 2nd Floor\n3. 3rd Floor""", ["1", "2", "3"])
    rooms = [
        ["You emerge into a room filled with treasure.", "Tresure"],
        ["You enter a barred room and the door closes....", "Game Over"],
        [
            "You emerge into a small bedroom where you see a creature",
            "Creature"
        ]
    ]
    action = randomness(rooms)
    print_pause(action[0])
    reward(''.join(action[1]), player)


# allows player to choose seeting
def choose_venue(choice, player):
    if choice == "1":
        return cave(player)
    else:
        return castle(player)


# keeps the games going unless win or lose conditions are met
def playGame(player):
    setting = chooser("Do you explore 1. The Cave or 2. The Castle?",
                      ["1", "2"])
    choose_venue(setting, player)
    while player["lives"] > 0:
        if len(player["items"]) > 2:
            print_pause("You have gained at lesat 3 itmes and have won!")
            return False
        else:
            choose_venue(setting, player)
    print_pause("Unfortunately, you have died :-(")
    return False


# allows player to choose to keep playing
def keep_playing(response):
    if response == "yes":
        return True
    else:
        return False


# sets up the game and runs it
def game():
    player = {
        'lives': 2,
        'items': [],
        'pets': []
    }
    intro(player)

    game_on = True
    while game_on:
        playGame(player)
        play_again = chooser("Do you want to play again? yes/no",
                             ["yes", "no"])
        game_on = keep_playing(play_again)


if __name__ == "__main__":
    game()
