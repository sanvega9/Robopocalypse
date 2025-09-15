
def Running(Robots_name):
    # You have to create and write to a file.
    # "a" that appends to a file if the file.
    # Robots_name is the user name that will appear toward the user
    san_file = open("Robopocaly.txt", "w")
    print("\n\n~~~~~~~~~~WELCOME " + Robots_name + " to Robopocalypse")
    san_file.write("\n\n~~~~~~~~~~WELCOME " + Robots_name + "to Robopocalypse")
    print("\nTechnology changes, but people stay the same is \"fear\"")
    san_file.write("\nTechnology changes, but people stay the same is \"fear\"")
    print("\nYou are a Robot know that time has changes a lot that individual mindset toward AI")
    san_file.write("\nYou are a Robot know that time has changes a lot that individual mindset toward AI")
    # This closes the file
    san_file.close()


def display_user_decisions(Robots_name):
    # This display the user the decision and what they choice will show in their history
    # "w" it destroys the file and over write that a new.
    # Robots_name is the user name that will appear toward the user
    san_file = open("Robopocaly.txt", "w")
    print("\nWhat are going to do " + Robots_name + " that you have been woke again?")
    san_file.write("\nWhat are going to do " + Robots_name + " that you have been woke again?")
    print("\nYou need to chose which mood you wanna to be with around the human your chose is be in peace#1 or angry#2")
    san_file.write("\nYou need to chose which mood you wanna to be with around the human your chose is be in peace#1"
                   "or angry#2")
    mood = input(">")
    san_file.write(">")
    # input the users decision
    if mood == "1":
        print("\nYou decide to be in peace with the human it went smooth they aren't required to built technology")
        san_file.write("\nYou decide to be in peace with the human it went smooth they aren't required to built"
                       "technology.")
        # Yes or no answer
        print("\nHowever,they tell you to follow the rules. Are going to follow the rule y or n")
        san_file.write("\nHowever,they tell you to follow the rules. Are going to follow the rule y or n")
        answer = input("enter y/n:")
        san_file.write("enter y/n:")
        if answer == "y":
            print("\nYou decide yes that you follow the rules and don't leave from the house")
            san_file.write("\nYou decide yes that you follow the rules and don't leave from the house")
        elif answer == "n":
            print("\nYou decide no that you wouldn't follow the rules and then your master got injury you feel bad that"
                  "they hurt him.")
            san_file.write("\nYou decide no that you wouldn't follow the rules and then your master got injury you feel"
                           "bad that they hurt him.")
    if mood == "2":
        print("\nYou decide to be in angry mood to the human it went awfully and you got disconnect.")
        san_file.write("\nYou decide to be in angry mood to the human it went awfully and you got disconnect.")
    san_file.close()


def read_view_history():
    # Read and view the preview history
    # r is to read or view it
    # the history view the
    print("\n\nView history:")
    san_file = open("Robopocaly.txt", "r")
    print(san_file.read())
    san_file.close()


def get_user_name():
    # open the file and be able to view the name of the username
    # This my user name input and to return the user_name
    san_file = open("Robopocaly.txt", "a")
    # To input the user the name
    user_name = input("what is your name:")
    san_file.write("what is your name:")
    san_file.write(user_name)
    san_file.close()
    return user_name


# Function that goes with the file
Robots_name = get_user_name()
Running(Robots_name)
display_user_decisions(Robots_name)
read_view_history()
