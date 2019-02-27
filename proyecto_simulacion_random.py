from random import randint
from sys import setrecursionlimit

# Setting the recursion depth property in 5000
setrecursionlimit(5000)

# Numero de reinas a buscar
queens_to_find = 8
#**************************
rows_tot = queens_to_find - 1
columns_tot = queens_to_find - 1

chances = 20

columns = []
diag_45 = []
diag_135 = []
queens = []

def validateQueenRandom(row,column):
    if column in columns or (column-row) in diag_45 or (column+row) in diag_135:
        return False
    else :
        return True

def validateQueensRandom(row,chance,data):
    column = randint(0,columns_tot)
    data['iterations_las_vegas'] = data.get('iterations_las_vegas',0) + 1
    data['iterations'] = data.get('iterations',0) + 1

    if len(queens) == queens_to_find:
        del columns[:]
        del diag_45[:]
        del diag_135[:]
        result = list(queens)
        del queens[:]
        return ('las_vegas ',result)
    elif chance > chances:
        del columns[:]
        del diag_45[:]
        del diag_135[:]
        del queens[:]
        return validateQueensRandom(0,0,data)
    elif validateQueenRandom(row,column):
        columns.append(column)
        diag_45.append(column-row)
        diag_135.append(column+row)
        queens.append((row,column))
        return validateQueensRandom(row+1,0,data)
    else:
        return validateQueensRandom(row,chance+1,data)
