n = int(input())
sprl = [[0 for j in range(n)] for i in range(n)]
s = 0
string = 0
column = 0
# while s < n ** 2:
while column < n:
    s += 1
    sprl[string][column] = s
    column += 1
string += 1
column -= 1
print(string, column, s)

while string < n:
    s += 1
    sprl[string][column] = s
    string += 1
string -= 1
column -= 1
print(string, column, s)

while column >= 0:
    s += 1
    sprl[string][column] = s
    column -= 1
string -= 1
column += 1
print(string, column, s)



for i in range(0, n):
    print(' ')
    for j in range(0, n):
        print(sprl[i][j], end=' ')