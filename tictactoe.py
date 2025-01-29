"""
Tic Tac Toe Player
"""

import copy
import math

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
    # Is the board in its initial state?
    if board == initial_state():
        return X

    # Count the number of Xs and Os
    x_cnt = 0
    o_cnt = 0

    for i in range(3):
        for j in range(3):
            # Increment X or O in a branchless manner
            x_cnt += int(board[i][j] == X)
            o_cnt += int(board[i][j] == O)

    # Is it O's turn?
    if x_cnt > o_cnt:
        return O

    # Is it X's turn?
    elif x_cnt == o_cnt:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Find all empty squares and return them
    actions = set()

    for i in range(3):
        for j in range(3):
            # Add the square to the actions available if it is empty
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Do bounds checking on action
    if (action[0] < 0 or action[0] > 2 or
            action[1] < 0 or action[1] > 2):
        raise Exception

    # Check if the given action is valid for the given game board
    i, j = action

    if board[i][j] != EMPTY:
        raise Exception

    # Calculate the resulting game board
    result = copy.deepcopy(board)
    result[i][j] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for three in a row horizontally
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

    # Check for three in a row vertically
    for j in range(3):
        if board[0][j] != EMPTY and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return board[0][j]

    # Check for three in a row diagonally
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (winner(board) is not None or not len(actions(board)))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Calculate utility in a branchless manner
    winning_player = winner(board)
    return int(winning_player == X) - int(winning_player == O)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return optimal_action(board)[0]


def optimal_action(board):
    """
    Returns the optimal action and its utility for the current player on the
    board.
    """
    # Is the game over?
    if terminal(board):
        return (None, utility(board))

    # Enumerate all possible actions and their utility
    current_player = player(board)
    possible_actions = [(action, optimal_action(result(board, action))[1]) 
                        for action in actions(board)]

    # Return most optimal action for current player
    if current_player == X:
        return max(possible_actions, key=lambda x: x[1])

    else:
        return min(possible_actions, key=lambda x: x[1])
