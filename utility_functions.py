from toolbox import uppercase
from math_challenges import math_challenges
from chance_challenges import chance_challenges
from logical_challenges import logical_challenges
from pere_fouras_challenge import pere_fouras_riddles
def introduction():
    """Print the introduction of the game"""
    print("Welcome to PyFort!")
    print("To unlock the treasure room, you will need 3 keys")
    print("Your team will need to complete challenges to obtain these keys")

def compose_team()->list:
    """Prompts the user to enter the number of team members (between 1 and 3),
    and for each member, their name, profession, and whether they are the leader.
    Ensures there is exactly one leader in the team."""
    try:
        n=int(input("Enter the number of team members: "))
        assert 3 >= n >= 1
        team = []
        for i in range(n):
            name = input("Enter the name of the team member: ")
            profession=input("Enter the profession of the team member: ")
            leader= input("Is this team member the leader? (y/n): ")
            team.append({"Name":uppercase(name),"Profession":profession,"Leader":leader})
        check=0
        for player in team:
            if player["Leader"]=="y":
                check+=1
        if check>1:
            print("There should be exactly one leader in the team")
            return compose_team()
        elif check==0:
            team[0]["Leader"]="y"
        return team
    except ValueError:
        print("Please enter a valid number")
        return compose_team()
    except TypeError:
        raise ValueError
    except AssertionError:
        raise ValueError
def choose_player(team):
    print("Select a player to attempt the challenge:")
    for i, player in enumerate(team):
        print(f"{i+1}. {player['Name']} ({player['Profession']}) - Leader ({player['Leader']})")
    try:
        choice=int(input("Enter the number of the player: "))
        assert len(team) >= choice >= 1
        return team[choice-1]
    except ValueError:
        print("Please enter a valid number")
        return choose_player(team)
    except TypeError:
        print("Please enter a valid number")
        return choose_player(team)
    except AssertionError:
        print("Please enter a valid number")
        return choose_player(team)
def challenge_menu():
    """Print the menu of challenges and prompt the user to select a challenge"""
    print("Select a challenge to attempt:")
    print("1. Math Challenges")
    print("2. Chance Challenges")
    print("3. Logical Challenges")
    print("4. Père Fouras Riddle")
    try:
        choice=int(input("Enter 1, 2, 3 or 4: "))
        assert 4 >= choice >= 1
        challenges=[math_challenges, chance_challenges, logical_challenges, pere_fouras_riddles]
        return challenges[choice-1]()
    except ValueError:
        print("Please enter a valid number")
        return challenge_menu()
    except TypeError:
        print("Please enter a valid number")
        return challenge_menu()
    except AssertionError:
        print("Please enter a valid number")
        return challenge_menu()

def record_history( player:dict, challenge:str, result:bool,keys:int):
    """Record the history of the game in a text file"""
    with open("history.txt","a") as file:
        file.write(f"{player['Name']} ({player['Profession']}) attempted the {challenge} and {'succeeded' if result else 'failed'},\nbringing the total number of keys to {keys}\n")
