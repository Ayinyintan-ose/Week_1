import random
print("Let's have some fun. Choose between rock, paper and scissors. Remember you could also type 'quit' "
      "to end the game")

while True:
    # User option to pick from
    user_choice = ["rock", "paper", "scissors"]
    for index, choice in enumerate(user_choice):
        print(f"{index + 1}. {choice}")
    choices = input("Make a choice: ").lower()
    if choices == "quit":
        print("bye!")
        break
    computer_choice = random.choice(user_choice)
    print(f"Player two picked {computer_choice}")

    if choices == computer_choice:
        print("Draw, pick again")
    elif choices == "rock" and computer_choice == "scissors":
        print("You win!")
    elif choices == "scissors" and computer_choice == "rock":
        print("Opps, you lose!")
    elif choices == "paper" and computer_choice == "rock":
        print("That's a good one")
    elif choices == "rock" and computer_choice == "paper":
        print("You lose!")
    elif choices == "paper" and computer_choice == "scissors":
        print("You lose!")
    elif choices == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Try again and enter a valid option.")
