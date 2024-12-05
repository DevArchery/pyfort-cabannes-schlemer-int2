import json
from toolbox import uppercase
from random import randint,choice
def treasure_room():
    with open('data/TRClues.json') as f:
        data = json.load(f)
    year=str(randint(2015,2019))
    shows=list(data['Fort Boyard'][year].keys())
    show=choice(shows)
    chosen=data['Fort Boyard'][year][show]
    for i in range(1,4):
        print(f"Clue {i}:"+chosen['Clues'][i])
    j=3
    for i in range(4,7):
        guess=uppercase(str(input("What is your answer? ")))
        if guess==chosen['CODE-WORD']:
            print("Congratulations! You have found the codeword.")
            return True
        else:
            k=0
            j+=1
            while k<j:
                print(f"Clue {k}:"+chosen['Clues'][k])
                k+=1
    guess=uppercase(str(input("What is your answer? ")))
    if guess==chosen['CODE-WORD']:
        print("Congratulations! You have found the codeword.")
        return True
    else:
        print("You have failed to find the codeword.")
        return False

treasure_room()