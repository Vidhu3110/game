# Game.py

import random

challenges = [
    {"description": "Solve a riddle", "attribute": "Intelligence"},
    {"description": "Defeat an enemy in combat", "attribute": "Strength"},
    {"description": "Navigate a treacherous maze", "attribute": "Dexterity"}
]

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def perform_challenge(player, challenge):
    print(f"You face a challenge: {challenge['description']}")
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll}.")

    if dice_roll <= 4:
        print("Challenge lost.")
    elif dice_roll <= 8:
        print("Challenge won.")
    else:
        print("Critical win!")
        player[challenge['attribute']] += 1

def start_game(player):
    for i, challenge in enumerate(challenges):
        print(f"Challenge {i + 1}: {challenge['description']}")
        input("Press Enter to continue...")
        perform_challenge(player, challenge)

    print("\nGame over! Your character's attributes:")
    for attr, value in player.items():
        print(f"{attr}: {value}")
