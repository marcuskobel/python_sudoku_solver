from common import *

class Sudoku_Solver:
    def __init__(self, sudoku_grid):
        # class contructor
        logdebug("SUDOKU_SOLVER", "Storing sudoku grid", False)
        self.sudoku_grid = sudoku_grid
        self.tries = 0


    def is_sudoku_valid(self):
        # check if current sudoku grid configuration is valid or not, uses full grid scans for all numbers
        for n in range(1, 10):
            for i in range(0, 9):
                nfoundhori = False
                nfoundvert = False
                for j in range(0, 9):
                    if self.sudoku_grid[i][j] == n:
                        if nfoundhori:
                            return False
                        else:
                            nfoundhori = True

                    if self.sudoku_grid[j][i] == n:
                        if nfoundvert:
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

        if count == 81:
            logdebug("SUDOKU SOLVER", "SODUKU SOLUTION FOUND! Number of tries = "+str(self.tries), False)
            self.print_sudoku_grid()
        return count


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


    def check_if_number_works_at_position(self, number, line, column):
        # check if number is duplicated in both line and column
        for i in range(0, 9):
            # check for number duplication in line
            if self.sudoku_grid[line][i] == number:
                return False
            # check for number duplication in column
            if self.sudoku_grid[i][column] == number:
                return False

        # check for number duplication in the same 3x3 square
        for i in range( (line//3)*3, ((line//3)*3)+3 ):
            for j in range( (column//3)*3, ((column//3)*3)+3 ):
                if self.sudoku_grid[i][j] == number:
                    return False

        return True


    def solve_sudoku(self, iteration_level, lin, col):
        # main function that tries to solve sudoku

        # calculate next lin/col that will de resolved upfront
        if col == 8:
            nextlin = lin + 1
            nextcol = 0
        else:
            nextlin = lin
            nextcol = col + 1

        if self.sudoku_grid[lin][col] == 0:
            for num in range(1, 10):
                if self.check_if_number_works_at_position(num, lin, col):
                    self.tries += 1
                    self.sudoku_grid[lin][col] = num

                    # check if this number solved sudoku
                    if self.count_numbers_in_sudoku_grid() == 81:
                        # sudoku is resolved (hopefully!), print it and get out
                        return True

                    if self.tries % 20000 == 0:
                        logdebug("SUDOKU SOLVER", "# of tries = "+str(self.tries), False)
                        if self.tries % 100000 == 0:
                            self.print_sudoku_grid()

                    if self.solve_sudoku(iteration_level+1, nextlin, nextcol):
                        # stop sudoku solving because an inner recursion has found a solution
                        return True
                    else:
                        self.sudoku_grid[lin][col] = 0

            return False

        else:
            if self.solve_sudoku(iteration_level+1, nextlin, nextcol):
                # stop sudoku solving because an inner recursion has found a solution
                return True
            else:
                return False