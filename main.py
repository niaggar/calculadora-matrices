
"""

Matrix example
--> rows: 5
--> columns: 4

      0  1  2  3
0 - [ 0, 0, 0, 0 ]
1 - [ 0, 0, 0, 0 ]
2 - [ 0, 0, 0, 0 ]
3 - [ 0, 0, 0, 0 ]
4 - [ 0, 0, 0, 0 ]

"""


def print_matrix(matrix):
    str_matrix = f'{"-" * 15}\n'

    for r in matrix:
        row = ''
        for c in r:
            row += f'{c}  '
        str_matrix += f'{row}\n'

    str_matrix += f'{"-" * 15}\n'
    print(str_matrix)


def create_new_matrix(rows=0, columns=0, state=False):
    if state:
        rows, columns = (int(i) for i in input('Rows  -  Columns\n').split())

    new_matrix = []
    for r in range(rows):
        new_matrix.append([])

        for c in range(columns):
            if state:
                element = float(input(f'Row: {r} Column: {c}\n'))
            else:
                element = 0

            new_matrix[r].append(element)

    return new_matrix


def _calculate_cell(i, j, mA, mB):
    cA = [e for e in mA[i]]
    cB = [e[j] for e in mB]

    return sum([eA * eB for eA, eB in zip(cA, cB)])


def operation_multiply(matrix_a, matrix_b):
    aN = len(matrix_a[0])
    aM = len(matrix_a)

    bN = len(matrix_b[0])
    bM = len(matrix_b)

    if not aN == bM:
        print('Tha matrix can\'t be multiplied')
        return

    matrix_result = create_new_matrix(rows=aM, columns=bN)

    for i, row in enumerate(matrix_result):
        for j, col in enumerate(row):
            matrix_result[i][j] = _calculate_cell(i, j, matrix_a, matrix_b)

    return matrix_result


def main():
    a = create_new_matrix(state=True)
    b = create_new_matrix(state=True)

    print_matrix(a)
    print_matrix(b)

    ab = operation_multiply(a, b)

    print_matrix(ab)


if __name__ == '__main__':
    main()
