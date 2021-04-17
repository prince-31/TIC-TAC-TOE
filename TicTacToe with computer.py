#TIC TAC TOE

import numpy
import random

def computer_training(A,flag):
    lists=[0,1,2,10,11,12,20,21,22]
    while(1):
        n=1
        for i in range(18):
            n=n+flag[i]
        if(n>0):
            if(A[0][0]=='O' and flag[0]==1):
                if(A[0][1]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='O' and A[0][1]=='_'):
                    return 1
                elif(A[1][1]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='O' and A[1][1]=='_'):
                    return 11
                elif(A[1][0]=='O' and A[2][0]=='_'):
                    return 20
                elif(A[2][0]=='O' and A[1][0]=='_'):
                    return 10
                else:
                    flag[0]=0
                    continue
            elif(A[0][2]=='O' and flag[1]==1):
                if(A[0][1]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[0][1]=='_'):
                    return 1
                elif(A[1][1]=='O' and A[2][0]=='_'):
                    return 20
                elif(A[2][0]=='O' and A[1][1]=='_'):
                    return 11
                elif(A[1][2]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='O' and A[1][2]=='_'):
                    return 12
                else:
                    flag[1]=0
                    continue
            elif(A[2][0]=='O' and flag[2]==1):
                if(A[1][0]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[1][0]=='_'):
                    return 10
                elif(A[1][1]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='O' and A[1][1]=='_'):
                    return 11
                elif(A[2][1]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='O' and A[2][1]=='_'):
                    return 21
                else:
                    flag[2]=0
                    continue
            elif(A[2][2]=='O' and flag[3]==1):
                if(A[0][2]=='O' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[1][1]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[1][1]=='_'):
                    return 11
                elif(A[2][0]=='O' and A[2][1]=='_'):
                    return 21
                elif(A[2][1]=='O' and A[2][0]=='_'):
                    return 20
                else:
                    flag[3]=0
                    continue
            elif(A[1][1]=='O' and flag[4]==1):
                if(A[2][2]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[2][0]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='O' and A[2][0]=='_'):
                    return 20
                elif(A[2][1]=='O' and A[0][1]=='_'):
                    return 1
                elif(A[0][1]=='O' and A[2][1]=='_'):
                    return 21
                elif(A[1][0]=='O' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='O' and A[1][0]=='_'):
                    return 10
                else:
                    flag[4]=0
                    continue
            elif(A[1][0]=='O' and flag[5]==1):
                if(A[2][0]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[2][0]=='_'):
                    return 20
                elif(A[1][1]=='O' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='O' and A[1][1]=='_'):
                    return 11
                else:
                    flag[5]=0
                    continue
            elif(A[0][1]=='O' and flag[6]==1):
                if(A[0][2]=='O' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[1][1]=='O' and A[2][1]=='_'):
                    return 21
                elif(A[2][1]=='O' and A[1][1]=='_'):
                    return 11
                else:
                    flag[6]=0
                    continue
            elif(A[1][2]=='O' and flag[7]==1):
                if(A[2][2]=='O' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[1][1]=='O' and A[1][0]=='_'):
                    return 10
                elif(A[1][0]=='O' and A[1][1]=='_'):
                    return 11
                else:
                    flag[7]=0
                    continue
            elif(A[2][1]=='O' and flag[8]==1):
                if(A[2][0]=='O' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='O' and A[2][0]=='_'):
                    return 20
                elif(A[1][1]=='O' and A[0][1]=='_'):
                    return 1
                elif(A[0][1]=='O' and A[1][1]=='_'):
                    return 11
                else:
                    flag[8]=0
                    continue
            elif(A[0][0]=='X' and flag[9]==1):
                if(A[0][1]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='X' and A[0][1]=='_'):
                    return 1
                elif(A[1][1]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='X' and A[1][1]=='_'):
                    return 11
                elif(A[1][0]=='X' and A[2][0]=='_'):
                    return 20
                elif(A[2][0]=='X' and A[1][0]=='_'):
                    return 10
                else:
                    flag[9]=0
                    continue
            elif(A[0][2]=='X' and flag[10]==1):
                if(A[0][1]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[0][1]=='_'):
                    return 1
                elif(A[1][1]=='X' and A[2][0]=='_'):
                    return 20
                elif(A[2][0]=='X' and A[1][1]=='_'):
                    return 11
                elif(A[1][2]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='X' and A[1][2]=='_'):
                    return 12
                else:
                    flag[10]=0
                    continue
            elif(A[2][0]=='X' and flag[11]==1):
                if(A[1][0]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[1][0]=='_'):
                    return 10
                elif(A[1][1]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='X' and A[1][1]=='_'):
                    return 11
                elif(A[2][1]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='X' and A[2][1]=='_'):
                    return 21
                else:
                    flag[11]=0
                    continue
            elif(A[2][2]=='X' and flag[12]==1):
                if(A[0][2]=='X' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[1][1]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[1][1]=='_'):
                    return 11
                elif(A[2][0]=='X' and A[2][1]=='_'):
                    return 21
                elif(A[2][1]=='X' and A[2][0]=='_'):
                    return 20
                else:
                    flag[12]=0
                    continue
            elif(A[1][1]=='X' and flag[13]==1):
                if(A[2][2]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[2][0]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='X' and A[2][0]=='_'):
                    return 20
                elif(A[2][1]=='X' and A[0][1]=='_'):
                    return 1
                elif(A[0][1]=='X' and A[2][1]=='_'):
                    return 21
                elif(A[1][0]=='X' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='X' and A[1][0]=='_'):
                    return 10
                else:
                    flag[13]=0
                    continue
            elif(A[1][0]=='X' and flag[14]==1):
                if(A[2][0]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[2][0]=='_'):
                    return 20
                elif(A[1][1]=='X' and A[1][2]=='_'):
                    return 12
                elif(A[1][2]=='X' and A[1][1]=='_'):
                    return 11
                else:
                    flag[14]=0
                    continue
            elif(A[0][1]=='X' and flag[15]==1):
                if(A[0][2]=='X' and A[0][0]=='_'):
                    return 0
                elif(A[0][0]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[1][1]=='X' and A[2][1]=='_'):
                    return 21
                elif(A[2][1]=='X' and A[1][1]=='_'):
                    return 11
                else:
                    flag[15]=0
                    continue
            elif(A[1][2]=='X' and flag[16]==1):
                if(A[2][2]=='X' and A[0][2]=='_'):
                    return 2
                elif(A[0][2]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[1][1]=='X' and A[1][0]=='_'):
                    return 10
                elif(A[1][0]=='X' and A[1][1]=='_'):
                    return 11
                else:
                    flag[16]=0
                    continue
            elif(A[2][1]=='X' and flag[17]==1):
                if(A[2][0]=='X' and A[2][2]=='_'):
                    return 22
                elif(A[2][2]=='X' and A[2][0]=='_'):
                    return 20
                elif(A[1][1]=='X' and A[0][1]=='_'):
                    return 1
                elif(A[0][1]=='X' and A[1][1]=='_'):
                    return 11
                else:
                    flag[17]=0
                    continue
            else:
                l=random.choice(lists)
                return l

