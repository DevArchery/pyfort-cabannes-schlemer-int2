import tkinter as tk
from tkinter import messagebox
import random as rnd
class PyfortGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pyfort Game")
        self.board = [[""] * 3 for _ in range(3)]
        self.turn = 0
        self.state = False
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", width=10, height=3, command=lambda i=i, j=j: self.player_turn(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def player_turn(self, i, j):
        if self.board[i][j] == "" and not self.state:
            self.board[i][j] = "X"
            self.buttons[i][j].config(text="X")
            self.check_state()
            if self.state:
                messagebox.showinfo("Game Over", "Player wins!")
                return
            self.turn += 1
            if self.turn == 9:
                messagebox.showinfo("Game Over", "It's a tie!")
                return
            self.master_turn()

    def master_turn(self):
        i, j = self.optimal_move()
        self.board[i][j] = "O"
        self.buttons[i][j].config(text="O")
        self.check_state()
        if self.state:
            messagebox.showinfo("Game Over", "Master wins!")
            return
        self.turn += 1
        if self.turn == 9:
            messagebox.showinfo("Game Over", "It's a tie!")

    def check_state(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "" or self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.state = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.state = True

    def optimal_move(self):
        if self.can_win("O"):
            return self.can_win("O")
        if self.can_win("X"):
            return self.can_win("X")
        i, j = rnd.randint(0, 2), rnd.randint(0, 2)
        if self.board[i][j] == "":
            return (i, j)
        else:
            return self.optimal_move()

    def can_win(self, char):
        for i in range(3):
            if self.board[i].count(char) == 2 and self.board[i].count("") == 1:
                return (i, self.board[i].index(""))
        for j in range(3):
            col = [self.board[i][j] for i in range(3)]
            if col.count(char) == 2 and col.count("") == 1:
                return (col.index(""), j)
        diag1 = [self.board[i][i] for i in range(3)]
        if diag1.count(char) == 2 and diag1.count("") == 1:
            return (diag1.index(""), diag1.index(""))
        diag2 = [self.board[i][2-i] for i in range(3)]
        if diag2.count(char) == 2 and diag2.count("") == 1:
            return (diag2.index(""), 2-diag2.index(""))
        return None

if __name__ == "__main__":
    root = tk.Tk()
    game = PyfortGame(root)
    root.mainloop()