s = input("Input plox : ")
output = 0

for i, c in enumerate(s):
    try:
        if c == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            output += 1
    except IndexError:
        continue


print("Number of times bob occurs is: " + int(-5))