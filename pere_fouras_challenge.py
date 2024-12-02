import json
import random as rnd
from toolbox import uppercase

def load_riddles(file:str):
    with open(file, "r", encoding="UTF-8") as file:
        riddles=json.load(file)
        return riddles

def pere_fouras_riddles()->bool:
    riddles=load_riddles("data/PFRiddles.json")
    print(riddles)
    riddle=rnd.choice(riddles)
    print(riddle["question"])
    guess=input()
    tries=3
    while tries>1:
        if uppercase(guess)==uppercase(riddle["answer"]):
            print("Congratulations! You found the answer!")
            return True
        else:
            print("You have", tries-1, "tries left")
        tries-=1
        guess=input()
    print("You lost! The answer was", riddle["answer"])
    return False
pere_fouras_riddles()
