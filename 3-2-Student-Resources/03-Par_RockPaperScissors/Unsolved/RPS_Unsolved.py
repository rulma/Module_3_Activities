# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

#Possible Outcomes (win,lose,tie)
Win = "You win!"
Lose = "You lost.."
Tie = "It's a draw"

# Record Keeper tallies user wins losses and drawss
user_w = 0
user_l = 0
user_d = 0

# Specify the three options
options = ["r", "p", "s"]

#r beats s 
# Computer Selection
computer_choice = random.choice(options)

# Run Conditionals

#Determine if the user still wants to play with a continue varirable
keep_playing = "y"
while keep_playing == "y":

    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    #Make Sure user input is valid
    if user_choice not in options:
        print("Please give a valid input, r, p, s")
        user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    
    #input is valid check who won
    else: 
        # Check for a Tie
        if user_choice == computer_choice:
            print(computer_choice + " vs " + user_choice)
            user_d += 1
            print(Tie)
            print(f"W: {user_w} D: {user_d} L: {user_l}")
            keep_playing = input("Continue y/n?...")

        #User won
        elif (user_choice == "r" and computer_choice == "s") or (user_choice == "s" and computer_choice == "p") or (user_choice == "p" and computer_choice == "r"):
            print(computer_choice + " vs " + user_choice)
            user_w += 1
            print(Win)
            print(f"W: {user_w} D: {user_d} L: {user_l}")
            keep_playing = input("Continue y/n?...")
        
        #User Lost
        else:
            print(computer_choice + " vs " + user_choice)
            user_l += 1
            print(Lose)
            print(f"W: {user_w} D: {user_d} L: {user_l}")
            keep_playing = input("Continue y/n?...")
