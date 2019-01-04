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

origin_queen = []
for i in range(0, int(num)):
    temp = input('queen:')
    try:
        t = temp.split(',')
        origin_queen.append((int(t[0]), int(t[1])))
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
    judge = True # judge whether the cell can be Queen
    run = [True for n in range(8)] # judge whetehr the direction should be run
    temp = [0 for n in range(8)] # tempitively save the inspect console
    barrier_cell = [None for n in range(8)] # save the cell about the barrier
    has_barrier = [False for n in range(8)]

    for x in range(1, power + 1):
        if run[0]:
            temp[0] = inspect_cell(i - x, j, matrix, has_barrier[0])
        if run[1]:
            temp[1] = inspect_cell(i + x, j, matrix, has_barrier[1])
        if run[2]:
            temp[2] = inspect_cell(i, j + x, matrix, has_barrier[2])
        if run[3]:
            temp[3] = inspect_cell(i, j - x, matrix, has_barrier[3])
        if run[4]:
            temp[4] = inspect_cell(i + x, j + x, matrix, has_barrier[4])
        if run[5]:
            temp[5] = inspect_cell(i + x, j - x, matrix, has_barrier[5])
        if run[6]:
            temp[6] = inspect_cell(i - x, j + x, matrix, has_barrier[6])
        if run[7]:
            temp[7] = inspect_cell(i - x, j - x, matrix, has_barrier[7])

        if temp[0] == 0 or temp[1] == 0 or temp[2] == 0 or temp[3] == 0 or temp[4] == 0 or temp[5] == 0 or temp[6] == 0 or temp[7] == 0:
            judge = False
            break

        for t in range(8):
            if temp[t] == 1:
                temp[t] = False
                run[t] = False
                if barrier_cell[t] != None:
                    barrier_cell[t] = (barrier_cell[t][0], True)
            elif type(temp[t]) == tuple:
                has_barrier[t] = True
                barrier_cell[t] = (temp[t], False)

    if judge:
        return barrier_cell
    else:
        return False

# inspect the cell of (i, j)

def inspect_cell(i, j, matrix, has_barrier):
    global height
    global width

    if i < height and j < width and i >= 0 and j >= 0:
        if has_barrier:
            if matrix[i][j] == 'Q':
                return 1
        else:
            if matrix[i][j] == 'Q':
                return 0
            elif matrix[i][j] == 'B':
                return (i, j)

    return 3

# depth-first-search implement for advanced n-queen problem

def dfs(i, j, power, matrix, num):
    global height
    global width
    global max_num
    global max_cell

    consoles = inspect_matrix(i, j, power, matrix)

    if matrix[i][j] == 'O' and type(consoles) == list:
        clone_matrix = matrix[:]
        clone_matrix[i][j] = 'Q'

        for console in consoles:
            if type(console) == tuple and console[1]:
                clone_matrix[console[0][0]][console[0][1]] = 'X'

        dfs(i, j, power, clone_matrix, num + 1)
    if i == height - 1 and j == width - 1:
        if max_num < num:
            max_num = num
            max_cell = matrix
    elif j == width -1:
        dfs(i + 1, 0, power, matrix, num)
    else:
        dfs(i, j + 1, power, matrix, num)

dfs(0, 0, power, matrix, 0)

result_queen = []
print('max: ' + str(max_num))
for m, i in enumerate(max_cell):
    print(i)
    for n, j in enumerate(i):
        if j == 'Q':
            if (m, n) not in origin_queen:
                result_queen.append((m, n))

for result in result_queen:
    print(result)