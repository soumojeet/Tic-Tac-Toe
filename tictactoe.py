def user_input():
    flag = True
    game_dict={'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'7':[2,0],'8':[2,1],'9':[2,2]}
    while flag:
        choice= input('Enter a value between (1-9): ')
              
        if choice.isdigit():    
            if int(choice) in range(0,10):
                flag=False
            else:
                print('Enter within range')
        else:
            print('Enter Digit')
            
    return game_dict[choice]

def user_display(block):
    for x in block:
        print(x)
import os

def tic_tac_toe():
    print('Game Instruction:\n1->[0][0] 2->[0][1] 3->[0][2]\n4->[1][0] 5->[1][1] 6->[1][2]\n7->[2][0] 8->[2][1] 9->[2][2]')
    row= [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    user_display(row)
    switch_flag=True
    
    while check(row)==1: 
        if switch_flag:
            print('Enter for X')
            row_input,column_input = user_input()
            if row[row_input][column_input] == ' ':
                row[row_input][column_input] = 'X'
            else:
                print('Already Equipped')
                continue
        else:
            print('Enter for O')
            row_input,column_input = user_input()
            if row[row_input][column_input] == ' ':
                row[row_input][column_input] = 'O'
            else:
                print('Already Equipped')
                continue
            
        switch_flag=not switch_flag
        
        user_display(row)
    else:
        if switch_flag == True and check(row)!=2:
            print('Game Over\nPlayer O WON')
        elif switch_flag == False and check(row)!=2:
            print('Game Over\nPlayer X WON')
        else: 
            print('Game Over\nDRAW')

def check(block):
    for y in [0,1,2]:
        if block[y][0]==block[y][1]==block[y][2]!=' ' or block[0][y]==block[1][y]==block[2][y]!=' ':
            return 0
        elif block[0][0]==block[1][1]==block[2][2]!=' ' or block[2][0]==block[1][1]==block[0][2]!=' ':
            return 0
        elif block[0][0]!=' ' and block[0][1]!=' ' and block[0][2]!=' ' and block[1][0]!=' ' and block[1][1]!=' ' and block[1][2]!=' ' and block[2][0]!=' ' and block[2][1]!=' ' and block[2][2]!=' ':
            return 2
    return 1

tic_tac_toe()