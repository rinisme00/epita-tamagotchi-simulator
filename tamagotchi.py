class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.health = 100
        self.boredom = 0
        self.exhaustion = 0

    @property
    def alive(self):
        return self.health > 0

    def feed(self):
        if self.alive:
            self.hunger = max(0, min(100, self.hunger - 25))
        else:
            print(f"{self.name} is no longer alive and cannot be fed.")
    
    def play(self):
        if self.alive:
            self.boredom = max(0, min(100, self.boredom - 15))
            self.hunger = max(0, min(100, self.hunger + 15))
            self.exhaustion = max(0, min(100, self.exhaustion + 10))
        else:
            print(f"{self.name} is no longer alive and cannot play.")

    def sleep(self):
        if self.alive:
            self.exhaustion = max(0, min(100, self.exhaustion - 20))
        else:
            print(f"{self.name} is no longer alive and cannot sleep.")

    def heal(self):
        if self.alive:
            self.health = max(0, min(100, self.health + 25))
        else:
            print(f"{self.name} is no longer alive and cannot be healed.")

    def update_needs(self):
        if not self.alive:
            return
        self.hunger = max(0, min(100, self.hunger + 5))
        self.exhaustion = max(0, min(100, self.exhaustion + 3))
        self.boredom = max(0, min(100, self.boredom + 5))

        if self.hunger >= 80:
            self.health = max(0, min(100, self.health - 5))
        if self.exhaustion >= 80:
            self.health = max(0, min(100, self.health - 5))
        if self.boredom >= 80:
            self.health = max(0, min(100, self.health - 3))

    def display_status(self):
        print(f"\n----- {self.name}'s Status -----")
        
        print(f"Health: {self.health}/100")
        print(f"Hunger: {self.hunger}/100")
        print(f"Boredom: {self.boredom}/100")
        print(f"Exhaustion: {self.exhaustion}/100")
        if self.alive:
            print(f"Status: Alive")
        else:
            print(f"Status: Dead")
        print("----------------------------\n")