import random as rnd
from time import sleep
from toolbox import remove_value
global sticks


def display_sticks(sticks):
    for i in range(sticks):
        print("|", end="")

    print()


def player_removal(sticks, player):
    print("Player", player, "how many sticks do you want to remove? (1, 2 or 3)")

    removed = int(input())

    while removed not in [1, 2, 3]:
        print("Please enter a valid number of sticks to remove (1, 2 or 3)")

        removed = int(input())

    sticks -= removed

    return sticks



def master_removal(sticks):
    removed = sticks % 4

    if removed == 0:
        removed = 1

    print("The master removed", removed, "sticks")

    sticks -= removed

    return sticks


def nim_game():
    sticks = 20

    player = 1

    while sticks > 0:
        print("There are", sticks, "sticks left")

        display_sticks(sticks)

        sticks = player_removal(sticks, player)

        sticks = master_removal(sticks)

    print("Player", player, "lost!")


class grid():
    def __init__(self):
        self.board = [["" for i in range(3)] for j in range(3)]
        self.turn = 0
        self.state = False

    def display_grid(self):
        for i in range(3):
            for j in range(3):
                if j == 2:
                    if self.board[i][j] == "":
                        print("  ", end=" ")
                    else:
                        print(self.board[i][j], end=" ")
                elif j == 1:
                    if self.board[i][j] == "":
                        print(" ","|", end=" ")
                    else:
                        print(self.board[i][j], "|", end=" ")
                else:
                    if self.board[i][j] == "":
                        print("  ","|", end=" ")
                    else:
                        print("",self.board[i][j], "|", end=" ")
            print()
            if i <= 1:
                print("------------", end=" ")
                print()

    def player_turn(self):
        try:
            x = int(input("Enter the x coordinate: "))
            y = int(input("Enter the y coordinate: "))
            if self.board[x][y] == "":
                self.board[x][y] = "X"
                self.display_grid()
            else:
                raise ValueError
        except ValueError:
            print("This cell is already taken. Please choose another one.")
            self.player_turn()
        except IndexError:
            print("Please enter a valid coordinate.")
            self.player_turn()

    def master_turn(self, i, j):
        self.board[i][j] = "O"
        self.display_grid()

    def check_state(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "" or self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.state = True
        i = 0
        if self.board[i][i] == self.board[i+1][i+1] == self.board[i+2][i+2] != "" or self.board[i][i+2] == self.board[i+1][i+1] == self.board[i+2][i] != "":
            self.state = True

    def optimal_move(self):
        if self.can_win("O"):
            return self.can_win("O")
        if self.can_win("X"):
            return self.can_win("X")
        i,j=rnd.randint(0,2),rnd.randint(0,2)
        if self.board[i][j] == "":
            return (i, j)
        else:
            return self.optimal_move()


    def can_win(self, char):
        # Check rows for a winning move
        for i in range(3):
            if self.board[i].count(char) == 2 and self.board[i].count("") == 1:
                return (i, self.board[i].index(""))

        # Check columns for a winning move
        for j in range(3):
            col = [self.board[i][j] for i in range(3)]
            if col.count(char) == 2 and col.count("") == 1:
                return (col.index(""), j)

        # Check diagonals for a winning move
        diag1 = [self.board[i][i] for i in range(3)]
        if diag1.count(char) == 2 and diag1.count("") == 1:
            return (diag1.index(""), diag1.index(""))

        diag2 = [self.board[i][2-i] for i in range(3)]
        if diag2.count(char) == 2 and diag2.count("") == 1:
            return (diag2.index(""), 2-diag2.index(""))

        return None

    def start(self):
        while self.turn <= 9:
            self.player_turn()
            self.check_state()
            if self.state:
                print("Player wins!")
                break
            self.turn += 1
            if self.turn == 9:
                print("It's a tie!")
                break
            i, j = self.optimal_move()
            self.master_turn(i, j)
            self.check_state()
            if self.state:
                print("Master wins!")
                break
            self.turn += 1
            if self.turn == 9:
                print("It's a tie!")
                break

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
def logical_challenges():
    challenges=["Nim","Tic-Tac-Toe","Battleships"]
    chosen=rnd.choice(challenges)
    if chosen=="Nim":
        nim_game()
    elif chosen=="Tic-Tac-Toe":
        tictactoe=grid()
        tictactoe.start()
    else:
        battleship_game()