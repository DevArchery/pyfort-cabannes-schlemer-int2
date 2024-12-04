
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



board = [[0 for _ in range(3)] for _ in range(3)] # 3x3 grid

def display_empty_grid():
    for i in range(3):
        if i <= 2:
            print("  ","|","  ", "|", end=" ")
            print()
            if i <= 1:
                print("------------", end=" ")
                print()

def check_winner():
    for raw in board:
        if raw[0] == raw[1] == raw[2] == "O" or raw[0] == raw[1] == raw[2] == "X":
            return True
    for col in board:
        if col[0] == col[1] == col[2] != "O" or col[0] == col[1] == col[2] != "X":
            return True
    for diag in board:
        if diag[0] == diag[1] == diag[2] != "O" or diag[0] == diag[1] == diag[2] != "X":
            return True

def full_grid():
    for row in board:
        if 0 in row:
            return False
        else:
            return True


def player_turn():
    player = "X"
    while True:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if board[row][col] == 0:
            board[row][col] = player
            break
        else:
            print("This cell is already taken. Please choose another one.")
    display_grid()
    check_result()
    return board

def display_grid():
    for i in range(3):
        for j in range(3):
            if j == 2:
                if board[i][j] == 0:
                    print("  ", end=" ")
                else:
                    print(board[i][j], end=" ")
            elif j == 1:
                if board[i][j] == 0:
                    print(" ","|", end=" ")
                else:
                    print(board[i][j], "|", end=" ")
            else :
                if board[i][j] == 0:
                    print("  ","|", end=" ")
                else:
                    print("",board[i][j], "|", end=" ")
        print()
        if i <= 1:
            print("------------", end=" ")
            print()

player_turn()

def check_result():
    if check_winner():
        return True
    elif full_grid():
        return True
    else:
        return False

display_empty_grid()

def master_turn():
    move = master_move(board)
    board[move[0]][move[1]] = "X"
    display_grid()
    check_result()
    return board

def tic_tac_toe():
    while True:
        player_turn()
        if check_result():
            break
        master_turn()
        if check_result():
            break