import numpy as np

arr = ["rock", "paper", "scissors"]
computer = arr[np.random.randint(0, 2)]
user = False
while user == False:
    user = input("rock, paper, scissors ,exit:\n")
    if user == computer:
        print("Tie!")
    elif user == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", user)
        else:
            print("You win!", user, "smashes", computer)
    elif user == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", user)
        else:
            print("You win!", user, "covers", computer)
    elif user == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", user)
        else:
            print("You win!", user, "cut", computer)
    elif user == "exit":
        break
    else:

        print("That's not a valid play. Check your spelling!")
    user = False
    computer = arr[randint(0, 2)]