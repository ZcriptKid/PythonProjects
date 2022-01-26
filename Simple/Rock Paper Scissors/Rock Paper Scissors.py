import random

while True:
    # Check what user wants to do, either continue the program or exit.
    response = input("Welcome to this rock, paper and scissors match. \
    \nDo you want to continue? Enter 'y' to continue or another key to discontinue. ")
    if response == 'y':
        # List of choices for CPU and player.
        rps_list = ['rock', 'paper', 'scissors']
        # Random item returns from RPS list as the CPU's throw stored as a variable.
        CPUThrow = random.choice(rps_list)
        # Player chooses what to throw stored as a variable.
        playerThrow = input("Rock, paper or scissors: ")
        # Check if player input is correct.
        if playerThrow == 'rock' or 'paper' or 'scissors':
            # Throws are shown and printed for user to see.
            print("\nYou threw " + playerThrow + ".\n" + "Your opponent threw " + CPUThrow + ".")
            # If player won.
            if playerThrow == 'rock' and CPUThrow == 'scissors' \
                    or playerThrow == 'paper' and CPUThrow == 'rock' \
                    or playerThrow == 'scissors' and CPUThrow == 'paper':
                print(" -You won! Meet me again.\n")
                continue
            # If player got a draw.
            elif playerThrow == 'rock' and CPUThrow == 'rock' \
                    or playerThrow == 'paper' and CPUThrow == 'paper' \
                    or playerThrow == 'scissors' and CPUThrow == 'scissors':
                print(" -It's a draw! Meet me again.\n")
                continue
            # If player lost.
            else:
                print(" -You lost! Meet me again.\n")
                continue
        # Player did not input with correct grammar.
        else:
            print("Invalid input. Try again.\n")
            continue
    # Player did not want to continue.
    else:
        print(" -See you!")
        break
