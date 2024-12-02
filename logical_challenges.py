
global x
global n
n = 0

def display_sticks(x):
    for i in range(x):
        print("|", end="")

def player_removal(x):
    n = x
    try:
        nb = 5
        while nb > 3:
            print("How many sticks do you wanna remove ?")
            nb = int(input())
            n -= nb
        display_sticks(x)
    except ValueError:
        print("Please enter a valid number")
    except TypeError:
        print("Please enter a valid number")
    master_removal(n)
    return n

def master_removal(n):
    n=int(4-player_removal(x))
    for i in range(n):
        print("|", end="")

x = int(input("Enter the number of sticks : "))

display_sticks(x)
player_removal(x)


