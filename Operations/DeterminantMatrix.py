import copy


m = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 5],
]


def determinant(matrix):
    e1 = matrix[0][0]
    e2 = matrix[0][1]
    e3 = matrix[1][0]
    e4 = matrix[1][1]

    return e1 * e4 - e2 * e3


def calc_det(matrix):
    if len(matrix[0]) == 2:
        return determinant(matrix)
    
    else:
        det = 0
        for column in range(len(matrix[0])):
            m = copy.deepcopy(matrix)
            m.pop(0)

            for row in range(len(m)):
                m[row].pop(column)
            
            print(column)
            print("new" + str(m))
            print("old" + str(matrix))

            det += ((-1) ** column) * matrix[0][column] * calc_det(m)
        return det


a = calc_det(m)

print(a)
