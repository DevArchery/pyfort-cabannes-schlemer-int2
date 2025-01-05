import utility_functions as utils
import final_challenge as final
from toolbox import uppercase

def game():
    """Main function to run the game"""
    utils.introduction()
    team = utils.compose_team()
    keys = Keys()
    attempts = 5
    challenges_attempted = 0
    wins = 0
    losses = 0

    while attempts > 0:
        if keys.check_keys():
            break
        utils.choose_player(team)
        if utils.challenge_menu():
            keys.add_key()
            wins += 1
        else:
            losses += 1
        challenges_attempted += 1
        attempts -= 1

    code_word_found = keys.check_keys()
    if code_word_found:
        print("Congratulations! You have unlocked the treasure room!")
        final.treasure_room()
    else:
        print("You have failed to obtain all the keys. The treasure room remains locked.")
    if uppercase(input("Would you like to save your game results? (y/n): ")) == "Y":
        save_game_results(challenges_attempted, wins, losses, code_word_found)

def save_game_results(challenges_attempted, wins, losses, code_word_found):
    with open("game_results.txt", "a") as file:
        file.write(f"Challenges Attempted: {challenges_attempted}\n")
        file.write(f"Successful attempts: {wins}\n")
        file.write(f"Failed attempts: {losses}\n")
        file.write(f"Code Word Found: {'Yes' if code_word_found else 'No'}\n")
        file.write("\n")

class Keys:
    """Class to keep track of the keys obtained by the player"""
    def __init__(self):
        self.keys = 0

    def add_key(self):
        self.keys += 1
        print("You have obtained a key!")
        print("You have", self.keys, "out of 3 keys")
        return self.keys

    def check_keys(self):
        if self.keys >= 3:
            print("You have obtained all the keys!")
            return True
        else:
            return False

if __name__ == "__main__":
    game()