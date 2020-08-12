class Student:
    num = 0
    langs = {}


a = int(input())

studs = []

for b in range(a):
    s = Student()
    s.num = int(input())
    s.langs = set()
    for sa in range(s.num):
        s.langs.add(str(input()))
    studs.append(s)

unique_langs = set()
all_known = set()

for s in studs:
    unique_langs |= s.langs
    if studs.index(s) == 0:
        all_known |= s.langs
    else:
        all_known &= s.langs

print(len(all_known))
for a in all_known:
    print(a)
print(len(unique_langs))
for a in unique_langs:
    print(a)
