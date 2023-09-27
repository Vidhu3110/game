import Game
import Role1  # Import the module for the first role (Wizard)
import Role2  # Import the module for the second role (Barbarian)

def main():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mystical realm filled with mystery and danger.")
    print("Two paths lie before you, each leading to a unique destiny.")
    print("Choose your role:")
    print("1. Wizard")
    print("2. Barbarian")

    role_choice = input("Enter your choice (1/2): ")

    if role_choice == '1':
        player = Role1.initialize_wizard()  # Create an instance of the Wizard class
        role_name = "Wizard"
    elif role_choice == '2':
        player = Role2.initialize_barbarian()  # Create an instance of the Barbarian class
        role_name = "Barbarian"
    else:
        print("Invalid choice. Exiting the game.")
        return

    print(f"You are now playing as {role_name}.")
    print("Prepare for an epic adventure!\n")

    # Start the game
    Game.start_game(player)

if __name__ == "__main__":
    main()
