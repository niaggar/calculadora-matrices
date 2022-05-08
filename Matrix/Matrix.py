class Matrix:

    def __init__(self, rows, col, name='NEW_MATRIX', fill=0):
        self.rows = rows
        self.columns = col
        self.name = name
        self.matrix = self.create_matrix(fill)


    def create_matrix(self, fill):
        new_matrix = []
        for r in range(self.rows):
            new_matrix.append([])

            for c in range(self.columns):
                new_matrix[r].append(fill)

        return new_matrix


    def print_matrix(self):
        str_matrix = f'{"-" * self.columns * 6}\n'
        str_matrix += f'{self.name}\n'
        str_matrix += f'{"-" * self.columns * 6}\n'

        for r in self.matrix:
            row = ''
            for c in r:
                row += f'{c}  '
            str_matrix += f'{row}\n'

        str_matrix += f'{"-" * self.columns * 6}\n'
        print(str_matrix)
