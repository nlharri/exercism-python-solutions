class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [map(lambda i: int(i), z) for z in [x.split(" ") for x in matrix_string.split("\n")]]

    def row(self, index):
        if (index < 1) or (index > len(self.matrix)):
            raise Exception("Row index out of range")
        return self.matrix[index-1]

    def column(self, index):
        pass


#y = [x.split(" ") for x in "1 2 3\n4 5 6\n7 8 9".split("\n")]
#[(int(y) for y in x.split(" ")) for x in "1 2 3\n4 5 6\n7 8 9".split("\n")]
#x.split(" ")
#[int(y)] for y in x.split(" ")
#y = [x.split(" ") for x in "1 2 3\n4 5 6\n7 8 9".split("\n")]
#q = [map(lambda i: int(i), z) for z in y]
#y = [x.split(" ") for x in "1 2 3\n4 5 6\n7 8 9".split("\n")]
#q = [map(lambda i: int(i), z) for z in [x.split(" ") for x in "1 2 3\n4 5 6\n7 8 9".split("\n")]]
