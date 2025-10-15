import random

options = ["stone", "scissor", "paper"]

user_choice = input("Enter your choice (stone, scissor, paper): ").lower()

if user_choice not in options:
    print("Invalid input! Try again.")
else:
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie ")
    elif (
        (user_choice == "stone" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "stone")
    ):
        print("You win!")
    else:
        print("Computer wins")