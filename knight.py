# knight.py

class Knight:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = 100
        self.coins = 0

    def attack(self):
        return f"{self.name} attacks with {self.weapon}!"

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        else:
            return f"{self.name} takes {damage} damage!"

    def equip_armor(self, armor):
        self.armor = armor
        return f"{self.name} has {self.armor}!"

    def get_health(self):
        bar_size = 20  # size of the life bar
        current_health = int((self.health / 100) * bar_size)
        life_bar = "[" + "#" * current_health + "-" * (bar_size - current_health) + "]"
        return f"{self.name}'s health: {life_bar}"

    def print_attributes(self):
        print("""
            KNIGHT
            
               /\\
              /--\\
             /    \\
             
             
        """)
        print(f"Name: {self.name}")
        print(f"Weapon: {self.weapon}")
        print(f"Armor: {self.armor}")
        print(f"Health: {self.health}")
        print(f"Coins: {self.coins}")  # add coins attribute
        with open("knight.txt", "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Weapon: {self.weapon}\n")
            f.write(f"Armor: {self.armor}\n")
            f.write(f"Health: {self.health}\n")
            f.write(f"Coins: {self.coins}\n")  # write coins attribute to file

    def store_coins(self, coins):
        self.coins += coins
        return f"{self.name} has stored {coins} coins!"

    def open_data_knight(self):
        with open("knight.txt", "r") as file:
            data = file.read().splitlines()
            if len(data) >= 5:
                self.name = data[0].split(": ")[1]
                self.weapon = data[1].split(": ")[1]
                self.armor = data[2].split(": ")[1]
                self.health = int(data[3].split(": ")[1])
                self.coins = int(data[4].split(": ")[1])
            else:
                print("Error: Invalid data format in knight.txt")



# Usage
knight = Knight("Knight", "Sword", "Platemail")
#knight.print_attributes()
#knight.store_coins(50)


'''
print(knight.attack())
print(knight.defend(20))
print(knight.get_health())
print(knight.defend(20))
print(knight.get_health())
'''