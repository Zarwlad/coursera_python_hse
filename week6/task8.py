class Man:
    name = ""
    s_name = ""
    school = 0
    mark = 0


def create_man(a):
    a = str(a).split()
    man = Man()
    man.name = a[1]
    man.s_name = a[0]
    man.school = int(a[2])
    man.mark = int(a[3])
    return man


def get_s_name(man):
    return man.s_name


file = open("input.txt", "r", encoding="utf8")

t = file.readlines()

mans = []

for a in t:
    mans.append(create_man(a))

mans.sort(key=get_s_name)

file_w = open("output.txt", "w", encoding="utf8")

for m in mans:
    print(m.s_name, m.name, m.mark, file=file_w)
