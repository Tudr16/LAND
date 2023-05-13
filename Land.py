import os
import time
import msvcrt
#from knight import Knight
import matplotlib.pyplot as plt
import mplcursors
import random



'''
#global variables
global counter
counter = 0
'''


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
            
    def create_knight(name, weapon, armor):
        new_knight = Knight(name, weapon, armor)
        with open("knight.txt", "w") as f:
            f.write(f"Name: {new_knight.name}\n")
            f.write(f"Weapon: {new_knight.weapon}\n")
            f.write(f"Armor: {new_knight.armor}\n")
            f.write(f"Health: {new_knight.health}\n")
            f.write(f"Coins: {new_knight.coins}\n")
        return new_knight


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
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Congratulations!
                     
                """)
                time.sleep(1)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Congratulations!
                     Keep it like this!
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(9, 17)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Don't worry! You can try anytime and as many times as you want.
                     
                """)
                time.sleep(1)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
    def tournament29(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(9, 14)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(42)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Good job! At the limit!
                     
                """)
                time.sleep(1)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Good job! At the limit!
                     Your sword is a bit underwhelming...
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     How about we go to the store?
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     There you can upgrade your sword or buy something new!
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(22, 32)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     Get up!
                     Don't worry! Your sword is almost broken.
                     
                """)
                time.sleep(1)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     You must be careful...
                     Anyway, let's go to the store.
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     You must be careful...
                     Anyway, let's go to the store.
                     You need a stronger weapon or at least repair this one.
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T29 = """
                 _                         
                /_\\                       ___
               -_|_-                       \\/|
                /|\\   _____               _||_
               /|||\\-|_____/       /\\/|/-/||\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T29)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament28(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(34, 42)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(42)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     How cool...
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     He didn't even have time to blink!
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(12, 15)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW
                    
                       /\\
                      /00\\
                     /    \\
                     
                     It's okay! Maybe next time!
                     
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T29 = """
                 _                         
                /_\\                       ___
               -_|_-                       \\/|
                /|\\   _____               _||_
               /|||\\-|_____/       /\\/|/-/||\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T29)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament27(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(30, 38)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(67)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(16, 17)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T27 = """
                 _                         -_-
                /_\\                       /_\\_
               -_|_-                      -_|_-
                /|\\   _____               _|_
               /|||\\-|_____/    --------|-/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T27)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     By the way, if you noticed, the damage you give to the opponent depends on his armor.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     The exception is the soldiers, who train constantly to keep up with those who defeat them.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            
    def tournament26(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(30, 38)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(83)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(16, 17)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T26 = """
                 _                        |-_-|
                /_\\                      /..\\_
               -_|_-                      -_|_-
                /|\\   _____         _    _|||_
               /|||\\-|_____/       |_|----/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T26)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament25(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(30, 38)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(89)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(16, 17)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T25 = """
                 _                        |-_-|
                /_\\                      /..\\_
               -_|_-                _    -_|_-
                /|\\   _____        | |   _|||_
               /|||\\-|_____/      || |----/|\\
                / \\                |_|    / \\
               /   \\                     /   \\
            """
            print(KN_T25)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament24(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(30, 38)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(92)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(18, 24)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T24 = """
                 _                        |-_-|
                /_\\                      /..\\_
               -_|_-                _    -_|_-
                /|\\   _____        / \\  _|||_
               /|||\\-|_____/       | |----/|\\
                / \\                \_/    / \\
               /   \\                     /   \\
            """
            print(KN_T24)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Perfect! You defeated the Iron Stray group!
                     The last three were from this group.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again

    def tournament23(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(26, 30)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(102)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(16, 17)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T23 = """
                 _                         -_-
                /_\\                       |_|_
               -_|_-                      -_|_-
                /|\\   _____       ______  _|_
               /|||\\-|_____/      |_____|-/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T23)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            
    def tournament22(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(8, 12)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!")
                self.store_coins(150)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(18, 24)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Wow!...
                         
                """)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         It is the legendary Platemail armor...
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         I have never seen anything like this before.
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Sorry... Anyway, we need to get better equipment!
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         So, we must immediately visit the Store.
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                clear_screen()
                time.sleep(2)
                # Generate a random sleep time between 1 and 10 seconds
                sleep_time = random.randint(1, 7)
                #print(f"Sleeping for {sleep_time} seconds...")
                print("Loading your data...")
                time.sleep(sleep_time)
                clear_screen()
                sleep_time = random.randint(1, 12)
                print("Resuming your profile...")
                time.sleep(sleep_time)
                clear_screen()
                time.sleep(2)
                print("<Ok, you can choose something better or upgrade your equipment.>")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Look! Legendary Armor!
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Look! Legendary Armor!
                         But it costs many coins...
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         I don't have that much and we have to get that coins!
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         Listen! I know who the guy is... I have a perfect deal:
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         Let this guy give me everything he has and, not only will I give him armor, but I will upgrade him.
                         And I will also give him an amulet...
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         And the legendary weapon will be the Sword of Darkness.
                         Exactly as in the armor theme: darkness and strong.
                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         I kept this armor hidden... What you will see on the Bloody champion is a fake, but heavily upgraded.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         He is recognized by appearances, not by truth.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         He is recognized by appearances, not by truth.
                         So, listen to me old man, I entrust you with this armor because you will succeed in defeating the Black Knight.
                         I saw what you can do. You have potential and you are lucky to have Morow by your side.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         A long time ago, there was a rumor from a famous wizard that one day...

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         He predicted that someone strong enough would enter this land to defeat the Black Knight.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         There were several fighters who tried to free us from his curse, but they failed...

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         No one ever saw them again. We don't know where they disappeared.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         Only one fighter strong enough managed to reach the castle...

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         And through a flash of lightning appeared that statue that you see on your left, behind.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         Both in the hero's statue and in his stone sword, there is an essence of the Black Knight.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         And if somehow the sword will fall, the end will come...
                         Soon I can say.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         The wizard predicted all these things and his manuscript has been kept secret for many years.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         No one is allowed to see more in the manuscript than has been said.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         The rest of the pages are blank as far as I understand, but...
                         Only one person can see what is written on those pages and see with the mind's eye where that manuscript is.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         These words were read by the wizard himself that we discussed earlier.
                         He wrote many things in that manuscript...

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         But he died, unfortunately.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         But he died, unfortunately.
                         And no one knows anything about the manuscript anymore.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    SALES MAN                      
                    
                       /\\
                      /\-\\
                     /    \\
                     
                         It is said that there are dozens of pages that talk about...

                         
                """)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                time.sleep(5)
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         The sword just moved! Lucky it didn't fall...

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Something is happening.

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                print("""
                    MOROW                      
                    
                       /\\
                      /OO\\
                     /    \\
                     
                         Now, make the deal and let's go!

                         
                """)
                time.sleep(3)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {0}\n"
                    f.seek(0)
                    f.writelines(lines)
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
            
            KN_T22 = """
                 _                       |___|
                /_\\                     __\_/__
               -_|_-                     -_|_-
                /|\\   _____    _________  _|_
               /|||\\-|_____/   \______/-|-/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T22)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            '''
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Wow!...
                     
            """)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     It is the legendary Platemail armor...
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     I have never seen anything like this before.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Sorry... Anyway, we need to get better equipment!
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     So, we must immediately visit the Store.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            clear_screen()
            time.sleep(2)
            # Generate a random sleep time between 1 and 10 seconds
            sleep_time = random.randint(1, 7)
            #print(f"Sleeping for {sleep_time} seconds...")
            print("Loading your data...")
            time.sleep(sleep_time)
            clear_screen()
            sleep_time = random.randint(1, 12)
            print("Resuming your profile...")
            time.sleep(sleep_time)
            clear_screen()
            time.sleep(2)
            print("<Ok, you can choose something better or upgrade your equipment.>")
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Look! Legendary Armor!
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Look! Legendary Armor!
                     But it costs many coins...
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     I don't have that much and we have to get that coins!
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     Listen! I know who the guy is... I have a perfect deal:
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     Let this guy give me everything he has and, not only will I give him armor, but I will upgrade him.
                     And I will also give him an amulet...
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     And the legendary weapon will be the Sword of Darkness.
                     Exactly as in the armor theme: darkness and strong.
                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     I kept this armor hidden... What you will see on the Bloody champion is a fake, but heavily upgraded.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     He is recognized by appearances, not by truth.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     He is recognized by appearances, not by truth.
                     So, listen to me old man, I entrust you with this armor because you will succeed in defeating the Black Knight.
                     I saw what you can do. You have potential and you are lucky to have Morow by your side.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     A long time ago, there was a rumor from a famous wizard that one day...

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     He predicted that someone strong enough would enter this land to defeat the Black Knight.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     There were several fighters who tried to free us from his curse, but they failed...

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     No one ever saw them again. We don't know where they disappeared.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     Only one fighter strong enough managed to reach the castle...

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     And through a flash of lightning appeared that statue that you see on your left, behind.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     Both in the hero's statue and in his stone sword, there is an essence of the Black Knight.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     And if somehow the sword will fall, the end will come...
                     Soon I can say.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     The wizard predicted all these things and his manuscript has been kept secret for many years.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     No one is allowed to see more in the manuscript than has been said.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     The rest of the pages are blank as far as I understand, but...
                     Only one person can see what is written on those pages and see with the mind's eye where that manuscript is.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     These words were read by the wizard himself that we discussed earlier.
                     He wrote many things in that manuscript...

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     But he died, unfortunately.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     But he died, unfortunately.
                     And no one knows anything about the manuscript anymore.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                SALES MAN                      
                
                   /\\
                  /\-\\
                 /    \\
                 
                     It is said that there are dozens of pages that talk about...

                     
            """)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            time.sleep(5)
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     The sword just moved! Lucky it didn't fall...

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Something is happening.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Now, make the deal and let's go!

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            with open("knight.txt", "r+") as f:
                lines = f.readlines()
                lines[4] = f"Coins: {0}\n"
                f.seek(0)
                f.writelines(lines)
            '''
                
    def tournament21(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(70, 90)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!\n\n\n")
                print("SHOCK! The enemy is unconscious.\n\n")
                self.store_coins(150)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(4, 8)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T21 = """
               |___|                      |___|
              __\_/__                    __\_/__
               -_|_-                      -_|_-
                _|_  _________  _________  _|_ 
                /|\-|-\______/  \______/-|-/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T21)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     That's the true power of the Legendary Armor, son!

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     That's the true power of the Legendary Armor, son!
                     From now on, it will be much easier.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     I forgot the amulet at the Store. I'll go get it.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     With that, the sales man will tell me more about it.

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Good luck, my disciple! 

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW                      
                
                   /\\
                  /OO\\
                 /    \\
                 
                     Good luck, my disciple! 
                     You will do a good job even without my help!

                     
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            
    def tournament20(self, enemy):
        knight_health = self.health  # save the initial health of the Knight
    
        win = True
        #pw = 0
        while win:
            # Knight attacks enemy      
            damage = random.randint(70, 90)
            print(f"{self.name} hits {enemy.name} with {self.weapon} for {damage} damage.")
            #enemy.defend(damage + pw)
            enemy.defend(damage)

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {self.name} wins!\n\n\n")
                print("SHOCK! The enemy is unconscious.\n\n")
                self.store_coins(150)
                with open("knight.txt", "r+") as f:
                    lines = f.readlines()
                    lines[4] = f"Coins: {self.coins}\n"
                    f.seek(0)
                    f.writelines(lines)
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
                win = False
                return

            # Enemy attacks Knight
            damage = random.randint(4, 8)
            print(f"{enemy.name} hits {self.name} with {enemy.weapon} for {damage} damage.")
            self.defend(damage)

            # Check if Knight is defeated
            if self.health <= 0:
                print(f"{self.name} has been defeated! {enemy.name} wins!")
                print("Press any key to continue...")
                msvcrt.getch()  # Wait for user input to continue
                clear_screen()  # Recursively call the function to clear the screen again
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
            
            KN_T20 = """
               |___|                       ___
              __\_/__                     _\_/_
               -_|_-                       _|_
                _|_  _________             _|_ 
                /|\-|-\______/  --|--|---|-/|\\
                / \\                       / \\
               /   \\                     /   \\
            """
            print(KN_T20)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #pw += 2



# Read the counter value from the file
try:
    with open("data.txt", "r") as file:
        counter = int(file.read().strip())
except FileNotFoundError:
    # If the file doesn't exist yet, set the counter to 0
    #print("irnfurue")
    counter = 0


#functions
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix and Linux
    else:
        _ = os.system('clear')


Sword = """
     _
    /_\
    |_|
    |_|
____|_|_____
   |   |
   | | |
   | | |
   | | |
   | | |
   | | |
   | | |
   | | |
   |   |
   \   /
    \_/ 

"""

Axe = """
     /| ________________
(   / |/               /|
 \ /                    |
 |  ___                |
 | |   |_______________|
 | |   /               /  
 | |  /               /   
 | | /_______________/    
 |/_________________/     
 |
 |\\
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 |_|
"""

Spear = """
    
"""

Fork = """

"""

Amulet_Of_Twins = """
      .-=-.   .-==-.
    /  .-. \ / .-.  \
   |  /   \ | /   \ |
   | |\_.  | |  ._/|
   |\|  | \;-\ /;/ /
   \ `\_/'/  |  `\_/
    `._.'`-''--'`-'
""" 

'''
def MAP():

    # Define the coordinates of the locations
    mountain = (45.5231, -122.6765)
    guardians = (45.5263, -122.6709)
    survival = (45.5222, -122.6804)
    store = (45.5207, -122.6747)
    river = (45.5213, -122.6774)
    woods = (45.5234, -122.6725)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Draw a marker for the mountain with castle
    ax.plot(mountain[1], mountain[0], marker='^', markersize=10, color='black', label='Mountain with Castle')

    # Draw a marker for the guardians under the castle
    ax.plot(guardians[1], guardians[0], marker='o', markersize=10, color='red', label='Guardians Under Castle')

    # Draw a marker for the survival place
    ax.plot(survival[1], survival[0], marker='s', markersize=10, color='green', label='Survival Place')

    # Draw a marker for the store place
    ax.plot(store[1], store[0], marker='p', markersize=10, color='blue', label='Store Place')

    # Draw a marker for the river
    ax.plot(river[1], river[0], marker='o', markersize=10, color='cyan', label='River')

    # Draw a marker for the woods
    ax.plot(woods[1], woods[0], marker='s', markersize=10, color='brown', label='Woods')

    # Turn off the axes
    ax.axis('off')

    # Add a legend
    ax.legend(loc='upper left')

    # Enable interactive cursor for the markers
    cursor = mplcursors.cursor(hover=True)

    def on_click(event):
        label = event.artist.get_label()
        print(f'You clicked on the {label} marker.')

    cursor.connect('add', on_click)

    # Add annotations to the markers
    mountain_annotation = ax.annotate('Mountain with Castle', xy=mountain, xytext=(mountain[1]-0.002, mountain[0]-0.001))
    guardians_annotation = ax.annotate('Guardians Under Castle', xy=guardians, xytext=(guardians[1]+0.002, guardians[0]+0.001))
    survival_annotation = ax.annotate('Survival Place', xy=survival, xytext=(survival[1]+0.002, survival[0]-0.001))
    store_annotation = ax.annotate('Store Place', xy=store, xytext=(store[1]-0.002, store[0]+0.001))
    river_annotation = ax.annotate('River', xy=river, xytext=(river[1]-0.002, river[0]+0.001))
    woods_annotation = ax.annotate('Woods', xy=woods, xytext=(woods[1]+0.002, woods[0]-0.001))

    # Style the text annotations
    for annotation in [mountain_annotation, guardians_annotation, survival_annotation, store_annotation, river_annotation, woods_annotation]:
        annotation.set_bbox(dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
        annotation.set_alpha(0.8)

    # Show the plot
    plt.show()
'''


def MAP():
    # create a figure and axis object
    fig, ax = plt.subplots()

    # draw the existing mountain
    mountain_points = [(0, 0), (1, 2), (2, 1), (3, 3), (4, 1), (5, 2), (6, 0)]
    mountain_x, mountain_y = zip(*mountain_points)
    ax.plot(mountain_x, mountain_y, color='grey', linewidth=3, zorder=1)

    # draw trees
    tree_points = [(1, 0.5), (1.5, 1), (2, 0.5), (2.5, 1), (3, 0.5), (4, 1.5), (5, 0.5), (5.5, 1)]
    tree_x, tree_y = zip(*tree_points)
    ax.scatter(tree_x, tree_y, s=200, marker='^', color='green')

    # add circles with labels
    circle_points = [(1.1, 1.9), (3, 2.5), (5, 2), (2, 0.8)]
    circle_x, circle_y = zip(*circle_points)
    ax.scatter(circle_x, circle_y, s=200, marker='o', facecolors='none', edgecolors='red')

    # add labels to the circles
    ax.annotate('Survival Place', xy=circle_points[0], xytext=(circle_points[0][0]-0.3, circle_points[0][1]+0.2), color='red')
    ax.annotate('Bodyguards', xy=circle_points[1], xytext=(circle_points[1][0]-0.5, circle_points[1][1]+0.2), color='red')
    ax.annotate('Tournament', xy=circle_points[2], xytext=(circle_points[2][0]-0.5, circle_points[2][1]-0.2), color='red')
    ax.annotate('Store', xy=circle_points[2], xytext=(circle_points[3][0]-0.5, circle_points[3][1]-0.2), color='red')

    # remove axis spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # set axis limits and labels
    ax.set_xlim([0, 6])
    ax.set_ylim([0, 3])

    # remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    # show the plot
    plt.show()


def misterious_knight_statue():
    print("       /^\\                                                                        ")
    print("      /   \\                                                                       ")
    print("     / _ _ \\                                                                      ")
    print("    / /o o\\ \\                                                                    ")
    print("   /  \\   /  \\                                                                   ")
    print("  /____\\ /____\\                                                                  ")
    print("  [____][____]                                                                     ")
    print("   \\__/  \\__/                                                                    ")
    print("     |    |                                                                        ")
    print("     |    |                                                                        ")
    print("     |    |                                                                        ")
    print("     |    |                                                                        ")
    print("    /      \\                                                                      ")
    print("   |        |                                                                      ")
    print("   |        |                                                                      ")
    print("   |        |                                                                      ")
    print("   |________|                                                                      ")
    
    
def misterious_knight_statue_with_sword():
    print("""       /^\                                          /\                             _
      /   \                                        /  \                           /_\\
     / _ _ \                                    __/    \/\                        |_|
    / /o o\ \                                  /      _/                          |_|
   /  \    /  \                               |       |                       ____|_|____
  /____\  /____\                             /        |                          |   |
  [____][____]                               \        |                          | | |
   \__/  \__/                               __|       /                          | | |
     |    |                                / ________/                           | | |
     |    |                               /                                      | | |
     |    |                              /__                                     | | |
     |    |         _________________   / /                                      | | |
    /      \       /                 \_/ /                                       | | |
   |        |     /                       \                                      |   |
   |        |____/                         \__________________________________   \   /
   |        |                                                                 \   \_/
   |________|""")


def Karl():
    print("""
        KARL
        
           /\\
          /..\\
         / -- \\
         
         HEY! 
         Weapons down! What do you imagine you want to do?
         Get your hands off the monument before it's too late!
    """)
    time.sleep(7)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    print("""
        KARL
        
           /\\
          /..\\
         / -- \\
         
         Anyone who tries to get their hands on this statue will...
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    

def Saber():
    print("""
        SABER
        
         |    |
          \/\//
          /^0\\
         / /\\ \\
         
         That's enough!
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    print("""
        SABER
        
         |    |
          \/\//
          /^0\\
         / /\\ \\
         
         You stepped on our territory and tried to dirty the statue with your dirty hands... But one thing is certain:
    """)
    time.sleep(7)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    print("""
        SABER
        
         |    |
          \/\//
          /^0\\
         / /\\ \\
         
         You will die in my hands!
""")
    time.sleep(4)
    clear_screen()
    print("To be continue...")
    time.sleep(5)
    clear_screen()
    time.sleep(4)
    
    
def Game_Logo():
    print("""
        L         AAA    N   N   DDDDD  
        L        A   A   NN  N   D   D 
        L        AAAAA   N N N   D   D 
        L        A   A   N  NN   D   D 
        LLLLL    A   A   N   N   DDDDD  

           Welcome to Land!
""")

    time.sleep(5)
    clear_screen()
    time.sleep(3)
    
    
def Fighter_intro():
    print("""
        UNKNOWN FIGHTER
        
           /\\
          /00\\
         /    \\
         
         Don't you dare hit him with your sharp sword, Saber!
         He is under my guardianship. If anyone dares to harm them, your heads will sit on the crest of the mountain of eggs.
    """)
    time.sleep(7.5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    print("""
        SABER
        
         |    |
          \/\//
          /^0\\
         / /\\ \\
         
         Old man, you're lucky this time. But you will see...
    """)
    time.sleep(6)
    clear_screen()
    time.sleep(4)
    
    
def Friend():
    print("""
        UNKNOWN FIGHTER
        
           /\\
          /00\\
         /    \\
         
         Com'on! Let's go! You were seen by the guardians of the land!
         It's all good! But no matter how strong you are now, you couldn't have defeated them.
         You still don't understand what forces you will face here.
         I assume you're looking for the sphere, aren't you?
    """)
    time.sleep(8)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    time.sleep(2)
    print("""
        UNKNOWN FIGHTER
        
           /\\
          /00\\
         /    \\
         
         I understand that you are not too talkative, right?
         All right then. Follow me.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    time.sleep(3)
    print("""
        UNKNOWN FIGHTER
        
           /\\
          /00\\
         /    \\
         
         Oh, of course! I forgot to introduce myself. Before we get to the cave, I will tell you a few words about myself.
         My name is Morow, but I have many derivatives here.
    """)
    time.sleep(4)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #clear_screen()
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Oh, of course! I forgot to introduce myself. Before we get to the cave, I will tell you a few words about myself.
         My name is Morow, but I have many derivatives here. Until I arrived in this land, I traveled in many worlds... to put it this way...
         Totally different worlds from what you will see here and so far. But fear not, I will be your guide.
         I've been in your place, I've been through a lot here... The adventure is just beginning, son.
         I failed many times to reach what I am today, but with my help you will be able to overcome the paths through which I was overshadowed at that time.
         You can't go back... All the borders of this land are covered now.
         And you will failed or even be killed, as I have seen with my own eyes on various champions who did not expect what would follow.
         Here things do not work only with your training and experience. You will see this, old man.
    """)
    time.sleep(10)
    #clear_screen()
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Here I managed to impose my respect through tens or maybe even hundreds of fights.
         But I failed, unfortunately.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Here I managed to impose my respect through tens or maybe even hundreds of fights.
         But I failed, unfortunately.
         What you will have to do to be able to survive at least for a while. The rest will depend on you.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         As you have seen in the distance, there is a mountain. Look at him there.
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""                                                    /\                             _
                                                   /  \                           /_\\
                                                __/    \/\                        |_|
                                               /      _/                          |_|
                                              |       |                       ____|_|____
                                             /        |                          |   |
                                             \        |                          | | |
                                            __|       /                          | | |
                                           / ________/                           | | |
                                          /                                      | | |
                                         /__                                     | | |
                                _____   / /                                      | | |
                                     \_/ /                                       | | |
                                          \                                      |   |
                                           \__________________________________   \   /
                                                                              \   \_/
          """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         This mountain is guarded by 5 very powerful guardians. Up there is a rather small castle, but it houses the sphere of the eternal.
         It pulses an obscure power to the one who owns it. It was stolen by a black knight over two and a half meters tall, who is in that castle.
         All I know is that it's different...
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(2)
    print("To be continue...")
    time.sleep(5)
    clear_screen()
    time.sleep(4)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         And, by the way, this statue you wanted to touch is of another fighter who managed to defeat the guards, but in a few seconds he failed in front of the Black Knight.
         In this statue is part of the Knight's essence. Once it has been touched, he knows you are here and at any time unprecedented things can happen.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         And, by the way, this statue you wanted to touch is of another fighter who managed to defeat the guards, but in a few seconds he failed in front of the Black Knight.
         In this statue is part of the Knight's essence. Once it has been touched, he knows you are here and at any time unprecedented things can happen.
         He knows you're here... He sees everything you do through the guards... He controls their minds... He can control anyone's mind...
         Maybe right now you're doing him his will.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         The troops from the east are coming after us.
         Run away!
    """)
    time.sleep(4)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(2)
    print("To be continue...")
    time.sleep(5)
    clear_screen()
    time.sleep(4)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         In this forest, if we keep going forward, we will reach my cave.
         It will be our shelter for a long time.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(3)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         I made it on time!...
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         I made it on time!...
         Well, this is where I live. Let me introduce you to the new house.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    
    
def print_cave():
    print("               ___")
    print("           ___/   \___")
    print("      _____/         \_____")
    print("  ___/                    \___")
    print("/                               \\")
    print("|                                |")
    print("|      /\                /\     |")
    print("|     /  \              /  \    |")
    print("|    /    \            /    \   |")
    print("|___/      \__________/      \__|")
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    
    
def print_exit_cave():    
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         


         
    """)
    print("""
                 /\       
                /  \      
               /    \     
              /      \    
             /        \   
            /          \  
           /            \ 
          /  /\      /\  \\
         /  /  \____/  \  \\
        /  /    .        \ \\
       /  /     /\.       \ \\
      /__/     /..\\        \__\\   
          
          
          
          Here is the exit to the mountain.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         


         
    """)
    print("""
                 /\       
                /  \      
               /    \     
              /      \    
             /        \   
            /          \  
           /            \ 
          /  /\      /\  \\
         /  /  \____/  \  \\
        /  /    .        \ \\
       /  /     /\.       \ \\
      /__/     /..\\        \__\\  
          
          
          
          Here is the exit to the mountain.
          As you can see, its crest is in your sight from this point.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         


         
    """)
    print("""
                 /\       
                /  \      
               /    \     
              /      \    
             /        \   
            /          \  
           /            \ 
          /  /\      /\  \\
         /  /  \____/  \  \\
        /  /    .        \ \\
       /  /     /\.       \ \\
      /__/     /..\\        \__\\  
          
          
          
          Here is the exit to the mountain.
          As you can see, its crest is in your sight from this point.
          The three small dots represent the houses of the locals, respectively the guards.
          That point at the top represents the castle we talked about. It is not very clear. It's very far from here.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         


         
    """)
    print("""
                 /\       
                /  \      
               /    \     
              /      \    
             /        \   
            /          \  
           /            \ 
          /  /\      /\  \\
         /  /  \____/  \  \\
        /  /    .        \ \\
       /  /     /\.       \ \\
      /__/     /..\\        \__\\  
          
          
          
          Since the mountain is so far away, it is almost impossible for anyone to see us from there.
          On the other hand, it's just a cave on the outside.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again 
    
    
def print_legend():
    legend = """
        1: View map
        2: Survival place
        3: Tournament
        4: Store
        5: Bodyguards
        
        L: LEGEND
    """
    print(legend)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again 
    

def Hide_under_armor():
    time.sleep(7)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Now, if we come out of hiding, we will most likely be captured...
         How good that you have this helmet through which no one can see your identity very well!
         Well, look. I have an older armor, it's a little rusty, but it's very solid. Perfect for the beginning I can say.
    """)
    time.sleep(5)
    clear_screen()
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Now, if we come out of hiding, we will most likely be captured...
         How good that you have this helmet through which no one can see your identity very well!
         Look. I have an older armor, it's a little rusty, but it's very solid. Perfect for the beginning I can say.
         Now you won't be able to be recognized.
         But be careful. I advise you not to leave the land. Most likely you will not escape alive now.
         Wait a little longer, son. First of all, you have to get out of this mess.
         The Black Knight knows you're here regardless of your appearances.
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(2)
    print("To be continue...")
    time.sleep(5)
    clear_screen()
    time.sleep(4)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         He feels that you have come to steal his sphere of the eternal.
         It's not for nothing that the whole kingdom is on alert...
    """)
    time.sleep(5)
    clear_screen()
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         He feels that you have come to steal his sphere of the eternal.
         It's not for nothing that the whole kingdom is on alert...
         Anyway... That sphere, once used by the Black Knight, will mean the end of not only this land, but the whole world.
         A completely transformed world will be reborn... I don't even want to think about it now.
         
    """)
    time.sleep(5)
    clear_screen()
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         He feels that you have come to steal his sphere of the eternal.
         It's not for nothing that the whole kingdom is on alert...
         Anyway... That sphere, once used by the Black Knight, will mean the end of not only this land, but the whole world.
         A completely transformed world will be reborn... I don't even want to think about it now.
         Maybe you didn't come here by chance.
         But if you manage to defeat a few local champions, it means that you are truly ready to face the Black Knight.
         Although there were fighters who tried their best to prevent his evil plans... They failed.
         And that champion I discussed earlier was one of the most skilled so far.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(2)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Let's let destiny guide us in this long journey.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    time.sleep(2)
    print("To be continue...")
    time.sleep(5)
    clear_screen()
    time.sleep(4)
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Now, I will present you a small map of the entire land.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    MAP()
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         You can keep it for the moments when you will get lost in these places.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         I want to change my equipment so that no one can recognize me.
         After that, let's hit the road!
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    
    
def survival():
    cnt = 10
    print("<Now, you can view your fighter data:>")
    print("\n\n")
    #knight = Knight("Knight", "Sword", "Platemail")
    knight = Knight("", "", "")
    knight.load_data("knight.txt")
    #knight.print_attributes()
    solider = Knight("Solider", "Sword", "Chainmail")
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    knight.ready_to_fight()
    print(KN_start)
    time.sleep(5)
    clear_screen()
    print(KN_survival)
    time.sleep(2)
    clear_screen()
    knight.ready_to_fight()
    print(KN_survival)
    #
    while cnt >= 0:
        if cnt == 10:
            clear_screen()
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 9:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 8:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 7:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 6:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 5:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 4:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 3:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 2:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 1:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 0:
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            continue_story()
    
    
def tournament():
    if not os.path.exists("Tournament.txt"):
        with open("Tournament.txt", "w") as f:
            f.write("30")
    with open("Tournament.txt", "r") as f:
        cnt = int(f.read())
    if cnt == 30:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Kapa = Knight("Kapa", "Kapa's Sword", "Wind Armour")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T30)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T30)
        #
        clear_screen()
        knight.tournament30(Kapa)
        print(KN_T30)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
    elif cnt == 29:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Spin = Knight("Spin", "Spin's Sword", "Buffallo")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T29)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T29)
        #
        clear_screen()
        knight.tournament29(Spin)
        print(KN_T29)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Now, let's see what we find here.
             
        """)
        time.sleep(1.5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        time.sleep(2)
        print("Loading")
        time.sleep(0.3)
        clear_screen()
        print("Loading.")
        time.sleep(0.5)
        clear_screen()
        print("Loading..")
        time.sleep(1)
        clear_screen()
        print("Loading...")
        time.sleep(1)
        clear_screen()
        print("Loading")
        clear_screen()
        print("Loading.")
        time.sleep(2)
        clear_screen()
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             With your money we can't buy something new... Or even upgrade your equipment.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             But I will give you money now for a small upgrade!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        time.sleep(4)
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Here you go!
             
        """)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Here you go! Now, take a deep breath and try to fight again!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
            
        
    elif cnt == 28:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Spin = Knight("Spin", "Spin's Sword", "Buffallo")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T29)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T29)
        #
        clear_screen()
        knight.tournament28(Spin)
        print(KN_T29)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 27:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Leadam = Knight("Leadam", "Katana", "Obsolette")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T27)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T27)
        #
        clear_screen()
        knight.tournament27(Leadam)
        print(KN_T27)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 26:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Matchet = Knight("Matchet", "Matchet's Mace", "Iron Stray")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T26)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T26)
        #
        clear_screen()
        knight.tournament26(Matchet)
        print(KN_T26)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 25:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Maya = Knight("Maya", "Maya's Hammer", "Iron Stray")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T25)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T25)
        #
        clear_screen()
        knight.tournament25(Maya)
        print(KN_T25)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 24:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Lion = Knight("Lion", "Lion's Lame", "Iron Stray")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T24)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T24)
        #
        clear_screen()
        knight.tournament24(Lion)
        print(KN_T24)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 23:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Buch = Knight("Buch", "Buch's Baton", "Common Legendary")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T23)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T23)
        #
        clear_screen()
        knight.tournament23(Buch)
        print(KN_T23)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 22:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Bloody = Knight("Bloody", "Bloody's Sword", "Legendary Platemail")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN_start)
        time.sleep(5)
        clear_screen()
        print(KN_T22)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T22)
        #
        clear_screen()
        knight.tournament22(Bloody)
        print(KN_T22)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 21:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight.create_knight("Knight", "Sword of Darkness", "Legendary Platemail")  # call the function using module name
        #knight = Knight("", "", "")
        #knight.load_data("knight.txt")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Bloody = Knight("Bloody", "Bloody's Sword", "Legendary Platemail")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN)
        time.sleep(5)
        clear_screen()
        print(KN_T21)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T23)
        #
        clear_screen()
        knight.tournament21(Bloody)
        print(KN_T21)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 20:
        clear_screen()
        print("<Now, you can view your fighter data:>")
        print("\n\n")
        #knight = Knight("Knight", "Sword", "Platemail")
        knight = Knight("", "", "")
        knight.load_data("knight.txt")
        #knight.print_attributes()
        Wired = Knight("Wired", "Wired's Wierd Sword", "Iron Fist")
        time.sleep(5)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        knight.ready_to_fight()
        print(KN)
        time.sleep(5)
        clear_screen()
        print(KN_T20)
        time.sleep(2)
        clear_screen()
        knight.ready_to_fight()
        print(KN_T20)
        #
        clear_screen()
        knight.tournament20(Wired)
        print(KN_T20)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.ready_to_fight()
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 19:
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Go, go!
             The Black Knight saw that it was you who touched the statue!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             I don't know how he realized...
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             We don't have time to talk anymore!
             We have to move fast!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        time.sleep(2)
        print("To be continue...")
        time.sleep(5)
        clear_screen()
        time.sleep(4)
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             There were at least 15 more champions to defeat, but you trained enough.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             I think that's why the sword moved.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             His nervousness made this…
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        time.sleep(2)
        print("To be continue...")
        time.sleep(5)
        clear_screen()
        time.sleep(4)
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Oh no!... Our cave is on fire...
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             It means that the only option is to go to the castle.
             We have nowhere else to go.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             This is not just any fire, it is a fire that burns forever...
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Perfect! Even better!
             You can use this amulet to devastate the entire castle!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             It's just that... It has only one use.
             It contains the magic of the wizard you heard about earlier.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             That amulet is very strong, no one knows about her, except the seller who was his very close friend.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Don't worry, son. The amulet will know when it's time to use it better than we do.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Don't worry, son. The amulet will know when it's time to use it better than we do.
             It will light up when it wants to pulsate an unimaginable power.
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             It was an honor to have you by my side, Knight!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        print("""
            MOROW
            
               /\\
              /00\\
             /    \\
             
             Now go! I will sit here and watch this evil knight be defeated!
             
        """)
        time.sleep(3)
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        cnt -= 1
        with open("Tournament.txt", "w") as f:
            f.write(str(cnt))
            
    elif cnt == 18:
        print("<No time to fight champions now!>")
        print("<Go to the bodyguards!>")
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        
        
    
def bodyguards():
    if not os.path.exists("Tournament.txt"):
        with open("Tournament.txt", "w") as f:
            f.write("30")
    if not os.path.exists("Bodyguards.txt"):
        with open("Bodyguards.txt", "w") as f:
            f.write("5")
    with open("Tournament.txt", "r") as f:
        cnt = int(f.read())
    if cnt > 18:
        print("<You are not trained enough to face the guards...>")
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
    else:
        bodyguards1()
        
        
