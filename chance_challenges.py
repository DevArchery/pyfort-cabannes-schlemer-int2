#this script will regroup the luck based challenges
##imports
import random as rnd
import toolbox as tools
##script
def shell_game(nb=3):
    """Implement the shell game, where the player has to guess which shell contains the key. nb is the number of shells
    and is set to 3 by default"""
    print("A key is hidden under one of three shells. Guess which shell it is in 2 tries or less to get it")
    shells=[chr(65+i) for i in range(nb)]
    print("The shells are labeled", shells)
    key=rnd.choice(shells)
    guess=None
    print("Which shell is the key under? ")
    while len(shells)>1:
        while guess not in shells:
            print("Please enter a valid shell :", shells)
            guess=tools.uppercase(str(input()))
            print("You entered", guess)
        if guess==key:
            print("Congratulations! You found the key!")
            return True
        else:
            shells=tools.remove_value(shells, guess)
            print("The key is not under shell", guess)
            print("Which shell is the key under? ")
            guess=None
    print("You lost! The key was under the shell", key)
    return False