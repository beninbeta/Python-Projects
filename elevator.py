import time


def print_pause(msg):
    print(msg + "\n")
    time.sleep(sleep_time)


def get_pause(msg):
    choice = input(msg + "\n")
    time.sleep(sleep_time)
    return choice


def intro():
    print_pause("""You have just arrived at your new job!\n""" +
                """You are in the elevator.""")


def first_floor(new_employee):
    if ''.join(floors[1][2]) in new_employee:
        print_pause(
            """The clerk greets you, but she has already given you """ +
            """your ID card, so there is nothing more to do here now.""")
        operate()
    else:
        new_employee.append(''.join(floors[1][2]))
        print_pause(
            f"""The clerk has given you an {''.join(floors[1][2])}. """ +
            """You can go to the 2nd floor to get your handbook!""")
        operate()


def second_floor(new_employee):
    if (''.join(floors[2][2][0]) in new_employee
            and ''.join(floors[2][2][1]) in new_employee):
            print_pause(
                """You already have everything you need """ +
                """please head to the 3rd floor.""")
            operate()
    elif ''.join(floors[2][2][0]) in new_employee:
        new_employee.append(''.join(floors[2][2][1]))
        print_pause(
            f"""You have recieved your {''.join(floors[2][2][1])}.""" +
            """  You can now go to work!""")
        operate()
    else:
        print_pause(
            f""""You need to have your {''.join(floors[1][2])} """ +
            """in order to access this floor.""")
        operate()


def third_floor(new_employee):
    if (''.join(floors[2][2][0]) in new_employee
            and ''.join(floors[2][2][1]) in new_employee):
            print_pause("Please proceed to your desk!")
    else:
        separator = ", "
        print_pause(""" I'm sorry you don't have everything you need!""" +
                    f"""You need to have {separator.join(floors[2][2])}.""")
        operate()


def check_creds(floor, new_employee):
    if floor == "1":
        first_floor(new_employee)
    elif floor == "2":
        second_floor(new_employee)
    elif floor == "3":
        third_floor(new_employee)


def floor_check(floor_choice):
    for floor in floors:
        for floor_num in floor:
            if floor_choice in floor_num:
                print_pause(
                    """After a few Moments, you """ +
                    f"""find your self in the {floor[1]}""")
                return check_creds(floor_choice, new_employee)
    return print_pause("""That's not actually a floor we have """ +
                       """here, please try again.""")


def operate():
    print_pause("""Please enter the number for the """ +
                """floor you would like to visit:""")
    for floor in floors:
        print_pause(f"{floor[0]}. {floor[1]}")
    choice = get_pause("What Floor Please: ")
    floor_check(choice)


def leaving_elevator(msg, yes, no):
    while True:
        leaving = get_pause(msg).lower()
        if leaving in yes:
            return False
        elif leaving in no:
            return True


def run_elevator():
    intro()
    operate()


if __name__ == "__main__":
    floors = [
        [
            "1",
            "Lobby",
            [""]
        ],
        [
            "2",
            "Human Resources",
            ["ID Card"]
        ],
        [
            "3",
            "Engineering Department",
            ["ID Card", "Employee Handbook"]
        ]
    ]

    new_employee = []
    sleep_time = 1
    run_elevator()
