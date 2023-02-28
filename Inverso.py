
string = "sistema"

#FORMA 1
print(string[::-1])

#FORMA 2
for x in range(1, len(string)):
    print(string[-x], end='')
print(string[-len(string)])