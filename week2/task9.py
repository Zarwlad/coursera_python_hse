inp = input()
intInp = int(inp)
lastNum = int(str(inp)[-1])

if 10 <= intInp <= 20 or lastNum in [0, 5, 6, 7, 8, 9]:
    print(intInp, "korov")
elif lastNum == 1:
    print(intInp, "korova")
else:
    print(intInp, "korovy")
