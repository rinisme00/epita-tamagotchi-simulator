from game import Game
from storage import save_game, load_game
from pathlib import Path

SAVE_DIR = Path("saves")

def display_menu():
    print(f"\n===== TAMAGOTCHI SIMULATOR =====")
    print("\n1. Select Pet")
    print("2. Display All Pets")
    print("3. Display Statistics")
    print("4. Save Game")
    print("5. Load Game")
    print("Q. Exit")

def pet_selection(game):
    while True:
        print("\n===== SELECT A TAMAGOTCHI =====")
        for index, pet in enumerate(game.pets, start=1):
            if pet.alive:
                status = "Alive"
            else:
                status = "Dead"
            print(f"{index}. {pet.name} [{status}]")

        print("0. Back to Main Menu")

        choice = input("\nSelect a pet: ").strip()

        if choice == "0":
            return None

        try:
            choice_number = int(choice)
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
            continue

        if not (1 <= choice_number <= len(game.pets)):
            print("Invalid pet selection. Please choose 1, 2, or 3.")
            continue

        pet = game.select_pet(choice_number - 1)
        return pet

def pet_action(game, pet):
    while True:
        print("\n===== ACTION MENU =====")
        print("\n1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Heal")
        print("5. Display Status")
        print("0. Back to Main Menu")

        choice = input("\nSelect an action: ").strip()
        action_performed = False
        if choice == "0":
            return
        elif choice == "1":
            if not pet.alive:
                print(f"{pet.name} is dead and cannot be fed.")
                continue

            pet.feed()
            action_performed = True

            print(f"You fed {pet.name}!")
        elif choice == "2":
            if not pet.alive:
                print(f"{pet.name} is dead and cannot be played with.")
                continue

            pet.play()
            action_performed = True

            print(f"You played with {pet.name}!")
        elif choice == "3":
            if not pet.alive:
                print(f"{pet.name} is dead and cannot sleep.")
                continue

            pet.sleep()
            action_performed = True

            print(f"{pet.name} slept!")
        elif choice == "4":
            if not pet.alive:
                print(f"{pet.name} is dead and cannot be healed.")
                continue

            pet.heal()
            action_performed = True

            print(f"You healed {pet.name}!")
        elif choice == "5":
            pet.display_status()
        else:
            print("Invalid action. Please enter a number from 0 to 5.")

        if action_performed:
            game.update_status()
            game.random_event()

            if not pet.alive:
                print(f"{pet.name} has died!")


def main():
    game = Game()
    SAVE_DIR.mkdir(exist_ok=True)

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting the game...")
            break
        elif choice == "1":
            selected_pet = pet_selection(game)

            if selected_pet is not None:
                print(f"\nYou selected {selected_pet.name}")
                selected_pet.display_status()

                pet_action(game, selected_pet)

        elif choice == "2":
            for pet in game.pets:
                pet.display_status()

        elif choice == "3":
            game.display_statistics()

        elif choice == "4":
            filename = input("Enter save filename: ").strip()

            if not filename:
                print("Error: Filename cannot be empty.")
                continue
            if Path(filename).name != filename or "\\" in filename:
                print("Error: Please enter a filename, not a path.")
                continue
            if not filename.endswith(".json"):
                filename += ".json"

            save_path = SAVE_DIR / filename

            if save_path.exists():
                confirm = input("Save file already exists. Overwrite? (Y/N): ").strip().upper()

                if confirm != "Y":
                    print("Save cancelled.")
                    continue
            save_game(game, save_path)

        elif choice == "5":
            save_files = sorted(SAVE_DIR.glob("*.json"))

            if not save_files:
                print("No save files found!")
                continue
            print("\n===== AVAILABLE SAVE FILES =====")

            for index, file in enumerate(save_files, start=1):
                print(f"{index}. {file.name}")
            print("0. Back to Main Menu")

            selected = input("\nSelect a save file: ").strip()
            
            if selected == "0":
                continue
            try:
                selected_number = int(selected)
            except ValueError:
                print("Invalid input. Please enter a valid number!")
                continue

            if not (1 <= selected_number <= len(save_files)):
                print("Invalid save file selection.")
                continue

            selected_file = save_files[selected_number - 1]

            loaded_pets = load_game(selected_file)

            if loaded_pets is not None:
                game.pets = loaded_pets
                print(f"Game loaded successfully from '{selected_file.name}'!")
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()