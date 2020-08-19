"""
Tic Tac Toe Player
NAME: Adrian Patterson
EMAIL: patterson.n.adrian@gmail.com
GITHUB: canadrian72

NOTES/REMARKS FOR MARKER:
- When game is a tie, an infinite loop is encountered. I'm not sure where this error comes from. Any feedback is greatly appreciated!
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if all(x is None for x in board):       # If all are None, it is X's first move
        return X

    o_count = 0
    x_count = 0

    for row in range(3):                   # Loop to count total number of x and o's
        for column in range(3):
            if board[row][column] == O:
                o_count+=1
            if board[row][column] == X:
                x_count+=1
            else:
                continue

    if o_count == x_count:              # decides on who's turn it is based on summation of x and o's
        return X
    if x_count > o_count:
        return O                           




def actions(board):     
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []

    for row in range(3):            # Loops iterate to find null cells in matrix
        for column in range(3):
            if board[row][column] == None:
                action = (str(row),str(column))
                action_list.append(action)
    
    return action_list



def result(board, action):          # Simply copies board, and tries to insert action
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updated_board = copy.deepcopy(board)

    try:
        updated_board[int(action[0])][int(action[1])] = player(board)
    except IndexError as error:
        print(error)
    
    return updated_board



def winner(board):          # Checks for a win
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):          # Checking all rows for a win
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    for i in range(3):          # Checking all columns for a win
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:        # Checking diagonals for a win
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O

    if board[2][0] == X and board[1][1] == X and board[0][2] == X:       
        return X
    if board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):       # uses winner function to see if board is terminal
        return True
    
    for row in range(3):                   
        for column in range(3):
            if board[row][column] == None:
                return False
    
    else:
        return False

    


def utility(board):     # returns utility values
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0



def minimax(board):         # implementation of minimax algorithm
        if board == initial_state():        # IF it is the computers first turn, then its first move is arbitrarily random
            return random.randint(0,2), random.randint(0,2)
        if player(board) == X:
            score = -math.inf
        if player(board) == O:
            score = math.inf
        best_action = ""

        for action in actions(board):           # iterates through all actions on current board
            board = result(board, action)       # does action
            board_score = best_score(board)     # computes score for this action   
            board[int(action[0])][int(action[1])] = None    # restores cell on tic tac toe board
            if board_score > score and player(board) == X:             # compares current score as better or worse than last
                score = board_score
                best_action = action
            elif board_score < score and player(board) == O:
                score = board_score
                best_action = action
        
        return best_action
    
    


def best_score(board):         # function to return score
    if terminal(board):
        return utility(board)
    scores = []
    for action in actions(board):               
        board = result(board,action)
        scores.append(best_score(board))
        board[int(action[0])][int(action[1])] = None
    if player(board) == X:
        return max(iter(scores) if scores else [0])         # Returns maximum score of list if we are playing with maximizer
    if player(board) == O:
        return min(iter(scores) if scores else [0])         # Returns minimum score of list if we are playing with minimizer