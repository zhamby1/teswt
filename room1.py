from check_in import check_input
from room1a import room1a_dialog
words = ["room1a","dead"]


def room1_dialog():
    print("room1a")
    choice = check_input(words)
    if choice == "room1a":
        room1a_dialog()
    else:
        print("you are done")
