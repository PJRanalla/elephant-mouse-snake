import random

# This is another version of Rock, Paper, Scissors by a different name...namely Elephant, Mouse, Snake.

while True:
    user_choice = input(f"Please Enter Your Choice:  Elephant | Mouse | Snake: ")
    choices = ["elephant", "mouse", "snake"]
    computer_choice = random.choice(choices)
    print(f"\nYou choose {user_choice.title()} and the computer chooses {computer_choice.title()}\n")


    if user_choice.lower() == computer_choice.lower():
        print(f"Both players have chosen {user_choice.title()}. This round is a draw. Try again to see who wins!")
    elif user_choice.lower() == "elephant":
        if computer_choice.lower() == "snake":
            print("Elephant Stomps on Snake! You Win!")
        else:
            print("Paper Beats Rock! You Lose :(")
    elif user_choice.lower() == "mouse":
        if computer_choice.lower() == "elephant":
            print("Mouse Scares Elephant! You Win!")
        else:
            print("Snake Eats Mouse! You Lose :(")
    elif user_choice.lower() == "Snake":
        if computer_choice.lower() == "Mouse":
            print("Snake Eats Mouse! You Win!")
        else:
            print("Elephant Stomps on Snake! You Lose :(")

    play_again = input("\nWould you like to play again? (Y/N): ")
    if play_again.lower() != "y":
        break
