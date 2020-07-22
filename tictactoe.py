#Initializing empty board 
board = [
    ["-","-","-"], 
    ["-","-","-"],
    ["-","-","-"]] 

#Values of different ending positions which will help in determining value 
#of nodes of the decision tree

value_dict = {
    "X": 1,
    "tie": 0,
    "O": -1
}

def print_board_state(board):
    # this functions takes the board as an argument and prints it on the console
    print("\n#########################\n")
    for row in board:
        print(row[0],row[1],row[2])
    print("\n#########################\n")


def winner(board):
    # Arguments :-
    # board - a nested list which is the current snapshot of the board

    #returns :=
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


def minimax(board, is_this_AIs_turn): 
    #Arguments :-
    #board - a nested list which is the current snapshot of the board
    #is_this_AIs_turn - a boolean which is true if AI is the current Player

    #returns :-
    #the value of the current node 

    winner_player = winner(board)

    #if we reached the end of the tree
    if winner_player != "continue":
        return value_dict[winner_player]
    
    #if this is AIs turn i.e the maximizing players turn
    if is_this_AIs_turn:
        score = - 2               #anything smaller than min score
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    curr_score = minimax(board,False)
                    board[i][j] = "-"
                    score = max(score, curr_score)
        return score
    else:
        score =  2               #anything bigger than max score
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    curr_score = minimax(board,True)
                    board[i][j] = "-"
                    score = min(score, curr_score)
        return score

                

def ais_move(board):
    #Arguments :-
    #board - a nested list which is the current snapshot of the board

    #returns :-
    #an array with 2 items representing the best move for AI in the current position

    score = - 2               #anything smaller than min score
    x = -1                    #the row no. of cell which AI chosses for best move
    y = -1                    #the column no. of cell which AI chosses for best move
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                board[i][j] = "X"
                curr_score = minimax(board,False)
                board[i][j] = "-"
                if curr_score > score:
                    score = curr_score
                    x = i 
                    y = j
    return [x, y]

dummy_board = [
    ["X","O","-"], 
    ["X","O","O"],
    ["-","X","-"]]

print(ais_move(dummy_board)[0],ais_move(dummy_board)[1])

