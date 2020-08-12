inFile = open('input.txt', 'r', encoding='utf8')
a = str(inFile.read())

p_a = set(a.split())

print(len(p_a))
