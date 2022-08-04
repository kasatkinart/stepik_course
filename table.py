# a = [input().split()]
# while ['end'] not in a:
#     a += [input().split()]
a = [[9, 5, 3], [0, 7, -1],[-5, 2, 9], ['end']]
del a[-1]
print(a)
c = []
b = []
# print(len(a))
# print(len(a[0]))
s = 0
for i in range(0, len(a)):
    for j in range(0, len(a[0])):
        s = a[i-1][j] + a[(i+1)%(len(a))][j] + a[i][j-1] + a[i][(j+1)%(len(a[0]))]
        c += [s]
        print(s)
    print(c)
    b += [[c]]
    c = []

print(b)

        # for di in range(-1, len(a)-1):
        #     for dj in range(-1, 2):
        #         ai = i + di
        #         aj = j + dj
        #         if ai + aj - i - j == 1 or ai + aj - i - j == -1:
        #         # print(ai, end=' ')
        #         # print(aj, end=' ')
        #         # print(s)
        #             s = s + int(a[ai][aj])
        #         else:
        #             continue





















