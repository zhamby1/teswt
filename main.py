from check_in import check_input
from room2 import room2_dialog
from room1 import room1_dialog
words = ["room1","room2"]
choice = check_input(words)

if (choice == "room1"):
    room1_dialog()
else:
    room2_dialog()