def bodyguards1():
    pass
    
    
def store():
    clear_screen()
    time.sleep(2)
    # Generate a random sleep time between 1 and 10 seconds
    sleep_time = random.randint(1, 7)
    #print(f"Sleeping for {sleep_time} seconds...")
    print("Loading your data...")
    time.sleep(sleep_time)
    clear_screen()
    sleep_time = random.randint(1, 12)
    print("Resuming your profile...")
    time.sleep(sleep_time)
    clear_screen()
    time.sleep(2)
    print("<According to your evolution, no changes or improvements are necessary.>")
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("<We will see your evolution next time.>")
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    
    
KN_T30 = """
     _                          __
    /_\\                       |/\\
   -_|_-                       \\/|
    /|\\   _____         ___    ||
   /|||\\-|_____/       |___|/-/||\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T29 = """
     _                         
    /_\\                       ___
   -_|_-                       \\/|
    /|\\   _____               _||_
   /|||\\-|_____/       /\\/|/-/||\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T27 = """
     _                         -_-
    /_\\                       /_\\_
   -_|_-                      -_|_-
    /|\\   _____               _|_
   /|||\\-|_____/    --------|-/|\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T26 = """
     _                        |-_-|
    /_\\                      /..\\_
   -_|_-                      -_|_-
    /|\\   _____         _    _|||_
   /|||\\-|_____/       |_|----/|\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T25 = """
     _                        |-_-|
    /_\\                      /..\\_
   -_|_-                _    -_|_-
    /|\\   _____        | |   _|||_
   /|||\\-|_____/      || |----/|\\
    / \\                |_|    / \\
   /   \\                     /   \\
"""


