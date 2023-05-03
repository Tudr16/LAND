import os
import time
import msvcrt


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
    
"""

Yari = """
    
"""


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
#start_story()
main_story()
