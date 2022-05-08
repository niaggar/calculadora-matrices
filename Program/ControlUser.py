import enquiries
from time import sleep
from os import system

from Matrix.Matrix import Matrix


class UserControlMatrix:
    def __init__(self):
        pass


    def create_new_matrix(self) -> Matrix:
        """
        Create a new matrix with the rows, columns and values given by the user.
        """
        system('clear')

        name = input('Enter the name of the matrix: ').upper()
        rows = int(input('Enter the number of rows: '))
        columns = int(input('Enter the number of columns: '))
        
        newMatrix = Matrix(rows, columns, name)

        for i in range(rows):
            for j in range(columns):
                system('clear')
                newMatrix.print_matrix()

                value = float(input(f'Enter the value for row {i} and column {j}: \n>>>> '))
                newMatrix.matrix[i][j] = value

        sleep(0.5)
        system('clear')

        return newMatrix


    def edit_matrix(self, matrix: Matrix) -> Matrix:
        """
        Edit the values of the matrix.
        """
        system('clear')

        rows = matrix.rows
        columns = matrix.columns

        while True:
            system('clear')
            matrix.print_matrix()

            r = int(input('Enter the row: '))
            c = int(input('Enter the column: '))

            if r < 0 or r >= rows or c < 0 or c >= columns:
                print('Invalid row or column. Try again.')
                sleep(1)
                continue

            system('clear')
            matrix.print_matrix()

            value = float(input(f'Enter the new value for row {r} and column {c}: \n>>>> '))
            matrix.matrix[r][c] = value

            system('clear')
            matrix.print_matrix()

            if enquiries.confirm('Do you want to edit another value?'):
                continue
            else:
                break

        sleep(0.5)
        system('clear')

        return matrix