#Rock Paper Scissors Game

import random
def determine_winner(user_choice,comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

user_score = 0
computer_score = 0

# Main game loop
while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue
    
    comp_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, comp_choice)

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    print(result)
    print(f"Scores -> You: {user_score} | Computer: {computer_score}\n")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
