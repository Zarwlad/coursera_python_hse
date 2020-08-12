from sys import stdin
import copy


class Matrix:
    def __init__(self, ll=None):
        if ll is None:
            ll = []
        self.ll = copy.deepcopy(ll)

    def __str__(self):
        string = ""
        for s in self.ll:
            string += "\t".join(list(map(str, s)))
            if self.ll.index(s) != len(self.ll) - 1:
                string += "\n"
        return string

    def __add__(self, other):
        new_dim = []
        for row in range(len(self.ll)):
            new_dim.append([*map(sum, zip(self.ll[row], other.ll[row]))])
        return Matrix(new_dim)

    def __mul__(self, alpha):
        new_dim = []
        for line in self.ll:
            new_dim.append([*map(lambda x: x * alpha, line)])
        return Matrix(new_dim)

    __rmul__ = __mul__

    def size(self):
        return len(self.ll), len(self.ll[0])


exec(stdin.read())