KN_T24 = """
     _                        |-_-|
    /_\\                      /..\\_
   -_|_-                _    -_|_-
    /|\\   _____        / \\  _|||_
   /|||\\-|_____/       | |----/|\\
    / \\                \_/    / \\
   /   \\                     /   \\
"""


KN_T23 = """
     _                         -_-
    /_\\                       |_|_
   -_|_-                      -_|_-
    /|\\   _____       ______  _|_
   /|||\\-|_____/      |_____|-/|\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T22 = """
     _                       |___|
    /_\\                     __\_/__
   -_|_-                     -_|_-
    /|\\   _____    _________  _|_
   /|||\\-|_____/   \______/-|-/|\\
    / \\                       / \\
   /   \\                     /   \\
"""
    

KN_T21 = """
   |___|                      |___|
  __\_/__                    __\_/__
   -_|_-                      -_|_-
    _|_  _________  _________  _|_ 
    /|\-|-\______/  \______/-|-/|\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN_T20 = """
   |___|                       ___
  __\_/__                     _\_/_
   -_|_-                       _|_
    _|_  _________             _|_ 
    /|\-|-\______/  --|--|---|-/|\\
    / \\                       / \\
   /   \\                     /   \\
"""


KN = """
   |___|            
  __\_/__           
   -_|_-            
    _|_  _________  
    /|\-|-\______/  
    / \\            
   /   \\                            
""" 

    
KN_start = """
     _
    /_\\                        
   -_|_-                        
    /|\\   _____                
   /|||\\-|_____/        
    / \\                        
   /   \\                     
"""    


