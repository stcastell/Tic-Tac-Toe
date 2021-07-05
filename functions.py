# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:01:20 2021

@author: Santiago Castellanos
"""

import numpy as np
    
def create_board():
    board = np.zeros((3,3), dtype=int)
    return(board)
    
def place(board, player, position):
    if(board[position]==0):
        board[position] = player
            
def possibilities(board):
    available = []
    x = board == 0
    y = np.where(x)
    y0 = y[0]
    y1 = y[1]
    for i in range(len(y0)):
        available.append((y0[i], y1[i]))
    return(available)
    
def random_place(board, player):
    available = possibilities(board)
    available_index = list(range(len(available)))
    selection = np.random.choice(available_index)
        
    random_coordinate = available[selection]
        
    board[random_coordinate] = player
    return(board)
    
def row_win(board, player):
    row0 = board[0] == player
    row1 = board[1] == player
    row2 = board[2] == player
        
    if row0.all():
        return(True)
    elif row1.all():
        return(True)
    elif row2.all():
        return(True)
    else:
        return(False)
        
def col_win(board,player):
    column0 = board[:,0] == player
    column1 = board[:,1] == player
    column2 = board[:,2] == player
        
    if column0.all():
        return(True)
    elif column1.all():
        return(True)
    elif column2.all():
        return(True)
    else:
        return(False)
        
def diag_win(board,player):
    diag0 = board.diagonal() == player
    diag1 = np.fliplr(board).diagonal() == player
        
    if diag0.all():
        return(True)
    elif diag1.all():
        return(True)
    else:
        return(False)
        
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if(row_win(board, player) == True):
            winner = f"Player {player} wins by a row."
                
        elif(col_win(board, player) == True):
            winner = f"Player {player} wins by a column."
                
        elif(diag_win(board, player) == True):
            winner = f"Player {player} wins by a diagonal."
        else:
            pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

