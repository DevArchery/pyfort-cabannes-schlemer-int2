import json
import random as rnd
from toolbox import uppercase

def load_riddles(file:str):
    """Load the riddles from a json file so they can be used in the game"""
    with open(file, "r", encoding="UTF-8") as file:
        riddles=json.load(file)
        return riddles

def pere_fouras_riddles()->bool:
    """Select a random riddle from the list and ask the player to guess the answer"""
    riddles=load_riddles("data/PFRiddles.json")
    riddle=rnd.choice(riddles)
    print(riddle["question"])
    tries=3
    while tries>=1:
        guess = input()
        size=len(riddle["answer"])
        if 'the' in riddle["answer"]:
            size-=3
        if uppercase(guess) in uppercase(riddle["answer"]) and len(guess)==size:
            print("Congratulations! You found the answer!")
            return True
        else:
            print(f"You have {tries-1} tries left")
        tries-=1
    print("You lost! The answer was", riddle["answer"])
    return False

if __name__ == "__main__":
    pere_fouras_riddles()