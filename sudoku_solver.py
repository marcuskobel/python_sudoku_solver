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
        # logdebug("SUDOKU SOLVER", "Amount numbers found in sudoku = " + str(count), False)
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
        return True


    def solve_sudoku(self, iteration_level, lin, col):
        # main function that tries to solve sudoku
        if col == 8 and lin == 8:
            nextlin = 9
            nextcol = 9
        elif col == 8:
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

                    # logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" - assigning "+str(t)+" at position "+str(i)+","+str(j) + " and restarting recursion", False)
                    if self.tries % 20000 == 0:
                        logdebug("SUDOKU SOLVER", "# of tries = "+str(self.tries), False)
                        if self.tries % 100000 == 0:
                            self.print_sudoku_grid()

                    if self.solve_sudoku(iteration_level+1, nextlin, nextcol):
                        # stop sudoku solving because an inner recursion has found a solution
                        return True
                    else:
                        self.sudoku_grid[lin][col] = 0

                # else:
                    # logdebug("SUDOKU SOLVER", "LVL"+str(iteration_level)+" - possiility "+str(t)+" didnt work at position " + str(i) + "," + str(j), False)
                    # if num == 9:
            # if FOR loop reached end and haven't found a solution, goes back in the recursion
            # self.sudoku_grid[lin][col] = 0
            return False

        else:
            if self.solve_sudoku(iteration_level+1, nextlin, nextcol):
                # stop sudoku solving because an inner recursion has found a solution
                return True
            else:
                return False