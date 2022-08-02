# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)

# a = [int(i) for i in input().split()]
# s=0
# for i in range(0, len(a)):
#     s=s+a[i]
# print(s)
# a = [int(i) for i in input().split()]
# for i in range(0, len(a)):
#     if len(a) == 1:
#         print(a[i])
#     elif i!= len(a)-1:
#         print(a[i-1]+a[i+1], end=' ')
#     elif i == len(a)-1:
#         print(a[i - 1] + a[0])

# a = [int(i) for i in input().split()]
# b = []
# for i in range(0, len(a)):
#     if a.count(a[i])>=2:
#         if a[i] not in b:
#             b.append(a[i])
#         else:
#             continue
#     continue
#
# for i in range(0, len(b)):
#     print(b[i], end=' ')

# a = [int(i) for i in input().split()]
# m = a[0]
# for i in range(1, len(a)):
#     if a[i]<m:
#         m = a[i]
#     else:
#         continue
# print(m)

# a = [int(i) for i in input().split()]
# m = a[0]
# for x in a:
#     if m > x:
#         m = x
# print(m)

n, m, k = (int(i) for i in input().split()) #  число строк, столбцов, мин
a = [[0 for j in range(m)] for i in range(n)]
print(a) #  следить за списком
for i in range(k):
    row, col = (int(i)-1 for i in input().split())
    a[row][col] = -1
print(a) #  следить за списком

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] = a[i][j] + 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()













