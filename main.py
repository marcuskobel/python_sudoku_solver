def is_sudoku_valid(sudoku_grid):
    for n in range(1, 10):
        # print('for 1')
        for i in range(0, 9):
            nfound = False
            # print('checking number = ' +str(n)+ ' at position ' +str(i)+ ',' +str(j)+ ' = ' + str(sudoku_grid[i][j]))
            if n in sudoku_grid[i]:
                if nfound:
                    # print('found issue!!')
                    return False
                else:
                    nfound = True

        # print('for 2')
        for j in range(0, 9):
            nfound = False
            for i in range(0, 9):
                # print('checking number = ' +str(n)+ ' at position ' +str(i)+ ',' +str(j)+ ' = ' + str(sudoku_grid[i][j]))
                if sudoku_grid[i][j] == n:
                    if nfound:
                        # print('found issue!!')
                        return False
                    else:
                        nfound = True
    # print('True')
    return True


def analyze_sudoku(sudoku_grid):
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_grid[i][j] > 0:
                count += 1
    print('initial numbers found in sudoku = ' + str(count))

def is_sudoku_completed(sudoku_grid):
    # small function to tell when to stop for solutions
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_grid[i][j] == 0:
                return False
    return True


def solve_sudoku(current_sudoku_grid, iteration_level):
    for i in range(0, 9):
        for j in range(0, 9):
            for t in range(1, 10):
                if current_sudoku_grid[i][j] == 0:
                    current_sudoku_grid[i][j] = t
                    if is_sudoku_valid(current_sudoku_grid):
                        if is_sudoku_completed(current_sudoku_grid):
                            # sudoku is resolved (hopefully!), print it and get out
                            print('LVL'+str(iteration_level)+' SODUKU SOLUTION FOUND!')
                            print_sudoku_grid(current_sudoku_grid)
                            return True

                        print('LVL'+str(iteration_level)+' - assigning '+str(t)+' at position '+str(i)+','+str(j) + ' and restarting recursion')
                        il = iteration_level+1
                        if solve_sudoku(current_sudoku_grid, il):
                            # stop sudoku solving because an inner recursion has found a solution
                            return True

                    else:
                        print('LVL'+str(iteration_level)+' - possiility '+str(t)+' didnt work at position ' + str(i) + ',' + str(j))
                        current_sudoku_grid[i][j] = 0

    print('LVL'+str(iteration_level)+' - NO POSSIBILITY WORKED, BACKING OFF!!')
    # tell previous recursion that current has failed
    return False


def print_sudoku_grid(my_sudoku_grid):
    for i in range(0, 9):
        if (i == 3 or i == 6):
            print('')
        for j in range(0, 9):
            if (j == 3 or j == 6):
                print(' ', end='')
            print(' %s' % my_sudoku_grid[i][j], end='')
        print('')


# random sudoku
sudoku_grid = [
    [2, 0, 0, 5, 0, 7, 0, 0, 0], [0, 0, 6, 2, 3, 0, 1, 0, 0], [7, 5, 3, 6, 0, 0, 0, 4, 8],
    [0, 0, 0, 8, 0, 0, 4, 5, 1], [3, 0, 0, 0, 6, 0, 9, 0, 2], [0, 8, 5, 0, 2, 0, 0, 3, 0],
    [5, 0, 1, 0, 0, 9, 6, 0, 0], [0, 4, 9, 7, 0, 0, 0, 0, 3], [8, 2, 7, 0, 0, 6, 0, 9, 0]]

# easy sudoku
# sudoku_grid = [
#     [2, 0, 0, 5, 0, 7, 0, 0, 0], [0, 0, 6, 2, 3, 0, 1, 0, 0], [7, 5, 3, 6, 0, 0, 0, 4, 8],
#     [0, 0, 0, 8, 0, 0, 4, 5, 1], [3, 0, 0, 0, 6, 0, 9, 0, 2], [0, 8, 5, 0, 2, 0, 0, 3, 0],
#     [5, 0, 1, 0, 0, 9, 6, 0, 0], [0, 4, 9, 7, 0, 0, 0, 0, 3], [8, 2, 7, 0, 0, 6, 0, 9, 0]]

# very hard sudoku
# sudoku_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 9, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 0, 5, 0, 0, 2],
#     [0, 5, 6, 0, 9, 0, 4, 0, 0], [1, 0, 0, 0, 0, 4, 0, 0, 0], [0, 8, 0, 0, 5, 0, 0, 7, 0],
#     [0, 0, 0, 5, 2, 0, 0, 0, 4], [0, 6, 0, 0, 0, 0, 0, 1, 0], [2, 1, 8, 0, 0, 0, 0, 0, 7]]


print("Starting to solve Sudoku!")
print('Check if initial sudoku grid is valid: ', end='')

is_valid = is_sudoku_valid(sudoku_grid)
if is_valid:
    print('VALID!')
    analyze_sudoku(sudoku_grid)
else:
    print('INVALID!')
    exit()

solve_sudoku(sudoku_grid, 1)