KN_survival = """
     _
    /_\\                        /\\
   -_|_-                       \\/
    /|\\   _____                ||
   /|||\\-|_____/         ---/-/  \\
    / \\                        / \\
   /   \\                      /   \\
"""

    
def survival_start():
    cnt = 10
    print("<Now, you can view your fighter data:>")
    print("\n\n")
    knight = Knight("Knight", "Sword", "Platemail")
    knight.print_attributes()
    solider = Knight("Solider", "Sword", "Chainmail")
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Now, let's see your training!
         
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    knight.ready_to_fight()
    print(KN_start)
    time.sleep(5)
    clear_screen()
    print(KN_survival)
    time.sleep(2)
    clear_screen()
    knight.ready_to_fight()
    print(KN_survival)
    #
    while cnt >= 0:
        if cnt == 10:
            clear_screen()
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 9:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 8:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 7:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 6:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 5:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 4:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 3:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 2:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 1:
            clear_screen()
            #knight = Knight("Knight", "Sword", "Platemail")
            solider = Knight("Solider", "Sword", "Chainmail")
            print(KN_start)
            time.sleep(5)
            clear_screen()
            print(KN_survival)
            time.sleep(2)
            clear_screen()
            knight.ready_to_fight()
            print(KN_survival)#
            knight.turn_survival_start(solider)
            print(KN_survival)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            #knight.ready_to_fight()
            cnt -= 1
        elif cnt == 0:
            print("""
                MOROW
                
                   /\\
                  /00\\
                 /    \\
                 
                 Wow...
                 
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW
                
                   /\\
                  /00\\
                 /    \\
                 
                 I have never seen such a fighting style before!
                 It's amazing!
                 
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            print("""
                MOROW
                
                   /\\
                  /00\\
                 /    \\
                 
                 And you passed all the rounds... You are capable, son.
                 
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            time.sleep(2)
            print("To be continue...")
            time.sleep(5)
            clear_screen()
            time.sleep(4)
            print("""
                MOROW
                
                   /\\
                  /00\\
                 /    \\
                 
                 Hmm... I'm thinking about it.
                 But in the meantime, how about trying a fight with one of the local champions?
                 
            """)
            time.sleep(3)
            print("Press any key to continue...")
            msvcrt.getch()  # Wait for user input to continue
            clear_screen()  # Recursively call the function to clear the screen again
            legend_open = False
            while not legend_open:
                print("<Type L to reopen the legend.>")
                choose = input()
                if choose.lower() == "l":
                    print_legend()
                    legend_open = True
                    clear_screen()  # Recursively call the function to clear the screen again
                else:
                    print("Invalid input. Please try again!")
                    clear_screen()  # Recursively call the function to clear the screen again
            tournament_open = False
            while not tournament_open:
                print("<Type 3 to go to tournament place.>")
                choose = input()
                if choose== "3":
                    tournament_start()
                    tournament_open = True
                    clear_screen()  # Recursively call the function to clear the screen again
                else:
                    print("Invalid input. Please try again!")
                    clear_screen()  # Recursively call the function to clear the screen again
            cnt -= 1


def tournament_start():
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Here is the tournament place. Before moving on, don't let yourself be influenced by their appearances.
         
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Here is the tournament place. Before moving on, don't let yourself be influenced by their appearances.
         They are also remarkable for their scary appearance.
         
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         If you want, you can still train in survival place before any fight you will have here.
         
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    continue_story()###############
    #main_story()#######
#survival_start()#################################################    
    
def Game_rules():
    print("<Legend>")
    print_legend()
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Now, let me introduce you to these places:
         
    """)
    time.sleep(3)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Survival place is the place where you can win nice amounts of gold, but you will have rounds after rounds.
         And in total there are ten rounds, and in each round you have to defeat one soldier.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Tournament place is where some local champions are.
         They are difficult to beat, but if you take it gradually with your training, everything will be fine.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         Store it is the place where you can buy a new armor in case the old one no longer strong.
         And, of course, a new weapon if necessary.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         And, last but not least, there is the place where the guards serve the Black Knight.
         We can't even think of defeating them at the moment.
         They are very well skilled...
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    print("""
        MOROW
        
           /\\
          /00\\
         /    \\
         
         For now, my advice is to start with Survival place.
         
    """)
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #choose = input()
    legend_open = False
    while not legend_open:
        print("<Type L to reopen the legend.>")
        choose = input()
        if choose.lower() == "l":
            print_legend()
            legend_open = True
            clear_screen()  # Recursively call the function to clear the screen again
        else:
            print("Invalid input. Please try again!")
            clear_screen()  # Recursively call the function to clear the screen again
    survival_open = False
    while not survival_open:
        print("<Type 2 to go to survival.>")
        choose = input()
        if choose== "2":
            survival_start()
            survival_open = True
            clear_screen()  # Recursively call the function to clear the screen again
        else:
            print("Invalid input. Please try again!")
            clear_screen()  # Recursively call the function to clear the screen again    
    

def start_story():
    global counter
    counter += 1
    print("History says that...")
    time.sleep(3)
    clear_screen()
    print("Once upon a time there was a powerfull knight...")
    time.sleep(3)
    clear_screen()
    print("who traveled the world far and wide, until...")
    time.sleep(5)
    clear_screen()
    print("he found a gigantic mysterious statue.")
    time.sleep(6)
    clear_screen()
    time.sleep(2)
    misterious_knight_statue()
    time.sleep(4)
    print("\n\n\n"+"Next to this statue, on the other side of the water, was a gigantic sword, petrified. He simply rested on its top.")
    time.sleep(5)
    clear_screen()
    print("Next to this statue, on the other side of the water, was a gigantic sword, petrified. He simply rested on its top.")
    time.sleep(4)
    clear_screen()
    time.sleep(2)
    misterious_knight_statue_with_sword()
    time.sleep(5)
    clear_screen()
    print("The knight wanted to approach the mysterious statue...")
    time.sleep(2)
    clear_screen()
    time.sleep(2)
    Karl()
    Saber()
    Game_Logo()
    Fighter_intro()
    Friend()
    print_cave()
    print_exit_cave()
    Hide_under_armor()
    Game_rules()
    
    
'''
def continue_story():
    #print("continue_story")
    #survival_start()#######
    clear_screen()  # Recursively call the function to clear the screen again
    legend_open = False
    while not legend_open:
        print("<Type L to open the legend.>")
        choose = input()
        if choose.lower() == "l":
            print_legend()
            legend_open = True
            clear_screen()  # Recursively call the function to clear the screen again
            print("<Choose a valid number: >")#######
            choose1 = input()
            if choose1 == 1:
                MAP()
            elif choose1 == 2:
                survival()
            elif choose1 == 3:
                tournament()
            elif choose1 == 4:
                store()
            elif choose1 == 5:
                bodyguards()
            else:
                print("Invalid input. Please try again!")
                clear_screen()  # Recursively call the function to clear the screen again
        else:
            print("Invalid input. Please try again!")
            clear_screen()  # Recursively call the function to clear the screen again
    """
    tournament_open = False
    while not tournament_open:
        print("<Type 3 to go to tournament place.>")
        choose = input()
        if choose== "3":
            tournament()
            tournament_open = True
            clear_screen()  # Recursively call the function to clear the screen again
        else:
            print("Invalid input. Please try again!")
            clear_screen()  # Recursively call the function to clear the screen again
        survival_open = False
    while not survival_open:
        print("<Type 2 to go to survival.>")
        choose = input()
        if choose== "2":
            survival_start()
            survival_open = True
            clear_screen()  # Recursively call the function to clear the screen again
        else:
            print("Invalid input. Please try again!")
            clear_screen()  # Recursively call the function to clear the screen again
    """
'''
    
    
def continue_story():
    clear_screen()  # Recursively call the function to clear the screen again
    while True:
        clear_screen()
        legend_open = False
        while not legend_open:
            print("<Type L to open the legend.>")
            choose = input()
            if choose.lower() == "l":
                print_legend()
                legend_open = True
            else:
                print("Invalid input. Please try again!")
                clear_screen()
        print("<Choose a valid number: >")
        choose1 = input()
        if choose1 == "1":
            MAP()
        elif choose1 == "2":
            survival()
        elif choose1 == "3":
            tournament()
        elif choose1 == "4":
            store()
        elif choose1 == "5":
            bodyguards()
        else:
            print("Invalid input. Please try again!")
        input("<Press enter to continue>")


# Read the counter value from the file
try:
    with open("data.txt", "r") as file:
        #print("is ok!")
        counter = int(file.read().strip())
except FileNotFoundError:
    # If the file doesn't exist yet, set the counter to 0
    counter = 0
except Exception as e:
    print(f"Error occurred while reading file: {e}")

def main_story():
    global counter
    if counter >= 1:
        continue_story()
    elif counter == 0:
        start_story()
        #print("Start story...\n\n\n")
        counter += 1
        
        # Write the updated counter value to the file
        try:
            with open("data.txt", "w") as file:
                #print("is ok")
                file.write(str(counter))
                #print(counter)
        except Exception as e:
            print(f"Error occurred while writing file: {e}")
        
        # Read the counter value from the file to make sure memory and file are in sync
        try:
            with open("data.txt", "r") as file:
                counter = int(file.read().strip())
        except Exception as e:
            print(f"Error occurred while reading file: {e}")



#call functions
main_story()
