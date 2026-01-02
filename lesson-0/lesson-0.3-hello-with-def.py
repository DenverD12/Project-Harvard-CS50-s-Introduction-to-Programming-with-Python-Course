
# define a function for hello with name parameter
# put in a default value of world in case an argument is not passed
def hello(to="world"):
    print("hello", to)

# separate function for main code - generally put at very top
def main():
    # ask user for name
    name = input("What is your name? ")

    # capitalize user's FULL name AND remove whitespace
    name = name.strip().title()


    # say hello to user by calling created function
    # function takes in the name variable 
    # and assumes it is now the "to" variable and passes it through that function
    hello(name)

    # hello without argument:
    hello()

main()