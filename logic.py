import random
import moves
from copy import deepcopy as dp
import os

#board = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
a = [[0000,0000,0000,0000], [0000,0000,0000,0000], [0000,0000,0000,0000] ,[0000,0000,0000,0000]]
ac =[]
ch = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
choices = ch.copy()
lose = []
pool = [2,4]
count = 0
t = []


def rb(c):
    return a[c]
    pass
def rn(c):
    row = c//4
    col = (c%4)
    return a[row][col]

def Upper(a,b): #dealing with a column  ...takes array and col number
    global t
    global count
    count = b
    for i in range(4):
        t.append(rn(b+(i*4)))
    
def wn(c, data):
    row = c//4
    col = (c%4)
    a[row][col] = data
    
def start():
    row = random.choice(choices)
    col = random.choice(choices)
    while row==col:
        col = random.choice(choices)
    wn(row, 2)
    wn(col, 2 )

def write(r,t):
    for i in range(4):
        wn(count+(i*4),t[i])

def clean():
    for i in range(16):
        if rn(i)==0:
            lose.append(i)
def populate():
    wn(random.choice(lose),random.choice(pool))

def pb():#shows the current board
    for i in a:
        print(i)

def mright():
    for i in a:
        moves.right(i)
    clean()
    if a!=ac:
        populate()   
        clean()
    elif a==ac:
        pass
    
def mleft():
    global ac
    ac = a.copy
    for i in a:
        moves.left(i)
    clean()
    if a!=ac:
        populate()   
        clean()
    elif a==ac:
        pass


def mdown():
    global a
    d = []
    d = dp(a)
 
    for i in range(4):
        Upper(a,i)
        moves.down(t)
        write(a,t)
        t.clear()
    clean()
    if a!=d:
        populate()   
        clean()
        d.clear()
    elif a==d:
        d.clear()
        pass
def mup():
    global ac
    global a
    ac = dp(a)
    for i in range(4):
        Upper(a,i)
        moves.up(t)
        write(a,t)
        t.clear()
    clean()
    if a!=ac:
        populate()   
        clean()
    elif a==ac:
        pass

'''def ply():
    #pb()
    moves = {"w":mup,"a":mleft,"s":mdown,"d":mright}
    
    value = input("")
    value = value.lower()
    if value in moves:
        moves[value]()
        os.system('clear')
        print(f"making move {value}")
        pb()

'''