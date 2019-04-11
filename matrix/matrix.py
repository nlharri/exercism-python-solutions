class Matrix(object):
    def __init__(self, matrix_string):
        # build matrix of integers
        matrix_of_strings = [s.split(" ") for s in matrix_string.split("\n")]
        self.matrix = []
        for i in range(len(matrix_of_strings)):
            self.matrix.append([int(j) for j in matrix_of_strings[i]])
        # build transposed matrix
        self.transposed_matrix = []
        for j in range(len(self.row(1))):
            self.transposed_matrix.append([])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.transposed_matrix[j].append(self.matrix[i][j])

    def row(self, index):
        if (index < 1) or (index > len(self.matrix)):
            raise Exception("Row index out of range")
        return list(self.matrix[index-1])

    def column(self, index):
        if (index < 1) or (index > len(self.transposed_matrix)):
            raise Exception("Column index out of range")
        return self.transposed_matrix[index-1]
