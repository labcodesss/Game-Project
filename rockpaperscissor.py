import random

def get_winner(player, computer):
    if player == computer:
        return "It's a Tie! 🤝"
    
    winning_cases = {
        "rock": "scissors",  # Rock beats Scissors
        "scissors": "paper",  # Scissors beats Paper
        "paper": "rock"  # Paper beats Rock
    }

    if winning_cases[player] == computer:
        return "You Win! 🎉"
    else:
        return "Computer Wins! 😢"

print("Welcome to Rock-Paper-Scissors Game! ✊✋✌️")
choices = ["rock", "paper", "scissors"]

# Get user choice
player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

# Validate input
if player_choice not in choices:
    print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
else:
    # Get computer's choice
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    # Determine the winner
    result = get_winner(player_choice, computer_choice)
    print(result)
