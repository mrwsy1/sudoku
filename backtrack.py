def find_empty_box(sample):
    for i in range(9):
        for j in range(9):
            if sample[i][j]==0:
                return i, j
    return None, None

def is_valid(sample, digit, row, col):
    #check row
    if digit in sample[row]:
        return False
    #check col
    for i in range(9):
        if sample[i][col]==digit:
            return False
    #check subgrid
    x_start = (row//3)*3
    y_start = (col//3)*3
    for i in range(x_start, x_start+3):
        for j in range(y_start, y_start+3):
            if sample[i][j]==digit:
                return False
    return True

def find_solution(sample):
    row, col = find_empty_box(sample)
    if row is None:
        return True
    for digit in range(1, 10):
        if is_valid(sample, digit, row, col)==True:
            sample[row][col] = digit
            if find_solution(sample)==True:
                return True
            sample[row][col] = 0
    return False
