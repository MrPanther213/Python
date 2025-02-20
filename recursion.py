# Example of recursion

def my_recursion():
    choice = input("Would you like to play a game, y or n: ")
    choice = choice.lower()
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("Have a lovely day")
    else:
        print("Unkown, please type y for yes and n for no. not Y or N.")
        my_recursion()

my_recursion()