import random as rnd
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

grid = grid()
grid.start()