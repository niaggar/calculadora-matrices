from time import sleep
from os import system

from Matrix.Matrix import Matrix


class UserControlMatrix:
    def __init__(self):
        pass

    @staticmethod
    def create_new_matrix() -> Matrix:
        system('cls')

        name = input('Enter the name of the matrix: ').upper()
        rows = int(input('Enter the number of rows: '))
        columns = int(input('Enter the number of columns: '))

        new_matrix = Matrix(rows, columns, name)

        for i in range(rows):
            for j in range(columns):
                system('cls')
                new_matrix.print_matrix()

                value = float(input(f'Enter the value for row {i} and column {j}: \n>>>> '))
                new_matrix.matrix[i][j] = value

        sleep(0.5)
        system('cls')

        return new_matrix

    @staticmethod
    def edit_matrix(matrix: Matrix) -> Matrix:
        system('cls')

        rows = matrix.rows
        columns = matrix.columns

        while True:
            system('cls')
            matrix.print_matrix()

            r = int(input('Enter the row: '))
            c = int(input('Enter the column: '))

            if r < 0 or r >= rows or c < 0 or c >= columns:
                print('Invalid row or column. Try again.')
                sleep(1)
                continue

            system('cls')
            matrix.print_matrix()

            value = float(input(f'Enter the new value for row {r} and column {c}: \n>>>> '))
            matrix.matrix[r][c] = value

            system('cls')
            matrix.print_matrix()

            if False:
                continue
            else:
                break

        sleep(0.5)
        system('cls')

        return matrix
