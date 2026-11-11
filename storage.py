import json
from tamagotchi import Tamagotchi

def save_game(game, filename):
    pets_data = []

    for pet in game.pets:
        pet_data = {
            "name": pet.name,
            "health": pet.health,
            "hunger": pet.hunger,
            "boredom": pet.boredom,
            "exhaustion": pet.exhaustion,
            "alive": pet.alive
        }

        pets_data.append(pet_data)

    game_data = {"pets": pets_data}

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(game_data, file, indent=4)
        print(f"Game is saved successfully as {filename}")
    except OSError as e:
        print(f"Error: Cannot save file '{filename}': {e}")
        return None

def load_game(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            game_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contains invalid JSON!")
        return None
    except OSError as e:
        print(f"Error: Cannot read file '{filename}': {e}")
        return None
    if not isinstance(game_data, dict):
        print("Error: Invalid game data.")
        return None
    
    pets_data = game_data.get("pets")
    
    if not isinstance(pets_data, list):
        print("Error: Invalid pets data.")
        return None

    if len(pets_data) != 3:
        print("Error: The game must contain exactly 3 pets!")
        return None

    required_keys = ["name", "health", "hunger", "boredom", "exhaustion", "alive"]
    numeric_attributes = ["health", "hunger", "boredom", "exhaustion"]
    loaded_pets = []

    for data in pets_data:
        if not isinstance(data, dict):
            print("Error: Invalid pet data.")
            return None
        
        for key in required_keys:
            if key not in data:
                print(f"Error: Missing required key '{key}'.")
                return None

        for attr in numeric_attributes:
            value = data[attr]

            if type(value) is not int:
                print(f"Error: '{attr}' must be an integer.")
                return None

            if not (0 <= value <= 100):
                print(f"Error: '{attr}' must be between 0 and 100.")
                return None
        name = data["name"]

        if not isinstance(name, str):
            print("Error: Pet name must be a string.")
            return None

        if not name.strip():
            print("Error: Pet name cannot be empty.")
            return None

        alive = data["alive"]

        if type(alive) is not bool:
            print("Error: 'alive' must be a boolean.")
            return None

        if alive != (data["health"] > 0):
            print("Error: 'alive' is inconsistent with 'health'.")
            return None
        
        pet = Tamagotchi(data["name"])
        pet.health = data["health"]
        pet.hunger = data["hunger"]
        pet.boredom = data["boredom"]
        pet.exhaustion = data["exhaustion"]

        loaded_pets.append(pet)

    return loaded_pets