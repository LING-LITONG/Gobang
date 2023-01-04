"""
Tic Tac Toe Player
"""

import math
import copy

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
    X_num = 0
    O_num = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                X_num += 1
            if board[i][j] == 'O':
                O_num += 1
    if X_num-O_num == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    fill = player(board)
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception("infeasible move")
    new_board[i][j] = fill
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for flag in [X, O]:
        for i in range(3):
            if board[i][0] == flag and board[i][1] == flag and board[i][2] == flag:
                return flag
            if board[0][i] == flag and board[1][i] == flag and board[2][i] == flag:
                return flag
        if board[0][0] == flag and board[1][1] == flag and board[2][2] == flag:
            return flag
        if board[0][2] == flag and board[1][1] == flag and board[2][0] == flag:
            return flag 
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Value = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Value = False
    if winner(board) or Value:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    if player(board) == O:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return utility(board), ()
    v = -10
    for action in actions(board):
        minval = min_value(result(board, action))[0]
        if v < minval:
            v = minval
            res = action
    return v, res


def min_value(board):
    if terminal(board):
        return utility(board), ()
    v = 10
    for action in actions(board):
        maxval = max_value(result(board, action))[0]
        if v > maxval:
            v = maxval
            res = action
    return v, res
        
    
