from sudoku_solver import *
from common import *
from sys import exit


# sudoku 1 - easy
# sudoku_grid = [
#     [2, 0, 0, 5, 0, 7, 0, 0, 0], 
#     [0, 0, 6, 2, 3, 0, 1, 0, 0], 
#     [7, 5, 3, 6, 0, 0, 0, 4, 8],
#     [0, 0, 0, 8, 0, 0, 4, 5, 1], 
#     [3, 0, 0, 0, 6, 0, 9, 0, 2], 
#     [0, 8, 5, 0, 2, 0, 0, 3, 0],
#     [5, 0, 1, 0, 0, 9, 6, 0, 0], 
#     [0, 4, 9, 7, 0, 0, 0, 0, 3], 
#     [8, 2, 7, 0, 0, 6, 0, 9, 0]]

# sudoke 2 - medium
# sudoku_grid = [
#     [0, 0, 0, 9, 1, 0, 0, 0, 6], 
#     [2, 0, 0, 0, 7, 0, 0, 0, 0], 
#     [7, 0, 0, 0, 0, 5, 1, 0, 8],
#     [0, 4, 8, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 6, 0, 0], 
#     [5, 0, 0, 1, 9, 0, 2, 4, 0],
#     [8, 0, 0, 0, 6, 0, 0, 7, 1], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 7, 5, 0, 0, 9, 4, 0, 0]]

# sudoke 3 - hard
# sudoku_grid = [
#     [0, 4, 0, 0, 0, 0, 0, 0, 0], 
#     [2, 0, 0, 0, 3, 0, 4, 0, 8], 
#     [6, 3, 0, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 2, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 6, 8, 1, 0, 0, 2], 
#     [0, 9, 0, 0, 4, 0, 5, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 0, 3], 
#     [7, 0, 0, 0, 6, 0, 2, 1, 0], 
#     [4, 0, 0, 1, 0, 7, 0, 5, 0]]

# very hard sudoku
sudoku_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 2, 9, 0, 0, 0, 6, 0, 0], 
    [0, 0, 0, 0, 0, 5, 0, 0, 2],
    [0, 5, 6, 0, 9, 0, 4, 0, 0], 
    [1, 0, 0, 0, 0, 4, 0, 0, 0], 
    [0, 8, 0, 0, 5, 0, 0, 7, 0],
    [0, 0, 0, 5, 2, 0, 0, 0, 4], 
    [0, 6, 0, 0, 0, 0, 0, 1, 0], 
    [2, 1, 8, 0, 0, 0, 0, 0, 7]]

# sudoku 0 (zeroed)
# sudoku_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# MAIN CODE STARTS HERE
print("Welcome to solve Sudoku! Starting things up!")

logdebug("MAIN", "Instanciating Sudoku_Solver class...", False)
ss = Sudoku_Solver(sudoku_grid)

logdebug("MAIN", "Checking if initial sudoku grid is valid: ", True)

if ss.is_sudoku_valid():
    print('VALID!')
else:
    print("INVALID! Can't continue solving sudoku.")
    exit(0)

ss.print_sudoku_grid()
c = ss.count_numbers_in_sudoku_grid()
logdebug("MAIN", "Amount numbers found in sudoku = " + str(c), False)

if c < 81:
    logdebug("MAIN", "Starting to solve Sudoku!", False)
    ss.solve_sudoku(1, 0, 0)

print("Sudoku solver has finished! :)")