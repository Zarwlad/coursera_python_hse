string = str(input())

first_word = string[:string.find(" ") + 1]
string = string.replace(first_word, "")
string = string + " " + first_word[:len(first_word) - 1]
print(string)
