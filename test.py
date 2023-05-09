import time
import os
import msvcrt
import matplotlib.pyplot as plt
import mplcursors
from knight import Knight

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
# knight.py

class Knight:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = 100

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

    def get_health(self):
        bar_size = 20  # size of the life bar
        current_health = int((self.health / 100) * bar_size)
        life_bar = "[" + "#" * current_health + "-" * (bar_size - current_health) + "]"
        return f"{self.name}'s health: {life_bar}"


# Usage
knight = Knight("Sir Lancelot", "Excalibur", "Chainmail")
print(knight.attack())
print(knight.defend(20))
print(knight.get_health())
print(knight.defend(20))
print(knight.get_health())
'''

'''
import matplotlib.pyplot as plt

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
'''

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

MAP()
'''


'''
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
knight.print_attributes()

# Save knight data to file
knight.print_attributes()

# Load knight data from file
knight.open_data_knight()
knight.print_attributes()
'''


'''
print(knight.attack())
print(knight.defend(20))
print(knight.get_health())
print(knight.defend(20))
print(knight.get_health())
'''





'''
KN = """
     _
    /_\\
   -_|_-
    /|\\   _____
   /|||\\-|_____/
    / \\
   /   \\
"""

print(KN)
'''

'''
knight = Knight("Knight", "Sword", "Platemail")
knight.ready_to_fight()
'''

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
knight = Knight("Knight", "Sword", "Platemail")
solider = Knight("Solider", "Sword", "Chainmail")
time.sleep(2)
clear_screen()
knight.ready_to_fight()
print(KN_survival)
#


'''
#knight.random_health_loss(5)
knight.defend(5)
clear_screen()
knight.ready_to_fight()
print(KN_survival)
##
#knight.random_health_loss(5)
knight.defend(5)
clear_screen()
knight.ready_to_fight()
print(KN_survival)
'''

clear_screen()
knight.turn_survival_start(solider)
print(KN_survival)
print("Press any key to continue...")
msvcrt.getch()  # Wait for user input to continue
clear_screen()  # Recursively call the function to clear the screen again
#knight.ready_to_fight()

'''
    if knight.health == 0:
        print("Solider wins...\n")
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        win = False
    elif solider.health == 0:
        print("Knight wins...\n")
        print("Press any key to continue...")
        msvcrt.getch()  # Wait for user input to continue
        clear_screen()  # Recursively call the function to clear the screen again
        #knight.store_coins(11)
        
        win = False
'''
'''
    clear_screen()
    knight.turn_survival_start(solider)
    print(KN_survival)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    #knight.ready_to_fight()
'''




































































print("Press any key to continue...")
msvcrt.getch()  # Wait for user input to continue
clear_screen()  # Recursively call the function to clear the screen again
