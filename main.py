
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

from Matrix.Matrix import Matrix
from Matrix.Identity import Identity

from Operations.MultiplyMatrix import multiply_matrix
from Operations.MultiplyNumber import multiply_number


if __name__ == '__main__':
    m1 = Matrix(3, 2, 5)
    m2 = Matrix(2, 3, 8)

    r1 = multiply_matrix(m1, m2)
    r2 = multiply_number(m1, 4)

    m3 = Identity(5)

    print('Matrix one')
    m1.print_matrix()

    print('Matrix tree')
    m3.print_matrix()


    print('Matrix r1')
    r1.print_matrix()

    print('Matrix r2')
    r2.print_matrix()

