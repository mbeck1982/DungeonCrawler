import os
import random

def displayMap():
    os.system('cls')  # on windows
    #os.system('clear')  # on linux / os x
    print("\t",end=" ")
    for column in range(NUM_COLUMNS):
        print(column,end="\t")#displays column header
   

    print("\n")
    for row in range (NUM_ROWS):
        print(row,end="\t")#displays row header
        for column in range (NUM_COLUMNS):
            if column==player_x and row==player_y:
                print("P",end="\t")
            elif column==monster_x and row==monster_y:
                print("M",end="\t")
            elif column==store_x and row==store_y:
                print("S",end="\t")
            else:
                print(grid[row][column],end="\t")
        print("\n")

def fight():
        print("You are being attacked by a monster")

def buy_stuff():
    print("You are in a store")
    print(store_inventory)


grid=[['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0']]


NUM_ROWS=len(grid)
NUM_COLUMNS=len(grid[0])

player_x=0
player_y=0
player_money=1000

store_inventory={"Sword":100,"Helmet":50,"Shield":75}
store_x=1
store_y=2


monster_x=random.randrange(NUM_COLUMNS)
monster_y=random.randrange(NUM_ROWS)

while 5>3:
    displayMap()
        
    if monster_x ==player_x and monster_y==player_y:
        fight()
    elif store_x ==player_x and store_y==player_y:
        buy_stuff()
        
    else:
        move=input("Please enter a direction")

    if move=='N':
        if player_y-1>=0:
            player_y-=1
        else:
            print("You can't go that way!")
    elif move=='S':
        if player_y+1<NUM_ROWS:
            player_y+=1
        else:
            print("You can't go that way!")
    elif move=='E':
        if player_x+1<NUM_COLUMNS:
            player_x+=1
        else:
            print("You can't go that way!")
    elif move=='W':
        if player_x-1>=0:
            player_x-=1
        else:
            print("You can't go that way!")
            
    
