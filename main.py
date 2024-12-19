#This script is the main script that will be run to start the program
import utility_functions as utils
import final_challenge as final
def game():
    utils.introduction()
    team=utils.compose_team()
    utils.choose_player(team)
def challenge():
    utils.challenge_menu()
class keys ():
    def __init__(self):
        self.keys=0
    def add_key(self):
        self.keys+=1
        print("You have obtained a key!")
        print("You have",self.keys,"key(s)")
        return self.keys
    def check_keys(self):
        if self.keys==3:
            print("You have obtained all the keys!")
            return True
        else:
            return False
if __name__ == "__main__":
    game()
    i,keys=1,keys()
    while i<=5 and keys.keys<=3:
        if challenge():
            keys.add_key()
        i+=1
    if keys.check_keys():
        print("Congratulations! You have unlocked the treasure room!")
        final.treasure_room()
    else:
        print("You have failed to obtain all the keys. The treasure room remains locked.")