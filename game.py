import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health})"

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Damage: {self.damage})"


class DungeonGame:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.enemies = [Enemy("Goblin", 30, 10), Enemy("Skeleton", 40, 15)]
        self.rooms_explored = 0

    def explore_room(self):
        print("You enter a dark room...")
        encounter_chance = random.random()
        if encounter_chance < 0.5:
            self.enemy_encounter()
        else:
            reward_chance = random.random()
            if reward_chance < 0.3:  # 30% chance of finding a reward
                self.find_cookies()
            else:
                print("You explore the room and find nothing of interest.")

    def find_cookies(self):
        print("You stumble upon a stash of cookies!")
        health_gain = random.randint(10, 30)
        self.player.health = min(100, self.player.health + health_gain)
        print(f"You eat the cookies and gain {health_gain} health!")

    def enemy_encounter(self):
        enemy = random.choice(self.enemies)
        print(f"You encounter a {enemy}!")
        while enemy.is_alive() and self.player.is_alive():
            print(f"{self.player} - vs - {enemy}")
            action = input("What will you do? [attack/flee] ").lower()
            if action == "attack":
                player_damage = random.randint(5, 20)
                enemy.take_damage(player_damage)
                print(f"You attack the {enemy.name} dealing {player_damage} damage!")
                if enemy.is_alive():
                    enemy_damage = random.randint(5, 15)
                    self.player.take_damage(enemy_damage)
                    print(f"The {enemy.name} attacks you, dealing {enemy_damage} damage!")
            elif action == "flee":
                flee_chance = random.random()
                if flee_chance < 0.5:
                    print("You successfully flee from the enemy!")
                    return
                else:
                    print("You failed to flee!")
                    enemy_damage = random.randint(5, 15)
                    self.player.take_damage(enemy_damage)
                    print(f"The {enemy.name} attacks you as you attempt to flee, dealing {enemy_damage} damage!")
            else:
                print("Invalid action. Choose 'attack' or 'flee'.")
        if self.player.is_alive():
            print(f"You defeated the {enemy.name}!")
            self.rooms_explored += 1
            print("You continue exploring...")
        else:
            print("Game Over! You were defeated.")

    def play(self):
        print("Welcome to the Dungeon!")
        while self.player.is_alive() and self.rooms_explored < 5:
            print("\n-----------------------------------")
            print(f"Rooms Explored: {self.rooms_explored}/5")
            print("-----------------------------------\n")
            self.explore_room()
        if self.rooms_explored == 5:
            print("Congratulations! You have successfully explored the dungeon.")

# Main
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = DungeonGame(player_name)
    game.play()

