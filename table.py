# a = [input().split()]
# while ['end'] not in a:
#     a += [input().split()]
a = [[9, 5, 3], [0, 7, -1],[-5, 2, 9], ['end']]
del a[-1]
print(a)
# b = []
# print(len(a))
# print(len(a[0]))
for i in range(0, len(a)-1):
    for j in range(0, len(a[0])-1):
        s = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ai = i + di
                aj = j + dj
                if ai-aj == 1 or aj - ai ==1:
                # print(ai, end=' ')
                # print(aj, end=' ')
                # print(s)
                    s = s + int(a[ai][aj])
                    print(s, end=' ')



















