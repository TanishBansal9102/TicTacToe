board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]] 



def print_board_state(board):
    # this functions takes the board as an argument and prints it on the console
    print("\n#########################\n")
    for row in board:
        print(row[0],row[1],row[2])
    print("\n#########################\n")


def winner(board):
    # this functions takes the board as an argument and returns a string 
    # "X" - if X wins 
    # "O" - if O wins 
    # "tie" - if game is a tie 
    # "continue" - if the game has still not ended

    #horizontal win
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return "X"
            if board[i][0] == "O":
                return "O"

    #vertical win
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return "X"
            if board[0][i] == "O":
                return "O"

    #diagonal win 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == "X":
                return "X"
            if board[0][0] == "O":
                return "O"

    #diagonal win 2
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            if board[2][0] == "X":
                return "X"
            if board[2][0] == "O":
                return "O"

    #continue 
    for row in board:
        for cell in row:
            if cell == "-":
                return "continue"

    #tie
    return "tie"



dummy_board = [
    ["X","O","X"],
    ["O","X","O"],
    ["O","X","O"]] 

print(winner(dummy_board))




