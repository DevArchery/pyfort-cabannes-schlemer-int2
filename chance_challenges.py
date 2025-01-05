#this script will regroup the luck based challenges
##imports
import random as rnd
import toolbox as tools
from time import sleep
##script
def shell_game(nb=rnd.randint(3,5))->bool:
    """Implement the shell game, where the player has to guess which shell contains the key"""
    print(f"A key is hidden under one of {nb} shells. Guess which shell it is in {nb-1} tries or less to get it")
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

def roll_dice_game(nbthrows=rnd.randint(3,5))->bool:
    """Implement a die game where the player has to roll two dices against the game master. The player wins if they roll
    a 6"""
    throws,finished=1,False
    while throws<=nbthrows:
        while input("Press enter to roll the dice")!="":
            print("Please press enter to roll the dice")
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

#Buckshot roulette
class Player:
    """Implement a player class with a name"""
    def __init__(self,name:str):
        self.name=name
        self.alive=True
        self.shocks=3
    def check_status(self):
        if self.shocks==0:
            self.alive=False
            print(f"{self.name} has no shocks left!")
            return False
        else:
            print(f"{self.name} has {self.shocks} shocks left!")
            return True
class Shotgun:
    """Implement a shotgun class with a magazine and a chamber"""
    def __init__(self):
        self.mag=[]
        self.chamber=None
    def empty(self):
        return True if self.mag==[] else False
    def load(self):
        self.rounds=rnd.randint(1,8)
        for i in range(self.rounds):
            self.mag.append("L" if rnd.randint(0,1)==1 else "B")
    def clear_load(self):
        print(("L",self.mag.count("L")),("B",self.mag.count("B")))
    def chamber(self):
        self.chamber=self.mag.pop()
    def fire(self,target):
        if self.chamber=="L":
            target.shocks-=1
            print(f"{target.name} has been shot!")
        else:
            print("Click!")
            print("It's a blank!")
        self.chamber=self.mag.pop()
    def turn(self,shooter:Player):
        print(f"{shooter.name}'s turn!")
        print("Who do you want to shoot?")
        target=input()
        print("Firing the shotgun")
        self.fire(target)


def roulette():
    """Starts the roulette game"""
    turn = 1
    dealer = Player("Dealer")
    name=str(input("Enter your name:"))
    player = Player(name)
    shotgun = Shotgun()

    while player.alive and dealer.alive:
        if shotgun.empty():
            shotgun.load()
            shotgun.clear_load()
            shotgun.chamber = shotgun.mag.pop()
            turn = 1

        if turn % 2 == 0:
            print(f"{dealer.name}'s turn!")
            l_count = shotgun.mag.count("L")
            b_count = shotgun.mag.count("B")
            if l_count > b_count:
                print(f"{dealer.name} chose to shoot {player.name}!")
                shotgun.fire(player)
                if player.alive:
                    turn += 2
            else:
                print(f"{dealer.name} chose to shoot {dealer.name}!")
                if shotgun.chamber == "B":
                    turn += 1
                else:
                    turn += 2
                shotgun.fire(dealer)
                sleep(2)

        else:
            print(f"{player.name}'s turn!")
            print("Who do you want to shoot? (Dealer/Yourself)")
            target_name = input().strip().lower()
            if target_name == "dealer":
                shotgun.fire(dealer)
                if dealer.alive:
                    turn += 2
            elif target_name == "yourself":
                if shotgun.chamber == "B":
                    turn += 1
                else:
                    turn += 2
                shotgun.fire(player)
            else:
                print("Invalid choice. Skipping turn.")
            sleep(2)

        player.check_status()
        dealer.check_status()
        turn += 1
def chance_challenges():
    """Select a random luck based challenge"""
    challenges=[shell_game, roll_dice_game,roulette]
    return rnd.choice(challenges)()