# Numero de reinas a buscar
queens_to_find = 8
#**************************
rows_tot = queens_to_find - 1
columns_tot = queens_to_find - 1

columns = []
diag_45 = []
diag_135 = []
queens = []

def validateQueen(row,column):
    if column in columns or (column-row) in diag_45 or (column+row) in diag_135:
        return False
    else :
        return True

def validateQueens(row,column,data):

    data['iterations_standard'] = data.get('iterations_standard',0) + 1
    data['iterations'] = data.get('iterations',0) + 1

    if len(queens) == queens_to_find:
        del columns[:]
        del diag_45[:]
        del diag_135[:]
        result = list(queens)
        del queens[:]
        return ('standard ',result)
    elif column > columns_tot:
        del columns[-1]
        del diag_45[-1]
        del diag_135[-1]
        row_temp = queens[-1][0]
        column_temp = queens[-1][1]
        del queens[-1]
        return validateQueens(row_temp,column_temp+1,data)
    elif validateQueen(row,column):
        columns.append(column)
        diag_45.append(column-row)
        diag_135.append(column+row)
        queens.append((row,column))
        return validateQueens(row+1,0,data)
    else:
        return validateQueens(row,column+1,data)