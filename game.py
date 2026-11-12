import random
from tamagotchi import Tamagotchi

class Game:
    def __init__(self):
        self.pets = [Tamagotchi("Tama"), Tamagotchi("Mochi"), Tamagotchi("Pocky")]

    def select_pet(self, index):
        if 0 <= index < len(self.pets):
            return self.pets[index]
        else:
            print("Invalid pet selection.")
            return None

    def update_status(self):
        for pet in self.pets:
            if pet.alive:
                pet.update_needs()                

    def random_event(self):
        for pet in self.pets:
            if pet.alive:
                if random.random() < 0.1:
                    pet.health = max(0, min(100, pet.health - 10))
                    print(f"{pet.name} is sick!")

    def display_statistics(self):
        print(f"\n----- Game Statistics -----")
        count_alive = 0
        count_dead = 0
        total_health, total_hunger, total_boredom, total_exhaustion = 0, 0, 0, 0
        for pet in self.pets:
            if pet.alive:
                count_alive += 1
                total_health += pet.health
                total_hunger += pet.hunger
                total_boredom += pet.boredom
                total_exhaustion += pet.exhaustion
            else:
                count_dead += 1
        print(f"Living pets: {count_alive}")
        print(f"Dead pets: {count_dead}")

        if count_alive > 0:
            print(f"Average health of living pets: {total_health / count_alive:.2f}")
            print(f"Average hunger of living pets: {total_hunger / count_alive:.2f}")
            print(f"Average boredom of living pets: {total_boredom / count_alive:.2f}")
            print(f"Average exhaustion of living pets: {total_exhaustion / count_alive:.2f}")
        else:
            print("No living pets.")