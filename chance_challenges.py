#this script will regroup the luck based challenges
##imports
import random as rnd
import toolbox as tools

##script
def shell_game(nb=3)->bool:
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

def roll_dice_game(nbthrows=3)->bool:
    throws,finished=1,False
    while throws<=nbthrows:
        player, game_master = (rnd.randint(1, 6), rnd.randint(1, 6)) , (rnd.randint(1, 6), rnd.randint(1, 6))
        for i in range(2):
            if player[i]==6 and game_master[i]!=6:
                print("You won!")
                return True
            elif player[i]!=6 and game_master[i]==6:
                print("You lost!")
                return False
            else:
                print("It's a draw! Let's roll again!")
        throws+=1
    print("The game master won by default!")
    return False
def chance_challenges():
    challenges=[shell_game, roll_dice_game]
    return rnd.choice(challenges)(rnd.randint(3,5))