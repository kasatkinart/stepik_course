n = int(input())

games = 0
a = []
while games < n:
    a.append(input().split(';'))
    games += 1

d = {}

for i in range(0, n):
    for j in (0, 2):
        if a[i][j] in d:
            continue
        elif a[i][j] not in d:
            d[a[i][j]] = [0]*5
    d[a[i][0]][0] += 1
    d[a[i][2]][0] += 1
    if int(a[i][1]) > int(a[i][3]):
        d[a[i][0]][1] += 1
        d[a[i][0]][4] += 3
        d[a[i][2]][3] += 1
    elif int(a[i][1]) == int(a[i][3]):
        d[a[i][0]][2] += 1
        d[a[i][2]][2] += 1
        d[a[i][0]][4] += 1
        d[a[i][2]][4] += 1
    elif int(a[i][1]) < int(a[i][3]):
        d[a[i][0]][3] += 1
        d[a[i][2]][4] += 3
        d[a[i][2]][1] += 1


for q, w in d.items():
    print((q+':'), *w, end='\n')






