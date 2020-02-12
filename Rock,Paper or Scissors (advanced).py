import random


computer_dice_roll = random.randint(1,3)
opponent_input = computer_dice_roll # computer input

def rock_paper_scissors():
    print("Choose 'Rock', 'Paper' or 'Scissors': ")
    user_input = input().lower() # user input
    if user_input == "rock"  and opponent_input == 1:
        print("Paper covers Rock, So Paper Wins! ")
        print("")
    elif user_input == "rock" and opponent_input == 2:
        print("Rock clashes with Rock, Choose Again! ")
        print("")
    elif user_input == "rock" and opponent_input == 3:
        print("Rock blunts Scissors, You Win! ")
        print("")
    elif user_input == "paper" and opponent_input == 1:
        print("Paper clashes with Paper, Choose Again! ")
        print("")
    elif user_input == "paper" and opponent_input == 2:
        print("Paper cover Rock, You Win! ")
        print("")
    elif user_input == "paper" and opponent_input == 3:
        print("Scissors cuts Paper, So Scissors Wins! ")
        print("")
    elif user_input == "scissors" and opponent_input == 1:
        print("Scissors cut Paper, You Win! ")
        print("")
    elif user_input == "scissors" and opponent_input == 2:
        print("Scissors are blunted by Rock, So Rock Wins! ")
        print("")
    elif user_input == "scissors" and opponent_input == 3:
        print("Scissors clashes with Scissors, Choose Again! ")
        print("")
    else:
        print("You did\'t pick!, Try Again")
        print("")


rock_paper_scissors()