def toss():
    n=random.randint(1,100)%2
    return n

def another_round(p1n,p2n,pp1,pp2):
    print(p1n,'wanna play more?')
    a=int(input('press 1 to play or 0 to quit:-'))
    if(a==1):
        return 1
    else:
        print(p1n,'Your score:-',pp1)
        print(p2n,'Your score:-',pp2)
        if(pp1>pp2):
            print('Hurrah!',p1n,'You won!')
        else:
            if(pp1<pp2):
                print('Oops Computer won!')
            else:
                print('Match tie!')
        print(p1n,'Thanks for playing.\nHave a nice day.')
        return 0

def null_matrix():
    M=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
    print(M)
    return M

def play():
    #null matrix will be created
    A=null_matrix()
    p1name=input('Player 1,Your name:-')
    p2name='Computer'
    print('Player 2 :-',p2name)
    turn=0
    #r will indicate the no. of round
    r=1
    #pp1 & pp2 are points of player and computers.
    pp1=0
    pp2=0
    #random value of 0 or 1 will be created so that player who makes first move,will be choosed randomly.
    t=toss()
    while(turn<9):
        if(turn==0):
            print('ROUND',r,'STARTED.')
        if(turn%2==t):
            print(p1name,'Your turn:-')
            n=input('Enter row and column no. together(like 13 for 1st row and 3rd column):-')
            row=int(int(n)/10)-1
            col=int(n)%10-1
            if(row<3 and col<3):
                if(A[row][col]=='_'):
                    A[row][col]='X'
                else:
                    print('Place already occupied.')
                    continue
            else:
                print('Please enter valid rows and column only.')
                continue
            print(A)
        else:
            print("Computer's turn:-")
            #reducing starting move error of computer
            if(turn<=1):
                if(A[1][1]=='_'):
                    ct=11
                else:
                    ct=0
            else:
                flag=[1]*18
                #Train computer so that it doesn't make silly errors like humans
                ct=computer_training(A,flag)
            row=int(ct/10)
            col=ct%10
            print(ct+11)
            if(A[row][col]=='_'):
                A[row][col]='O'
            else:
                print('Place already occupied.')
                continue
            print(A)
        
        if(A[0][0]==A[0][1]==A[0][2]=='X' or A[1][0]==A[1][1]==A[1][2]=='X' or A[2][0]==A[2][1]==A[2][2]=='X' or A[0][0]==A[1][0]==A[2][0]=='X' or A[0][1]==A[1][1]==A[2][1]=='X' or A[0][2]==A[1][2]==A[2][2]=='X' or A[0][0]==A[1][1]==A[2][2]=='X' or A[0][2]==A[1][1]==A[2][0]=='X'):
            pp1=pp1+1
            print(p1name,'wins the round.')
            print(p1name,':-',pp1)
            print(p2name,':-',pp2)
            y=another_round(p1name, p2name, pp1, pp2)
            if(y==0):
                break
            else:
                #New round therefore everything have to be reset.
                A=null_matrix()
                turn=0
                r=r+1
                t=toss()
        else:
            if(A[0][0]==A[0][1]==A[0][2]=='O' or A[1][0]==A[1][1]==A[1][2]=='O' or A[2][0]==A[2][1]==A[2][2]=='O' or A[0][0]==A[1][0]==A[2][0]=='O' or A[0][1]==A[1][1]==A[2][1]=='O' or A[0][2]==A[1][2]==A[2][2]=='O' or A[0][0]==A[1][1]==A[2][2]=='O' or A[0][2]==A[1][1]==A[2][0]=='O'):
                pp2=pp2+1
                print(p2name,'wins the round.')
                print(p1name,':-',pp1)
                print(p2name,':-',pp2)
                y=another_round(p1name, p2name, pp1, pp2)
                if(y==0):
                    break
                else:
                    #New round therefore everything have to be reset.
                    A=null_matrix()
                    r=r+1
                    turn=0
                    t=toss()
            else:
                if(turn<8):
                    turn=turn+1
                else:
                    print('Draw.')
                    print(p1name,':-',pp1)
                    print(p2name,':-',pp2)
                    y=another_round(p1name, p2name, pp1, pp2)
                    if(y==0):
                        break
                    else:
                        #New round therefore everything have to be reset.
                        A=null_matrix()
                        r=r+1
                        turn=0
                        t=toss()

play()