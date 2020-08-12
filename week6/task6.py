n = int(input())
townsList = list(map(int, input().split()[:n]))
townsTuple = []
for i in range(n):
    townsTuple.append((townsList[i], i))
m = int(input())
shelterList = list(map(int, input().split()[:m]))
shelterTuple = []
for i in range(m):
    shelterTuple.append((shelterList[i], i))
townsShelters = []
townsTuple.sort()
shelterTuple.sort()
currentTown = 0
for i in range(m):
    if i == m - 1:
        while currentTown < n:
            townsShelters.append((shelterTuple[i][1] + 1,
                                  townsTuple[currentTown][1]))
            currentTown += 1
    else:
        bound = shelterTuple[i][0] + shelterTuple[i + 1][0]
        while (currentTown < n) and (2 * townsTuple[currentTown][0] <= bound):
            townsShelters.append((shelterTuple[i][1] + 1,
                                  townsTuple[currentTown][1]))
            currentTown += 1


def second(mytuple):
    return mytuple[1]


townsShelters.sort(key=second)
answer = ''
for item in townsShelters:
    answer += str(item[0]) + ' '
print(answer[:-1])
