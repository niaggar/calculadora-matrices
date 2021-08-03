from Matrix.Matrix import Matrix


class Identity(Matrix):

    def __init__(self, rows):
        super().__init__(rows, rows)
        self.set_identity()


    def set_identity(self):
        for row in range(len(self.matrix)):
            self.matrix[row][row] = 1
