from Matrix.Matrix import Matrix


def __calculate_cell(i, j, mA, mB):
    cA = [e for e in mA[i]]
    cB = [e[j] for e in mB]

    return sum([eA * eB for eA, eB in zip(cA, cB)])


def multiply_matrix(matrix_a: Matrix, matrix_b: Matrix):
    aN = len(matrix_a.matrix[0])
    aM = len(matrix_a.matrix)

    bN = len(matrix_b.matrix[0])
    bM = len(matrix_b.matrix)

    if not aN == bM:
        print('Tha matrix can\'t be multiplied')
        return

    matrix_result = Matrix(aM, bN)
    for i, row in enumerate(matrix_result.matrix):
        for j, col in enumerate(row):
            matrix_result.matrix[i][j] = __calculate_cell(i, j, matrix_a.matrix, matrix_b.matrix)

    return matrix_result


