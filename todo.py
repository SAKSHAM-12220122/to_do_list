#simple todo list
Enter_input = 'random'
data = list()
# creating  a list with following list data
# 1.Add an item
# 2.Mark as done
# 3.Remove item
# 4.Exit


def Menu():
    print("Menu:")
    print("Add item, Enter 1:")
    print("Mark item Done, Enter 2:")
    print("Remove item,Enter 3:")
    print("Exit menu, Enter 4:")


while Enter_input != '4':

    Menu()
    Enter_input = input("Select Your choice:")

    if Enter_input == '1':
        task = input("Please add task :")
        data.append(task)
        print("Added task is :",task)
    elif Enter_input == '2':
        task = input("What is to be marked as Done")
        # if task is present in data list then remove it from list
        # else print the statement that item does not exist in the list
        if task in data:
            data.remove
            print("Removed task is :",task)
        else:
            print("Task does not exist in the to do list")
    elif Enter_input == '3':
        print("List of To-Do Tasks:")
        for items in data:
            print(task)
    elif Enter_input == '4':
        print("Your menu has been Exited")