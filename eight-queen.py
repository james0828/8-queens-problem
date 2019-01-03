import sys


# deal with input about height and width
try:
    height = input('height:')
    width = input('width:')
    # use matrix to save the chestboard 0 means the blank cell, 1 means the queen, 2 means the barrier
    matrix = [[0 for n in range(0, int(width))] for n in range(0, int(height))]
except:
    sys.exit('format about height or width is wrong')

# deal with input about the queens which are existed
num = input('how many queens would you want?')
queens = []

for i in range(0, int(num)):
    temp = input('queen:')
    try:
        t = temp.split(',')
        print(t)
        matrix[int(t[0])][int(t[1])] = 1
    except:
        sys.exit('format error or your index is over the chestboard')

# deal with input about the barriers which are existed
num = input('how many barrier would you want?')
barrier = []

for i in range(0, int(num)):
    temp = input('barrier:')
    try:
        t = temp.split(',')
        matrix[t[0]][t[1]] = 2
    except:
        sys.exit('format error or your index is over the chestboard')
