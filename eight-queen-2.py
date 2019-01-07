import sys
import copy

sys.setrecursionlimit(1000000)

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

barriers = []
for i in range(0, int(num)):
    temp = input('barrier:')
    try:
        t = temp.split(',')
        barriers.append(t)
        matrix[int(t[0])][int(t[1])] = 'B'
    except:
        sys.exit('format error or your index is over the chestboard')

# deal with input about power

power = int(input('power: '))

# deal with the cells in matrix

max_num = 0
max_cell = []

def get_runlist(matrix):
    global height
    global width
    global power
    count = 0
    console = []
    all_way = []
    key = True
    for i, s in enumerate(matrix):
        for j, _ in enumerate(s):
            if matrix[i][j] == 'O':
                can_run = [True for n in range(8)]
                for m in range(1, power + 1):
                    if can_run[0]:
                        temp = can_put(i + m, j, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[0] = False
                        else:
                            key = False
                            break
                    if can_run[1]:
                        temp = can_put(i - m, j, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[1] = False
                        else:
                            key = False
                            break
                    if can_run[2]:
                        temp = can_put(i, j + m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[2] = False
                        else:
                            key = False
                            break
                    if can_run[3]:
                        temp = can_put(i, j - m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[3] = False
                        else:
                            key = False
                            break
                    if can_run[4]:
                        temp = can_put(i + m, j + m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[4] = False
                        else:
                            key = False
                            break
                    if can_run[5]:
                        temp = can_put(i - m, j - m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[5] = False
                        else:
                            key = False
                            break
                    if can_run[6]:
                        temp = can_put(i - m, j + m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[6] = False
                        else:
                            key = False
                            break
                    if can_run[7]:
                        temp = can_put(i + m, j - m, matrix)
                        if temp == 2:
                            count += 1
                        elif temp == 0:
                            can_run[7] = False
                        else:
                            key = False
                            break
                if key:
                    all_way.append([i, j])
                    try:
                        if minimum > count:
                            minimum = count
                            console = []
                            console.append([i, j])
                        elif minimum == count:
                            console.append([i, j])
                    except:
                        minimum = count
                        console.append([i, j])
                key = True
                count = 0
    return (console, all_way)

def get_new_runlist(runlist):
    global power
    global barriers
    key = False
    count = 0
    console = []
    for i in runlist:
        for j in runlist:
            first_num = abs(j[0] - i[0])
            second_num = abs(j[1] - i[1])
            
            if (first_num == 0 and second_num <= power):
                key = True
                for barrier in barriers:
                    if barrier[0] == 0 and max(i[1], j[1]) > barrier[1] and min(i[1], j[1]) < barrier[1]:
                        key = False
            elif (first_num <= power and second_num == 0):
                key = True
                for barrier in barriers:
                    if barrier[1] == 0 and max(i[0], j[0]) > barrier[0] and min(i[0], j[0]) < barrier[0]:
                        key = False
            elif (first_num != 0 and second_num != 0 and first_num == second_num and first_num < power):
                key = True
                for barrier in barriers:
                    if max(i[0], j[0]) > barrier[0] and min(i[0], j[0]) < barrier[0] and max(i[1], j[1]) > barrier[1] and min(i[1], j[1]) < barrier[1] and (barrier[0] - i[0]) % (barrier[1] - i[1]) == 0:
                        key = False

            if key:
                count += 1
            key = False
        try:
            if count < minimum:
                minimum = count
                console = []
                console.append(i)
            elif count == minimum:
                console.append(i)    
        except:
            minimum = count
            console.append(i)
        count = 0
    return console

def get_pattern(x, y, pattern):
    temp_pattern = copy.deepcopy(pattern)
    key = False
    for i in pattern:
        first_num = abs(x - i[0])
        second_num = abs(y - i[1])
        
        if (first_num == 0 and second_num <= power):
            key = True
            for barrier in barriers:
                if barrier[0] == 0 and max(i[1], y) > barrier[1] and min(i[1], y) < barrier[1]:
                    key = False
        elif (first_num <= power and second_num == 0):
            key = True
            for barrier in barriers:
                if barrier[1] == 0 and max(i[0], x) > barrier[0] and min(i[0], x) < barrier[0]:
                    key = False
        elif (first_num != 0 and second_num != 0 and first_num == second_num and first_num <= power):
            key = True
            for barrier in barriers:
                if max(i[0], x) > barrier[0] and min(i[0], jx) < barrier[0] and max(i[1], y) > barrier[1] and min(i[1], y) < barrier[1] and (barrier[0] - i[0]) % (barrier[1] - i[1]) == 0:
                    key = False
        if key:
            temp_pattern.remove(i)
        key = False
    return temp_pattern
def can_put(i, j, matrix):
    global height
    global width

    if i < 0 or i >= height or j < 0 or j >= width or matrix[i][j] == 'B':
        return 0
    if matrix[i][j] == 'Q':
        return 1
    else:
        return 2

def dfs(matrix, num, runlist, pattern):
    global max_cell
    global max_num
    if len(runlist) == 0:
        if num > max_num:
            max_num = num
            max_cell = matrix
    else:
        for cell in runlist:
            clone_matrix = copy.deepcopy(matrix)
            clone_matrix[cell[0]][cell[1]] = 'Q'
            new_pattern = get_pattern(cell[0], cell[1], pattern)
            new_runlist = get_new_runlist(new_pattern)
            dfs(clone_matrix, num + 1, new_runlist, new_pattern)

s = get_runlist(matrix)
dfs(matrix, 0, s[0], s[1])

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