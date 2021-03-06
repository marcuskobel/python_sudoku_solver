from sudoku_solver import *
from common import *
from sys import exit


# sudoku 1 - easy
# resolved in 242 tries, v1
# resolved in 61 tries, v2
sudoku_grid = [
    [2, 0, 0, 5, 0, 7, 0, 0, 0], 
    [0, 0, 6, 2, 3, 0, 1, 0, 0], 
    [7, 5, 3, 6, 0, 0, 0, 4, 8],
    [0, 0, 0, 8, 0, 0, 4, 5, 1], 
    [3, 0, 0, 0, 6, 0, 9, 0, 2], 
    [0, 8, 5, 0, 2, 0, 0, 3, 0],
    [5, 0, 1, 0, 0, 9, 6, 0, 0], 
    [0, 4, 9, 7, 0, 0, 0, 0, 3], 
    [8, 2, 7, 0, 0, 6, 0, 9, 0]]

# sudoke 2 - medium
# resolved in 860 tries, v1 - solution was invalid :(
# resolved in 86741 tries, v2
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
# resolved in 144742 tries, v1
# resolved in 17784 tries, v2
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

# very hard sudoku 4
# resolved in 115256 tries, v1
# resolved in 13792 tries, v2
# sudoku_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 2, 9, 0, 0, 0, 6, 0, 0], 
#     [0, 0, 0, 0, 0, 5, 0, 0, 2],
#     [0, 5, 6, 0, 9, 0, 4, 0, 0], 
#     [1, 0, 0, 0, 0, 4, 0, 0, 0], 
#     [0, 8, 0, 0, 5, 0, 0, 7, 0],
#     [0, 0, 0, 5, 2, 0, 0, 0, 4], 
#     [0, 6, 0, 0, 0, 0, 0, 1, 0], 
#     [2, 1, 8, 0, 0, 0, 0, 0, 7]]

# sudoku 5 - expert
# resolved in 2394 tries, v1 - solution was wrong
# resolved in 108190 tries, v2
# sudoku_grid = [
#     [0, 0, 0, 4, 1, 0, 0, 0, 0], 
#     [0, 8, 0, 7, 0, 0, 2, 0, 0], 
#     [0, 7, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 6, 0, 0, 0, 3, 0, 0], 
#     [2, 0, 0, 0, 9, 6, 0, 7, 0], 
#     [0, 0, 0, 0, 8, 4, 0, 0, 0],
#     [5, 3, 0, 0, 0, 0, 8, 0, 4], 
#     [0, 0, 0, 0, 0, 9, 0, 6, 0], 
#     [0, 4, 0, 0, 0, 1, 0, 0, 0]]

# world hardest sudoku according to  https://www.conceptispuzzles.com/index.aspx?uri=info/article/424
# unresolved after 1M tries
# sudoku_grid = [
#     [8, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 0, 3, 6, 0, 0, 0, 0, 0], 
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0], 
#     [0, 0, 0, 0, 4, 5, 7, 0, 0], 
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8], 
#     [0, 0, 8, 5, 0, 0, 0, 1, 0], 
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]]


# sudoku AI Escargot - https://www.kristanix.com/sudokuepic/worlds-hardest-sudoku.php
# resolved in 168 tries, v1 - solution was wrong
# resolved in 8969 tries, v2
# sudoku_grid = [
#     [1, 0, 0, 0, 0, 7, 0, 9, 0], 
#     [0, 3, 0, 0, 2, 0, 0, 0, 8], 
#     [0, 0, 9, 6, 0, 0, 5, 0, 0],
#     [0, 0, 5, 3, 0, 0, 9, 0, 0], 
#     [0, 1, 0, 0, 8, 0, 0, 0, 2], 
#     [6, 0, 0, 0, 0, 4, 0, 0, 0],
#     [3, 0, 0, 0, 0, 0, 0, 1, 0], 
#     [0, 4, 0, 0, 0, 0, 0, 0, 7], 
#     [0, 0, 7, 0, 0, 0, 3, 0, 0]]

# sudoku 0 (zeroed)
# resovled with 302 tries, v1
# resovled with 391 tries, v2
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

# local news paper sudoku = Dec/18/20
# resolved with 131318 tries, v1
# resolved with 831 tries, v2
# sudoku_grid = [
#     [0, 5, 0, 0, 8, 0, 0, 0, 0], 
#     [0, 0, 1, 2, 6, 0, 0, 5, 7], 
#     [0, 3, 0, 0, 5, 9, 0, 4, 0],
#     [0, 6, 2, 0, 0, 0, 3, 8, 0], 
#     [0, 1, 5, 0, 0, 0, 4, 0, 0], 
#     [0, 4, 0, 0, 3, 0, 0, 1, 9],
#     [1, 0, 8, 0, 9, 0, 0, 3, 0], 
#     [0, 2, 3, 0, 7, 0, 0, 0, 0], 
#     [5, 9, 0, 0, 0, 0, 7, 2, 0]]


# local news paper sudoku = Dec/19/20
# resolved with 4159 tries, v1
# resolved with 4157 tries, v2
# sudoku_grid = [
#     [2, 0, 6, 0, 9, 0, 8, 0, 0], 
#     [0, 0, 1, 0, 0, 0, 0, 0, 2], 
#     [8, 0, 0, 0, 0, 0, 0, 3, 0],
#     [0, 0, 4, 7, 0, 0, 9, 0, 0], 
#     [7, 0, 0, 3, 6, 0, 4, 1, 5], 
#     [0, 0, 0, 0, 1, 0, 0, 8, 7],
#     [3, 0, 8, 2, 5, 7, 0, 0, 0], 
#     [0, 0, 0, 9, 3, 0, 0, 2, 8], 
#     [5, 9, 0, 0, 0, 1, 0, 0, 6]]


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