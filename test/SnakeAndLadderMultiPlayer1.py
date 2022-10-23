import math
import random
from colorama import Fore

def Move(position, move, maxvalue):
    position = position + move
    if position>maxvalue:
        position = position - move
        print(Fore.RED+"Sorry, Cant Move")
    return position

def SnakeAndLadderCreation(boardsize):
    y = math.ceil(boardsize/10)
    choice = [i for i in range(3, boardsize-1)]
    snake = [0 for i in range(2*y)]
    ladder = [0 for i in range(2*y)]
    gistsnake = ""
    gistladder = ""
    for i in range(0, 2*y, 2):
        snake[i] = random.choice(choice)
        choice.remove(snake[i])
        snake[i+1] = random.choice([i for i in range(2, snake[i])])
        gistsnake = gistsnake+str(snake[i])+"->"+str(snake[i+1])+", "
    for i in range(0, 2*y, 2):
        ladder[i] = random.choice(choice)
        choice.remove(ladder[i])
        ladder[i+1] = random.choice([i for i in range(ladder[i]+1, boardsize)])
        gistladder = gistladder+str(ladder[i])+"->"+str(ladder[i+1])+", "        
    return {"snake":snake, "ladder":ladder, "gistsnake":gistsnake, "gistladder":gistladder}

def SnakeAndLadderCheck(snake, ladder, position):
    for i in range(0, len(snake), 2):
        if position == snake[i]:
            print(Fore.RED+"SNAKE Found at "+str(snake[i])+"! Downgradation to " + str(snake[i+1]), end="")
            input(Fore.WHITE+"Enter to make the move")
            position = snake[i+1]
        if position == ladder[i]:
            print(Fore.GREEN+"LADDER Found at "+str(ladder[i])+"! Upgradation to " + str(ladder[i+1]), end="")
            input(Fore.WHITE+"Enter to make the move")
            position = ladder[i+1]
    return position
    
def BoardCreation(row, col, position, snake, ladder):
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
            if board[i][j]==position:
                print(Fore.CYAN+("%02d"%board[i][j]), end="  ")
            elif board[i][j] in [snake[i] for i in range(0, len(snake), 2)]:
                print(Fore.RED+("%02d"%board[i][j]), end="  ")
            elif board[i][j] in [ladder[i] for i in range(0, len(ladder), 2)]:
                print(Fore.GREEN+("%02d"%board[i][j]), end="  ")
            else:
                print(Fore.BLACK+("%02d"%board[i][j]), end="  ")
        print()
        
def MakingTheMove(i, position, boardrow, boardcol, snakeandladder):
    print("\n\n"+Fore.WHITE+"PLAYER", i+1, end = "")
    input(Fore.WHITE+"Enter To Roll The Dice")
    move = random.randint(1,6)
    print(Fore.WHITE+"Dice Gave:", move, end = "")
    input(Fore.WHITE+"Enter to Move")
    position = Move(position, move, boardrow*boardcol)
    BoardCreation(boardrow, boardcol, position, snakeandladder["snake"], snakeandladder["ladder"])
    print(Fore.WHITE+"Snake:", snakeandladder["gistsnake"], "\nLadder:", snakeandladder["gistladder"])
    newposition = SnakeAndLadderCheck(snakeandladder["snake"], snakeandladder["ladder"], position)
    if position != newposition:
        position = newposition
        BoardCreation(boardrow, boardcol, position, snakeandladder["snake"], snakeandladder["ladder"])
        print(Fore.WHITE+"Snake:", snakeandladder["gistsnake"], "\nLadder:", snakeandladder["gistladder"])
    if position == boardrow*boardcol:
        print(Fore.MAGENTA+"\nCONGRATULATIONS PLAYER "+str(i+1)+"!! YOU WON.")
        return -1
    return position
    

def Initiasation(players, boardrow, boardcol):
    print(Fore.WHITE+"-------------------------------------")
    position = [0 for i in range(players)]
    snakeandladder = SnakeAndLadderCreation(boardrow*boardcol)
    print("Total Players:", players)
    print("Initial position of all the players:", 0)
    print(Fore.WHITE+"\nBoard size:", boardrow*boardcol)
    BoardCreation(boardrow, boardcol, 0, snakeandladder["snake"], snakeandladder["ladder"])
    print(Fore.WHITE+"Snake: ", snakeandladder["gistsnake"], "\nLadder: ", snakeandladder["gistladder"])
    print(Fore.WHITE+"\nRed->Snake \nGreen->Ladder \nBlue->Player Position")
    print(Fore.WHITE+"------------------------------------\n")
    while True:
        for i in range(len(position)):
            position[i] = MakingTheMove(i, position[i], boardrow, boardcol, snakeandladder)
            if position[i] == -1:
                return
    
    


players = 3
board_row = 5
board_col = 5
Initiasation(players, board_row, board_col)




    

    
        
    








    
    