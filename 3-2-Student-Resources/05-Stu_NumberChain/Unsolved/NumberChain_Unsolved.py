# Initial variable to track game play
user_play = "y"
Number_List = []
start = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    print("Please only give WHOLE NUMBERS")
    UserInput = input("How many numbers would you like to count: ")
    InputFixed = int(UserInput)
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(0,InputFixed):
        Number_List.append(i)

        # Print each number in the range
        print(i)
    print(Number_List)    
    
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")