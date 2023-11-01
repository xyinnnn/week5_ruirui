# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def show_board(input_board):
    for row in input_board:
        print(row)

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    return 'X'

def get_winner(input_board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    winner = None
    for i in range(0, 3):
        if input_board[i][0] != None and input_board[i][0] == input_board[i][1] and input_board[i][1] == input_board[i][2]:
            winner = input_board[i][0]
            print(winner, ' won.')
            return winner

        if input_board[0][i] != None and input_board[0][i] == input_board[1][i] and input_board[1][i] == input_board[2][i]:
            winner = input_board[0][i]
            print(winner, ' won.')
            return winner

    if (input_board[0][0] == input_board[1][1] and input_board[1][1] == input_board[2][2]) or (input_board[0][2] == input_board[1][1] and input_board[1][1] == input_board[2][0]):
        winner = input_board[1][1]

    if winner != None:
        print(winner, ' won.')

    return winner


def input_move(input_board, turn):
    try:
        row = int(input("Input row index: "))
        column = int(input("Input col index: "))
    except:
        raise ValueError('Input invalid, must be an int.')
    else:
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise ValueError('Input invalid, should >=0 and <=2.')
        if input_board[row][column] != None:
            raise ValueError('Input invalid, the place already has input.')
        input_board[row][column] = turn 


        
def check_game_end(input_board):
    for i in range(0, 3):
        for j in range(0, 3):
            if input_board[i][j] == None:
                return False
    return True
