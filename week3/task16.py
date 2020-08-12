string = str(input())

first = string.find("h")
sec = string.rfind("h") + 1

str_for_del = string[first:sec]

new_str = string.replace(str_for_del, "")

print(new_str)
