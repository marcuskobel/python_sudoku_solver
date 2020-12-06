from common import *

class Sudoku_Solver:
    def __init__(self, sudoku_grid):
        # class contructor
        logdebug("SUDOKU_SOLVER", "Storing sudoku grid", False)
        self.sudoku_grid = sudoku_grid
        self.tries = 0


    def is_sudoku_valid(self):
        # check if current sudoku grid configuration is valid or not
        # uses full grid scans for all numbers - very slow
        # logdebug("SUDOKU SOLVER", "Starting horizontal check...", False)
        for n in range(1, 10):
            for i in range(0, 9):
                nfoundhori = False
                nfoundvert = False
                for j in range(0, 9):
                    # logdebug("SUDOKU SOLVER", "Horizontally checking number = "+str(n)+" at position "+str(i)+","+str(j)+" = "+str(sudoku_grid[i][j]), False)
                    if self.sudoku_grid[i][j] == n:
                        if nfoundhori:
                            # logdebug("SUDOKU SOLVER", "Issue found!! Sudoku is invalid.", False)
                            return False
                        else:
                            nfoundhori = True

                    # logdebug("SUDOKU SOLVER", "Vertically checking number = "+str(n)+" at position "+str(j)+","+str(i)+" = "+str(sudoku_grid[j][i]), False)
                    if self.sudoku_grid[j][i] == n:
                        if nfoundvert:
                            # logdebug("SUDOKU SOLVER", "Issue found!! Sudoku is invalid.", False)
                            return False
                        else:
                            nfoundvert = True
        return True


    def count_numbers_in_sudoku_grid(self):
        # function to return how many numbers we have in sudoku
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_grid[i][j] > 0:
                    count += 1
        logdebug("SUDOKU SOLVER", "Amount numbers found in sudoku = " + str(count), False)


    def print_sudoku_grid(self):
        # function to print sudoku grid
        logdebug("SUDOKU SOLVER", "Printing sudoku grid...", False)
        for i in range(0, 9):
            if (i == 3 or i == 6):
                print('')
            for j in range(0, 9):
                if (j == 3 or j == 6):
                    print(' ', end='')
                print(' %s' % self.sudoku_grid[i][j], end='')
            print('')


    def is_sudoku_completed(self):
        #  function to tell when to stop searching for solutions
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_grid[i][j] == 0:
                    return False
        return True


    def check_if_number_works_at_position(self, number, line, column):
        # check if number is duplicated in both line and column
        for i in range(0, 9):
            # check for number duplication in line
            if self.sudoku_grid[line][i] == number:
                return False
            # check for number duplication in column
            if self.sudoku_grid[i][column] == number:
                return False
        return True


    def solve_sudoku(self, iteration_level):
        # main function that tries to solve sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_grid[i][j] == 0:
                    for t in range(1, 10):
                        if self.check_if_number_works_at_position(t, i, j):
                            self.sudoku_grid[i][j] = t
                            # check if this number solved sudoku
                            if self.is_sudoku_completed():
                                # sudoku is resolved (hopefully!), print it and get out
                                logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" SODUKU SOLUTION FOUND!", False)
                                self.print_sudoku_grid()
                                return True

                            # logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" - assigning "+str(t)+" at position "+str(i)+","+str(j) + " and restarting recursion", False)
                            self.tries += 1
                            if self.tries % 1000 == 0:
                                logdebug("SUDOKU SOLVER", "# of tries = "+str(self.tries), False)

                            if self.solve_sudoku(iteration_level+1):
                                # stop sudoku solving because an inner recursion has found a solution
                                return True
                            else:
                                self.sudoku_grid[i][j] = 0

                        # else:
                            # logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" - possiility "+str(t)+" didnt work at position " + str(i) + "," + str(j), False)
                            # self.sudoku_grid[i][j] = 0

        # logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" - NO POSSIBILITY WORKED, BACKING OFF ON RECURSION!!", False)
        # tell previous recursion that current has failed and it must move to next number
        return False