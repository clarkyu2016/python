def check_sudoku(sudokus):
    #check row
    sum = 0 
    for row in sudokus:
        for i in row:
            if row.count(i) > 1 or i > len(sudokus):
                return False
            sum = sum + i
        if sum != (len(sudokus) * (len(sudokus) +1))/2:
            return False
        else:
            sum = 0
        
    #check column
    column = []
    n = 0
    while n < len(sudokus):
        for row in sudokus:
            column.append(row[n])
        for i in column:
            if column.count(i) > 1 or i > len(sudokus):
                return False
            else:
                column = []
        n = n + 1
    return True
