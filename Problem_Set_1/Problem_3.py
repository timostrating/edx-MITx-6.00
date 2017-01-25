s = input("Input plox : ")
output = 0
length = 0
text = ""

for i, c in enumerate(s):
    length = 1
    index = i
    curText = c

    while len(s) - 1 > index:
        if ord(s[index]) <= ord(s[index + 1]):
            length += 1
            index += 1
            curText += s[index]

        else:
            break

    if output < length:
        output = length
        text = curText

print("Longest substring in alphabetical order is: " + text)
