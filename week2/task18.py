a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

box1 = [a1, b1, c1]
box1.sort()

box2 = [a2, b2, c2]
box2.sort()

isA1Larger = False
isB1Larger = False
isC1Larger = False
isBoxesEq = False

if box1[2] == box2[2] and box1[1] == box2[1] and box1[0] == box2[0]:
    isBoxesEq = True

if not isBoxesEq and box1[2] >= box2[2]:
    isA1Larger = True

if box1[1] >= box2[1]:
    isB1Larger = True

if box1[0] >= box2[0]:
    isC1Larger = True

if isA1Larger and isB1Larger and isC1Larger:
    print("The first box is larger than the second one")
elif not isA1Larger and not isB1Larger and not isC1Larger:
    print("The first box is smaller than the second one")
elif isBoxesEq:
    print("Boxes are equal")
else:
    print("Boxes are incomparable")
