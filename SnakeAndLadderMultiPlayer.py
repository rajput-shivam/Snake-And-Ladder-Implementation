import math
import random
from colorama import Fore

# returns random value between 1 and 6
def Dice():
    return random.randint(1,6)

# makes a forward move with accordance to the dice output
def Move(position, move, maxvalue):
    position = position + move
    if position>maxvalue:
        position = position - move
        print(Fore.RED+"Sorry, Cant Move")
    return position

# generate random snake and ladders depending upon the size of the board
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
        snake[i+1] = random.choice([i for i in range(2, snake[i]-1)])
        gistsnake = gistsnake+str(snake[i])+"->"+str(snake[i+1])+", "
    for i in range(0, 2*y, 2):
        ladder[i] = random.choice(choice)
        choice.remove(ladder[i])
        ladder[i+1] = random.choice([i for i in range(ladder[i]+2, boardsize)])
        gistladder = gistladder+str(ladder[i])+"->"+str(ladder[i+1])+", "        
    return {"snake":snake, "ladder":ladder, "gistsnake":gistsnake, "gistladder":gistladder}

# It checks the presence of a snake or a ladder, and returns the updated position
def SnakeAndLadderCheck(snake, ladder, position):
    oldposition = position
    for i in range(0, len(snake), 2):
        if position == snake[i]:
            print(Fore.RED+"SNAKE Found at "+str(snake[i])+"! Downgradation to " + str(snake[i+1]), end="")
            input(Fore.WHITE+"Enter to make the move")
            position = snake[i+1]
            continue
        if position == ladder[i]:
            print(Fore.GREEN+"LADDER Found at "+str(ladder[i])+"! Upgradation to " + str(ladder[i+1]), end="")
            input(Fore.WHITE+"Enter to make the move")
            position = ladder[i+1]
            continue
    if position != oldposition:
        SnakeAndLadderCheck(snake, ladder, position)
    return position
  
# It creates a board of any size and prints the board with details
def BoardCreation(positions, row, col, snake, ladder):
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
            counter = "  "
            if board[i][j] in positions:
                counter = ""
                for k in range(len(positions)):
                    if board[i][j] == positions[k]:
                        counter = counter+"p"+str(k+1)
            if board[i][j] in [snake[i] for i in range(0, len(snake), 2)]:
                print(Fore.RED+("%02d"%board[i][j])+Fore.CYAN+counter, end="   ")
            elif board[i][j] in [ladder[i] for i in range(0, len(ladder), 2)]:
                print(Fore.GREEN+("%02d"%board[i][j])+Fore.CYAN+counter, end="   ")
            else:
                print(Fore.BLACK+("%02d"%board[i][j])+Fore.CYAN+counter, end="   ")
        print()
 
# It rolls the dice, makes the move, checks the prescence of snake or ladder, makes furthur move if present, for a player  
def MakingTheMove(i, positions, boardrow, boardcol, snakeandladder):
    print("\n\n"+Fore.WHITE+"PLAYER", i+1, end = "")
    input(Fore.WHITE+"Enter To Roll The Dice")
    move = Dice()
    print(Fore.WHITE+"Dice Gave:", move, end = "")
    input(Fore.WHITE+"Enter to Move")
    positions[i] = Move(positions[i], move, boardrow*boardcol)
    BoardCreation(positions, boardrow, boardcol, snakeandladder["snake"], snakeandladder["ladder"])
    print(Fore.WHITE+"Snake:", snakeandladder["gistsnake"], "\nLadder:", snakeandladder["gistladder"])
    newposition = SnakeAndLadderCheck(snakeandladder["snake"], snakeandladder["ladder"], positions[i])
    if positions[i] != newposition:
        positions[i] = newposition
        BoardCreation(positions, boardrow, boardcol, snakeandladder["snake"], snakeandladder["ladder"])
        print(Fore.WHITE+"Snake:", snakeandladder["gistsnake"], "\nLadder:", snakeandladder["gistladder"])
    if positions[i] == boardrow*boardcol:
        print(Fore.MAGENTA+"\nCONGRATULATIONS PLAYER "+str(i+1)+"!! YOU WON.")
        return -1
    return positions[i]
    
# It prints the basic details of the game and and calls the fucntion for making every move for every player 
def Initiasation(players, boardrow, boardcol):
    print(Fore.WHITE+"-------------------------------------")
    positions = [0 for i in range(players)]
    snakeandladder = SnakeAndLadderCreation(boardrow*boardcol)
    print("Total Players:", players)
    print("Initial position of all the players:", 0)
    print(Fore.WHITE+"\nBoard size:", boardrow*boardcol)
    BoardCreation(positions, boardrow, boardcol, snakeandladder["snake"], snakeandladder["ladder"])
    print(Fore.WHITE+"Snake: ", snakeandladder["gistsnake"], "\nLadder: ", snakeandladder["gistladder"])
    print(Fore.WHITE+"\nRed->Snake \nGreen->Ladder \nBlue->Player")
    print(Fore.WHITE+"------------------------------------\n")
    while True:
        for i in range(len(positions)):
            positions[i] = MakingTheMove(i, positions, boardrow, boardcol, snakeandladder)
            if positions[i] == -1:
                return
    



players = 2
board_row = 6
board_col = 6
Initiasation(players, board_row, board_col)