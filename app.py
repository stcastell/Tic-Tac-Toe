from extensions.functions import *


def play_game():
    player = 1
    board = create_board()
    while True:
        board = random_place(board, player)
        if row_win(board, player) == True or col_win(board, player) == True or diag_win(board, player) == True:
            print(board)
            print(evaluate(board))
            break
        else:
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
play_game()

                

        
