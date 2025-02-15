import random

def game(computer, player):
    if computer == player:
        return None  # Game is a tie
    elif (computer == 's' and player == 'w') or \
         (computer == 'w' and player == 'g') or \
         (computer == 'g' and player == 's'):
        return False  # Computer wins
    else:
        return True   # Player wins

print("Computer's turn: Snake (s), Water (w), or Gun (g)?")

randNo = random.randint(1, 3)

if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
else:
    computer = 'g'

player = input("Player's Turn: Choose Snake (s), Water (w), or Gun (g): ").lower()

# Validate input
if player not in ['s', 'w', 'g']:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    a = game(computer, player)

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")

    if a is None:
        print("The game is a tie! 🤝")
    elif a:
        print("Player wins! 🎉")
    else:
        print("Computer wins! 😢")
