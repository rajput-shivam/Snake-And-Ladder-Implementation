import random

def Dice():
    return random.choice([1,2,3,4,5,6])
    
def Move(position, move):
    position = position + move
    if position>10:
        print("Cant Move")
        position = position - move
        return position
    #SnakeMove
    if position == 8:   
        input("8 Snake!! Press Enter")
        position = 3
    #LadderMove
    if position == 2:
        input("2 Ladder!! Press Enter")
        position = 7
    return position
    
position = 0
print("Initial Position", position)
while True:
    input("Eneter To Roll The Dice")
    move = Dice()
    print("Dice Gave:", move)
    position = Move(position, move)
    print(position)
    if position == 10:
        print("CONGRATULATIONS!!")
        break
    




    
    