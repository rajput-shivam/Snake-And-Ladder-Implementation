import random

def Dice():
    return random.choice([1,2,3,4,5,6])
    
def Move(position, move):
    position = position + move
    if position>10:
        print("Cant Move")
        position = position - move
    return position
        
def SnakeAndLadder(position):
    if position == 8:
        print("Snake Found: downgraded from 8 to 3")
        position = 3
        print("Current Position",position)
        
    if position == 2:
        print("Ladder Found: upgraed from 2 to 7")
        position = 7
        print("Current Position",position)
    return position
    
    
position = 0
print("Initial Position", position)
while True:
    input("Eneter To Roll The Dice")
    move = Dice()
    print("Dice Gave:", move)
    position = Move(position, move)
    print("Current Position",position)
    newposition = SnakeAndLadder(position)
    if position == 10:
        print("CONGRATULATIONS!!")
        break
    




    
    