import time

sleep_time = 1
options = [
    ["waffles","Waffles with strawberries and whipped cream."],
    ["pancakes", "Sweet potato pancakes with butter and syrup." ],
    ["donuts","Yummy gooey chocolate donuts."]]

def print_pause(msg):
    print(msg + "\n")
    time.sleep(sleep_time)

def ask_pause(msg):
    answer = input(msg + "\n").lower()
    time.sleep(sleep_time)
    return answer

def valid_input(prompt, options):
    while True:
        answer = ask_pause(prompt)
        for option in options:
            if option[0] in answer:
                return answer 
        print_pause("I'm sorry I don't understand.")

def intro():           
    print_pause("""Welcome to breakfast, I am your breakfast bot, Bob.\n""" +
            f"""Today we have {len(options)} breakfasts available.""")
def menu():
    for option in options:
        print_pause(option[1])       

def order_again():
    while True:
        answer = valid_input("Do you want to place another order: yes/no/menu", ["yes","no","menu"])
        if "no" in answer:
            print_pause("Ok, Thanks for ordering Good Bye!")
            break
        elif 'yes' in answer:
            print_pause("I'm happy to take another order!")
            break
        elif "menu" in answer:
            menu()
    return answer

def get_order(breakfast):
    while breakfast == "yes":
        items =[]
        for option in options:
            items.append(option[0])
        item_list = ", ".join(items)
        order = valid_input(f"Please place your order. Would you like {item_list}?", options)
        for option in options:
            if option[0] in order:
                print_pause(f"{option[0]} it is!")
        print_pause("Your order will be ready shortly.")
        breakfast = order_again()

def order_breakfast():
    intro()
    menu()
    get_order("yes")

if __name__ == "__main__":
    order_breakfast()