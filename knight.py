# knight.py

import random
import os
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Knight:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = 100
        self.coins = 0
        
    def load_data(self, file_name):
        with open(file_name, "r") as file:
            data = file.read().splitlines()
            if len(data) >= 5:
                self.name = data[0].split(": ")[1]
                self.weapon = data[1].split(": ")[1]
                self.armor = data[2].split(": ")[1]
                self.health = int(data[3].split(": ")[1])
                self.coins = int(data[4].split(": ")[1])
            else:
                print("Error: Invalid data format in knight.txt")
        
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
        print(f"Coins: {self.coins}")

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
        with open("knight.txt", "r") as f:
            lines = f.readlines()
            self.name = lines[0].strip()
            self.weapon = lines[1].strip()
            self.armor = lines[2].strip()
            #self.health = int(lines[3].strip())
            #self.coins = int(lines[4].strip())
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
        '''
        with open("knight.txt", "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Weapon: {self.weapon}\n")
            f.write(f"Armor: {self.armor}\n")
            f.write(f"Health: {self.health}\n")
            f.write(f"Coins: {self.coins}\n")  # write coins attribute to file
        '''

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
                
    def ready_to_fight(self):
        print("""
            KNIGHT                      
            
               /\\
              /--\\
             /    \\
             
        """)
        health_bar = self.get_health()
        print(health_bar)
        print("\n\n\n")
        
    def random_health_loss(self, damage):
        health_loss = random.randint(1, damage)
        self.health -= health_loss
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        else:
            return f"{self.name} takes {health_loss} damage!"
        '''    
    def turn_survival_start(self, enemy):
        # Knight attacks enemy      
        damage = random.randint(5, 20)
        print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
        enemy.defend(damage)

        # Enemy attacks Knight
        damage = random.randint(2, 6)
        print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
        self.defend(damage)
        
        print("""
            KNIGHT                      
            
               /\\
              /--\\
             /    \\
             
        """)
        health_bar = self.get_health()
        health_bar_E = enemy.get_health()
        print(health_bar + "            " + health_bar_E)
        '''
    def turn_survival_start(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(18, 25)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(11)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(1, 2)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                win = False
                return
                #break
                
            # Both Knight and enemy are still alive
            print("""
                KNIGHT                      
                
                   /\\
                  /--\\
                 /    \\
                 
            """)
            health_bar = self.get_health()
            health_bar_E = enemy.get_health()
            print(health_bar + "            " + health_bar_E)
            
            # Save the current health of the Knight to the variable
            knight_health = self.health
            
            KN_survival = """
                 _
                /_\\                        /\\
               -_|_-                       \\/
                /|\\   _____                ||
               /|||\\-|_____/         ---/-/  \\
                / \\                        / \\
               /   \\                      /   \\
            """
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament30(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(18, 25)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(20)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(14, 27)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                win = False
                return
                #break
                
            # Both Knight and enemy are still alive
            print("""
                KNIGHT                      
                
                   /\\
                  /--\\
                 /    \\
                 
            """)
            health_bar = self.get_health()
            health_bar_E = enemy.get_health()
            print(health_bar + "            " + health_bar_E)
            
            # Save the current health of the Knight to the variable
            knight_health = self.health
            
            KN_T30 = """
                 _                          __
                /_\\                       |/\\
               -_|_-                       \\/|
                /|\\   _____         ___    ||
               /|||\\-|_____/       |___|/-/||\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T30)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2


# Usage
#knight = Knight("Knight", "Sword", "Platemail")
#knight.print_attributes()
#knight.store_coins(50)


'''
print(knight.attack())
print(knight.defend(20))
print(knight.get_health())
print(knight.defend(20))
print(knight.get_health())
'''