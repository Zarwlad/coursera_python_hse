from sys import stdin
import copy


class Matrix:
    def __init__(self, list_lists=None):
        if list_lists is None:
            list_lists = []
        self.list_lists = copy.deepcopy(list_lists)

    def __str__(self):
        string = ""
        for s in self.list_lists:
            string += "\t".join(list(map(str, s)))
            if self.list_lists.index(s) != len(self.list_lists) - 1:
                string += "\n"
        return string

    def size(self):
        return len(self.list_lists), len(self.list_lists[0])


exec(stdin.read())
