n = int(input())
sprl = [[0 for j in range(n)] for i in range(n)]
s = 0
string = 0
column = 0
k = n
while s < n ** 2:
    for i in range(k):
        s += 1
        sprl[string][column] = s
        column += 1
    string += 1
    column -= 1

    for i in range(k-1):
        s += 1
        sprl[string][column] = s
        string += 1
    string -= 1
    column -= 1

    for i in range(k-1):
        s += 1
        sprl[string][column] = s
        column -= 1
    string -= 1
    column += 1

    for i in range(k-2):
        s += 1
        sprl[string][column] = s
        string -= 1
    string += 1
    column += 1
    k -= 2


for i in range(0, n):
    print(' ')
    for j in range(0, n):
        print(sprl[i][j], end=' ')