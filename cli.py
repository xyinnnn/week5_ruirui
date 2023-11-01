# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import other_player
from logic import get_winner
from logic import input_move
from logic import show_board
from logic import check_game_end


# Reminder to check all the tests
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = 'X'
    while winner == None:
        print("Next turn: ", turn)
        input_move(board, turn)
        show_board(board)
        turn = other_player(turn)
        winner = get_winner(board)
        if check_game_end(board):
            print("Game ends. No winner.")
            break
