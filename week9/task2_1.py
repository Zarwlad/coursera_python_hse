from sys import stdin


class Matrix(list):
    def __init__(self, lst):
        self.lst = [line.copy() for line in lst]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.lst])

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        new_dim = []
        for row in range(len(self.lst)):
            new_dim.append([*map(sum, zip(self.lst[row], other.lst[row]))])
        return Matrix(new_dim)

    def __mul__(self, alpha):
        new_dim = []
        for line in self.lst:
            new_dim.append([*map(lambda x: x * alpha, line)])
        return Matrix(new_dim)

    __rmul__ = __mul__


exec(stdin.read())
