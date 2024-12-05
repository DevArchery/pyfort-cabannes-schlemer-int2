import random as rnd
from time import sleep
from toolbox import remove_value
class Battleships:
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([" "] * 3)
        self.ships = []
    def display(self):
        for row in self.board:
            print(" | {} | {} | {} |".format(row[0], row[1], row[2]))
        print(" -------------")
    def place(self, x, y):
        try:
            if (x, y) in self.ships:
                print("There is already a ship here.")
                self.place(int(input("Enter an x: ")), int(input("Enter a y: ")))
            else:
                self.board[x][y] = "B"
                self.ships.append((x, y))
        except IndexError:
            print("Please enter a valid coordinate.")
            self.place(int(input("Enter an x: ")), int(input("Enter a y: ")))
    def boat_master(self):
        x = rnd.randint(0, 2)
        y = rnd.randint(0, 2)
        if (x, y) in self.ships:
            self.boat_master()
        else:
            self.place(x, y)
            self.ships.append((x, y))
    def player_shoot(self,opponent,x,y):
        try:
            if (x,y) in opponent.ships:
                print("Hit!")
                opponent.ships = remove_value(opponent.ships, (x, y))
                opponent.board[x][y]="X"
            else:
                if opponent.board[x][y]==".":
                    print("You have already hit this location.")
                    self.player_shoot(opponent,int(input("Enter an x: ")),int(input("Enter a y: ")))
                else:
                    print("Miss!")
                    opponent.board[x][y]="."
        except IndexError:
            self.player_shoot(opponent, int(input("Enter an x: ")), int(input("Enter a y: ")))
        except ValueError:
            self.player_shoot(opponent, int(input("Enter an x: ")), int(input("Enter a y: ")))

    def master_shoot(self, opponent):
        x = rnd.randint(0, 2)
        y = rnd.randint(0, 2)
        if opponent.board[x][y] == "X" or opponent.board[x][y] == ".":
            print("You have already hit this location.")
            self.master_shoot(opponent)
        else:
            if (x, y) in opponent.ships:
                print("Hit!")
                opponent.ships = remove_value(opponent.ships, (x, y))
                opponent.board[x][y] = "X"
            else:
                print("Miss!")
                opponent.board[x][y] = "."
def battleship_game():
    turn = 1
    player, master = Battleships(), Battleships()
    master.boat_master()
    master.boat_master()
    print("Place your boats")
    player.place(int(input("Enter an x: ")), int(input("Enter a y: ")))
    player.display()
    player.place(int(input("Enter an x: ")), int(input("Enter a y: ")))
    while True:
        if turn%2==1:
            print("Your boats")
            player.display()
            print("It's your turn to play")
            player.player_shoot(master,int(input("Enter an x: ")),int(input("Enter a y: ")))
            sleep(3)
            if len(master.ships)==0:
                print("You have won!")
                return True
        else:
            print("It's the master's turn to play")
            master.master_shoot(player)
            sleep(3)
            if len(player.ships)==0:
                print("The master has won!")
                return False
        turn+=1