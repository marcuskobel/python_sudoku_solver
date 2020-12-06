from common import *

class Sudoku_Solver:
    def __init__(self, sudoku_grid):
        logdebug("SUDOKU_SOLVER", "Storing sudoki grid", False)
        self.sudoku_grid = sudoku_grid


    def is_sudoku_valid(self):
        # logdebug("SUDOKU SOLVER", "Starting horizontal check...", False)
        for n in range(1, 10):
            for i in range(0, 9):
                nfoundhori = False
                nfoundvert = False
                for j in range(0, 9):
                    # logdebug("SUDOKU SOLVER", "Horizontally checking number = "+str(n)+" at position "+str(i)+","+str(j)+" = "+str(sudoku_grid[i][j]), False)
                    if self.sudoku_grid[i][j] == n:
                        if nfoundhori:
                            logdebug("SUDOKU SOLVER", "Issue found!! Sudoku is invalid.", False)
                            return False
                        else:
                            nfoundhori = True

                    # logdebug("SUDOKU SOLVER", "Vertically checking number = "+str(n)+" at position "+str(j)+","+str(i)+" = "+str(sudoku_grid[j][i]), False)
                    if self.sudoku_grid[j][i] == n:
                        if nfoundvert:
                            logdebug("SUDOKU SOLVER", "Issue found!! Sudoku is invalid.", False)
                            return False
                        else:
                            nfoundvert = True

        return True


    def analyze_sudoku(self):
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_grid[i][j] > 0:
                    count += 1
        logdebug("SUDOKU SOLVER", "Initial numbers found in sudoku = " + str(count), False)


    # def is_sudoku_completed(self, sudoku_grid):
    #     # small function to tell when to stop for solutions
    #     for i in range(0, 9):
    #         for j in range(0, 9):
    #             if sudoku_grid[i][j] == 0:
    #                 return False
    #     return True


    # def solve_sudoku(self, current_sudoku_grid, iteration_level):
    #     for i in range(0, 9):
    #         for j in range(0, 9):
    #             for t in range(1, 10):
    #                 if current_sudoku_grid[i][j] == 0:
    #                     current_sudoku_grid[i][j] = t
    #                     if is_sudoku_valid(current_sudoku_grid):
    #                         if is_sudoku_completed(current_sudoku_grid):
    #                             # sudoku is resolved (hopefully!), print it and get out
    #                             print('LVL'+str(iteration_level)+' SODUKU SOLUTION FOUND!')
    #                             print_sudoku_grid(current_sudoku_grid)
    #                             return True

    #                         print('LVL'+str(iteration_level)+' - assigning '+str(t)+' at position '+str(i)+','+str(j) + ' and restarting recursion')
    #                         il = iteration_level+1
    #                         if solve_sudoku(current_sudoku_grid, il):
    #                             # stop sudoku solving because an inner recursion has found a solution
    #                             return True

    #                     else:
    #                         print('LVL'+str(iteration_level)+' - possiility '+str(t)+' didnt work at position ' + str(i) + ',' + str(j))
    #                         current_sudoku_grid[i][j] = 0

    #     print('LVL'+str(iteration_level)+' - NO POSSIBILITY WORKED, BACKING OFF!!')
    #     # tell previous recursion that current has failed
    #     return False


    def print_sudoku_grid(self):
        logdebug("SUDOKU SOLVER", "Printing sudoku grid...", False)
        for i in range(0, 9):
            if (i == 3 or i == 6):
                print('')
            for j in range(0, 9):
                if (j == 3 or j == 6):
                    print(' ', end='')
                print(' %s' % self.sudoku_grid[i][j], end='')
            print('')
