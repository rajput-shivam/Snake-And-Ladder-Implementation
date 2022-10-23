import math
import random
from colorama import Fore

def BoardCreation(p, positions, row, col, snake, ladder):
    board = [[0 for j in range(col)] for i in range(row)]
    counter, i, j = 0, row, 0
    while i>-1:
        i = i - 1
        while j<col and i>-1:
            counter = counter + 1
            board[i][j] = counter
            j = j + 1
        i = i - 1
        while j>0 and i>-1:
            j = j - 1
            counter = counter + 1
            board[i][j] = counter
    for i in range(row):
        for j in range(col):
            if board[i][j] in positions:
                counter = ""
                for k in range(len(positions)):
                    if board[i][j] == positions[k]:
                        counter = counter + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[k]
                print(Fore.CYAN+("%02d"%board[i][j])+counter, end="  ")
            elif board[i][j] in [snake[i] for i in range(0, len(snake), 2)]:
                print(Fore.RED+("%02d"%board[i][j]), end="  ")
            elif board[i][j] in [ladder[i] for i in range(0, len(ladder), 2)]:
                print(Fore.GREEN+("%02d"%board[i][j]), end="  ")
            else:
                print(Fore.BLACK+("%02d"%board[i][j]), end="  ")
        print()
        
BoardCreation(1, )
        
