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

    def minimax(self, board, depth, is_max):
        score = self.evaluate(board)
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if not self.is_moves_left(board):
            return 0

        if is_max:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        best = max(best, self.minimax(board, depth + 1, not is_max))
                        board[i][j] = ""
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        best = min(best, self.minimax(board, depth + 1, not is_max))
                        board[i][j] = ""
            return best

    def evaluate(self, board):
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return 10 if row[0] == "O" else -10
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return 10 if board[0][col] == "O" else -10
        if board[0][0] == board[1][1] == board[2][2] != "":
            return 10 if board[0][0] == "O" else -10
        if board[0][2] == board[1][1] == board[2][0] != "":
            return 10 if board[0][2] == "O" else -10
        return 0

    def is_moves_left(self, board):
        for row in board:
            if "" in row:
                return True
        return False

    def optimal_move(self):
        best_val = -1000
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    move_val = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

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