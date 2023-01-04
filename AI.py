X = "X"
O = "O"
EMPTY = None


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

    >>> terminal([[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]])
    False
    """
    Value = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Value = False
    if winner(board) or Value:
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()