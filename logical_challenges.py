import random as rnd
from time import sleep
from toolbox import remove_value

#Creation of an exception used to switch to the GUI version of tictactoe
class GUIVersion(Exception):
    pass

# Nim game
#make the sticks variable global so that it can be accessed by the functions used in the Nim game
global sticks

def display_sticks(sticks):
    """Display the sticks left"""
    for i in range(sticks):
        print("|", end="")

    print()


def player_removal(sticks):
    """Asks the users how many sticks does he want to remove and if it is either 1,2 or 3, """
    try:
        print("How many sticks do you want to remove? (1, 2 or 3)")

        removed = int(input())

        if removed not in [1, 2, 3]:
            raise ValueError

        sticks -= removed

        return sticks
    except ValueError:
        print("Please enter a valid number of sticks.")
        return player_removal(sticks)
    except TypeError:
        raise ValueError


def master_removal(sticks):
    """The master haas a 10% chance to remove a random number of sticks, otherwise it will remove the number of sticks left modulo 4"""
    if sticks==1:
        removed=1
    elif rnd.random() <= 0.1:
        removed = rnd.randint(1, 3)
    else:
        removed = sticks % 4

        if removed == 0:
            removed = 1

    print("The master removed", removed, "sticks")

    sticks -= removed

    return sticks


def nim_game():
    """Starts the Nim game and explains the rules"""
    print("Welcome to the Nim game!")
    print("The goal is to remove the last stick.")
    print("You can remove 1, 2 or 3 sticks at a time.")
    print("Since you will start, the master will always")
    print("win as there exists an algorithm to always win when playing in second.")
    print("To avoid that, the master has a chance to remove a random number of sticks.")
    print("Let's start!")

    sticks = 20

    player = 1

    while sticks > 0:
        print("There are", sticks, "sticks left")
        display_sticks(sticks)
        sticks = player_removal(sticks)
        if sticks == 1:
            print("You won!")
            return True
        sticks = master_removal(sticks)
    print("You lost!")
    return False
#Creation of the grid class used for the Tic-Tac-Toe game
class grid():
    def __init__(self):
        """Initializes the board as a 3x3 matrix, the turn and the state of the game"""
        self.board = [["" for i in range(3)] for j in range(3)]
        self.turn = 0
        self.state = False

    def display_grid(self):
        """Displays the grid"""
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
        """Asks the player for the coordinates of the cell he wants to fill, in case the cell is already taken, it will ask for another one by
        raising a ValueError"""
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
        """Places an O in the cell (i,j)"""
        self.board[i][j] = "O"
        self.display_grid()

    def check_state(self):
        """Checks if the game is over by checking the rows, columns and diagonals"""
        #  lines and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "" or self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.state = True
        # diagonals
        i = 0
        if self.board[i][i] == self.board[i+1][i+1] == self.board[i+2][i+2] != "" or self.board[i][i+2] == self.board[i+1][i+1] == self.board[i+2][i] != "":
            self.state = True

    def optimal_move(self):
        """Returns the optimal move for the master to play, if it can win, it will play the winning move, if it can't win but it can
        block the player from winning, it will play that move,otherwise it will play a random move"""
        if self.can_win("O"): #if the master can win
            return self.can_win("O")
        if self.can_win("X"): #if the master can block the player from winning
            return self.can_win("X")
        i,j=rnd.randint(0,2),rnd.randint(0,2)
        if self.board[i][j] == "":
            return (i, j)
        else:
            return self.optimal_move()#if the cell is already taken, it will try again, it is far from optimal it terms of complexity but it is a simple solution

    def can_win(self, char):
        """Checks if a character ("X" or "O") can win in the next move by checking the rows, columns and diagonals"""
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
        """Starts the game and explains the rules, then asks if the player wants to play the graphical version, in which
         case it will raise the GUIVersion exception defined earlier"""
        try:
            print("Welcome to Tic-Tac-Toe!")
            print("You will be playing against the master.")
            print("You will be X and the master will be O.")
            print("You can select a cell by entering the x and y coordinates.")
            print("If you want to try the graphical version, please enter 'GUI'")
            if input()=="GUI":
                raise GUIVersion
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
        except GUIVersion:
            import tkinter as tk
            import TTTGUI
            root = tk.Tk()
            game = TTTGUI.PyfortGame(root)
            root.mainloop()
            return True if game.state else False
#Creation of the Battleships class used for the Battleships game
class Battleships:
    def __init__(self):
        """Initializes the board as a 3x3 matrix, the history board as a 3x3 matrix, the ships location list"""
        self.board = []
        self.history = []
        for i in range(3):
            self.board.append([" "] * 3)
            self.history.append([" "] * 3)
        self.ships = []
    def display(self):
        """Displays the board and the history board"""
        for row in self.board:
            print(" | {} | {} | {} |".format(row[0], row[1], row[2]))
        print(" -------------")
        print('History board')
        for row in self.history:
            print(" | {} | {} | {} |".format(row[0], row[1], row[2]))
        print(" -------------")
    def place(self, x, y):
        """Places a ship in the cell (x,y) if it is empty, otherwise it will ask for another cell"""
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
        except ValueError:
            raise IndexError
    def boat_master(self):
        """Places a ship in a random cell, if the cell is already taken, it will try again"""
        x = rnd.randint(0, 2)
        y = rnd.randint(0, 2)
        if (x, y) in self.ships:
            self.boat_master()
        else:
            self.place(x, y)
            self.ships.append((x, y))
    def player_shoot(self,opponent,x,y):
        """The player shoots at the cell (x,y) of the opponent, if it is a hit, it will remove the ship from the opponent's ships list"""
        try:
            if (x,y) in opponent.ships:
                print("Hit!")
                opponent.ships = remove_value(opponent.ships, (x, y))
                opponent.board[x][y]="X"
                self.history[x][y]="X"
            else:
                if opponent.board[x][y]==".":
                    print("You have already hit this location.")
                    self.player_shoot(opponent,int(input("Enter an x: ")),int(input("Enter a y: ")))
                else:
                    print("Miss!")
                    opponent.board[x][y]="."
                    self.history[x][y]="."
        except IndexError:
            self.player_shoot(opponent, int(input("Enter an x: ")), int(input("Enter a y: ")))
        except ValueError:
            self.player_shoot(opponent, int(input("Enter an x: ")), int(input("Enter a y: ")))

    def master_shoot(self, opponent):
        """The master shoots at a random cell, if it is a hit, it will remove the ship from the opponent's ships list"""
        x = rnd.randint(0, 2)
        y = rnd.randint(0, 2)
        if opponent.board[x][y] == "X" or opponent.board[x][y] == ".":
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
    """Starts the Battleships game and explains the rules"""
    print("Welcome to Battleships!")
    print("You will be playing against the master.")
    print("The master will place its boats first.")
    print("You will then place your boats.")
    print("You will then take turns to shoot at each other's boats.")
    print("The first player to sink all of the opponent's boats wins.")
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
            x,y=int(input("Enter an x: ")),int(input("Enter a y: "))
            player.player_shoot(master,x,y)
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
    """Randomly selects a challenge from the list of challenges and starts it"""
    challenges=["Nim","Tic-Tac-Toe","Battleships"]
    chosen=rnd.choice(challenges)
    if chosen=="Nim":
        nim_game()
    elif chosen=="Tic-Tac-Toe":
        tictactoe=grid()
        tictactoe.start()
    else:
        battleship_game()

if __name__ == "__main__":
    tictactoe = grid()
    print(tictactoe.start())