n = int(input())

games = 0
a = []
while games < n:
    a.append(input().split(';'))
    games += 1

# print(games)
# print(a)
# print(a[0][0])
d = {}

for i in range(0, n):
    for j in 0, 2:
        d[a[i][j]] = [0, 0, 0, 0, 0]

j = 0

for i in range(0, n):
        d[a[i][0]][0] += 1
        d[a[i][2]][0] += 1
        if a[i][1] < a[i][3]:
            d[a[i][0]][1] += 1
            d[a[i][0]][4] += 3
            d[a[i][2]][3] += 1
        elif a[i][1] == a[i][3]:
            d[a[i][0]][2] += 1
            d[a[i][2]][2] += 1
            d[a[i][0]][4] += 1
            d[a[i][2]][4] += 1
        elif a[i][1] > a[i][3]:
            d[a[i][2]][1] += 1
            d[a[i][2]][4] += 3
            d[a[i][0]][3] += 1


# print(d.items())

for q, w in d.items():
    print((q+':'), *w, end='\n')


# tableResult[a[i][0]] = [0, 0, 0, 0, 0]
# tableResult[a[i][2]] = [0, 0, 0, 0, 0]
# tableResult[a[i][0]][0] += 1
# tableResult[a[i][2]][0] += 1
# if a[i][1] > a[i][3]:
#     tableResult[a[i][0]][1] += 1
#     tableResult[a[i][0]][4] += 3
#     tableResult[a[i][2]][3] += 1
# elif a[i][1] == a[i][3]:
#     tableResult[a[i][0]][2] += 1
#     tableResult[a[i][2]][2] += 1
#     tableResult[a[i][0]][4] += 1
#     tableResult[a[i][2]][4] += 1
# elif a[i][1] < a[i][3]:
#     tableResult[a[i][2]][1] += 1
#     tableResult[a[i][2]][4] += 3
#     tableResult[a[i][0]][3] += 1