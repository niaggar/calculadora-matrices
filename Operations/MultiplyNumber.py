from Matrix.Matrix import Matrix


def multiply_number(matrix_mult: Matrix, number: float):
    matrix_res = Matrix(matrix_mult.rows, matrix_mult.columns)

    for r in range(matrix_res.rows):
        for c in range(matrix_res.columns):
            matrix_res.matrix[r][c] = matrix_mult.matrix[r][c] * number

    return matrix_res
