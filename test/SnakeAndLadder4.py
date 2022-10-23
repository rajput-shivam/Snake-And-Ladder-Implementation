import random
from colorama import Fore



def Dice():
    return random.choice([1,2,3,4,5,6])
    
def Move(position, move, maxvalue):
    position = position + move
    if position>maxvalue:
        position = position - move
        print(Fore.RED+"Sorry, Cant Move")
    return position
        
def SnakeAndLadder(position):
    if position == 13:
        print(Fore.RED+"SNAKE Found! Downgradation to 2")
        position = 2
        BoardCreation(boardrow, boardcol, position)
    if position == 4:
        print(Fore.GREEN+"LADDER Found! Downgradation to 11")
        position = 11
        BoardCreation(boardrow, boardcol, position)
    return position

def BoardCreation(row, col, position):
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
            if position==board[i][j]:
                print(Fore.BLUE+("%02d"%board[i][j]), end="  ")
            else:
                print(Fore.WHITE+("%02d"%board[i][j]), end="  ")
        print()
 

           
position = 0
boardrow, boardcol = 2, 6
print("\nSnake on 13 downgrades to 2")
print("Ladder on 4 upgrades to 11")
print("Initial Board", end="\n")
BoardCreation(boardrow, boardcol, position)


while True:
    input(Fore.WHITE+"\nEnter To Roll The Dice")
    move = Dice()
    print(Fore.WHITE+"Dice Gave:", move, end = "")
    input(Fore.WHITE+"Enter to Move")
    position = Move(position, move, boardrow*boardcol)
    BoardCreation(boardrow, boardcol, position)
    position = SnakeAndLadder(position)
    if position == boardrow*boardcol:
        print(Fore.MAGENTA+"\nCONGRATULATIONS!! YOU WON.")
        break





    

    
        
    








    
    