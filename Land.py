import os
import time
import msvcrt
from knight import Knight
import matplotlib.pyplot as plt
import mplcursors



'''
#global variables
global counter
counter = 0
'''


# Read the counter value from the file
try:
    with open("data.txt", "r") as file:
        counter = int(file.read().strip())
except FileNotFoundError:
    # If the file doesn't exist yet, set the counter to 0
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
         
         Now, I will present you a small map of the entire country.
         
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
    pass
    
    
def survival_start():
    print("<Now, you can view your fighter data:>")
    print("\n\n\n")
    knight = Knight("Knight", "Sword", "Chainmail")
    knight.print_attributes()
    time.sleep(5)
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for user input to continue
    clear_screen()  # Recursively call the function to clear the screen again
    
    
    
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
    
    
    
def continue_story():
    print("continue_story")
    
    
def main_story():
    global counter
    if counter >= 1:
        continue_story()
    elif counter == 0:
        start_story()
        counter += 1
        # Write the updated counter value to the file
        with open("data.txt", "w") as file:
            file.write(str(counter))
            
        # Read the counter value from the file to make sure memory and file are in sync
        with open("data.txt", "r") as file:
            counter = int(file.read().strip())


#call functions
main_story()
