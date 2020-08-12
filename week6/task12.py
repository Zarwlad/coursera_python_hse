class Student:
    s_name = ""
    grade = 0


def read_create_stud():
    s = input().split()
    stud = Student()
    stud.s_name = s[0]
    stud.grade = int(s[1])
    return stud


i = int(input())
studs = []

for k in range(i):
    student = read_create_stud()
    studs.append(student)

studs.sort(key=lambda x: x.grade, reverse=True)

for s in studs:
    print(s.s_name)
