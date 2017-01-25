s = input("Input plox : ")
output = 0

for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        output += 1

print("Number of vowels: " + str(output))