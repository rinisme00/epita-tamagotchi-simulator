# Tamagotchi Simulator

## Description

Tamagotchi Simulator is a command-line virtual pet simulation game developed in Python.

The player manages three Tamagotchis: Tama, Mochi, and Pocky. Each pet has its own needs and health status, which change as the player interacts with it.

This project demonstrates fundamental Python programming concepts, including Object-Oriented Programming (OOP), control flow, file handling, and JSON data persistence.

## Features

- Manage three Tamagotchis with individual attributes.
- Perform actions: Feed, Play, Sleep, and Heal.
- Monitor Health, Hunger, Boredom, and Exhaustion.
- Automatically update pet needs after each action.
- Experience random events that can affect pet health.
- Track living and deceased pets.
- Display game statistics.
- Save and load game progress using JSON files.
- Manage multiple save files with overwrite confirmation.
- Handle invalid user inputs and save files.

## Project Structure

- `main.py` — Command-line interface and user interaction.
- `tamagotchi.py` — Tamagotchi class, attributes, and actions.
- `game.py` — Game management, random events, and statistics.
- `storage.py` — JSON save and load functionality.
- `saves/` — Directory containing saved game files (created automatically).

## Requirements

- Python3
- No external dependencies required.

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the following command:

   `python3 main.py`

## How to Play

The Main Menu provides the following options:

1. **Select Pet** — Choose a Tamagotchi to interact with.
2. **Display All Pets** — View the status of all three pets.
3. **Display Statistics** — View overall game statistics.
4. **Save Game** — Save the current game state to a JSON file.
5. **Load Game** — Select an existing save file to restore the game.
6. **Exit (Q)** — Quit the game.

After selecting a pet, the player can choose from the following actions:

- **Feed:** Reduce hunger.
- **Play:** Reduce boredom while increasing hunger and exhaustion.
- **Sleep:** Reduce exhaustion.
- **Heal:** Restore health.
- **Display Status:** View the selected pet's current attributes.

Each successful action advances the game state. Pets can lose health when their needs become too high. A pet whose health reaches zero dies and can no longer perform actions.

## Save and Load

Game progress is stored in JSON format inside the `saves/` directory.

Players can create multiple save files, overwrite existing files after confirmation, and restore previously saved game states.

Invalid or corrupted save files are handled without replacing the current game state.