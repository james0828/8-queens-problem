import sys

# deal with input about height and width

try:
    height = int(input('height:'))
    width = int(input('width:'))
    # use matrix to save the chestboard 0 means the blank cell, 1 means the queen, 2 means the barrier

    matrix = [['O' for n in range(0, width)] for n in range(0, height)]
except:
    sys.exit('format about height or width is wrong')

# deal with input about the queens which are existed

num = input('how many queens would you want?')

for i in range(0, int(num)):
    temp = input('queen:')
    try:
        t = temp.split(',')
        print(t)
        matrix[int(t[0])][int(t[1])] = 'Q'
    except:
        sys.exit('format error or your index is over the chestboard')

# deal with input about the barriers which are existed

num = input('how many barrier would you want?')

for i in range(0, int(num)):
    temp = input('barrier:')
    try:
        t = temp.split(',')
        matrix[int(t[0])][int(t[1])] = 'B'
    except:
        sys.exit('format error or your index is over the chestboard')

# deal with input about power

power = int(input('power: '))

# deal with the cells in matrix

max_num = 0
max_cell = []

# inspect whether the cell can put Queen

def inspect_matrix(i, j, power, matrix):
    judge = True

    for x in range(1, power + 1):
        if inspect_cell(i - x, j, matrix) or inspect_cell(i + x, j, matrix) or inspect_cell(i, j + x, matrix) or inspect_cell(i, j - x, matrix)\
            or inspect_cell(i + x, j + x, matrix) or inspect_cell(i + x, j - x, matrix) or inspect_cell(i - x, j + x, matrix) or inspect_cell(i - x, j - x, matrix):
            judge = False
            break

    return judge

# inspect whether the cell is Queen

def inspect_cell(i,j, matrix):
    global height
    global width

    if i < height and j < width and matrix[i][j] == 'Q':
        return True

    return False                 

# depth-first-search implement for advanced n-queen problem

def dfs(i, j, power, matrix, num):
    global height
    global width
    global max_num
    global max_cell

    if matrix[i][j] == 'O' and inspect_matrix(i, j, power, matrix):
        matrix[i][j] = 'Q'
        dfs(i, j, power, matrix[:], num + 1)
    if i == height - 1 and j == width - 1:
        if max_num < num:
            max_num = num
            max_cell = matrix
    elif j == width -1:
        dfs(i + 1, 0, power, matrix, num)
    else:
        dfs(i, j + 1, power, matrix, num)

dfs(0, 0, power, matrix, 0)
