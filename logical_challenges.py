
global sticks
def display_sticks(sticks):
    for i in range(sticks):
        print("|", end="")
    print()
def player_removal(sticks, player):
    print("Player", player, "how many sticks do you want to remove? (1, 2 or 3)")
    removed=int(input())
    while removed not in [1,2,3]:
        print("Please enter a valid number of sticks to remove (1, 2 or 3)")
        removed=int(input())
    sticks-=removed
    return sticks

def master_removal(sticks):
    removed=sticks%4
    if removed==0:
        removed=1
    print("The master removed", removed, "sticks")
    sticks-=removed
    return sticks

def nim_game():
    sticks=20
    player=1
    while sticks>0:
        print("There are", sticks, "sticks left")
        display_sticks(sticks)
        sticks=player_removal(sticks, player)
        sticks=master_removal(sticks)
    print("Player", player, "lost!")

#nim_game()

