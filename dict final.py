n = int(input())
a = []
for i in range(0, n):
    a += [int(input())]

d = {}

for i, n in enumerate(a):
    if n in d:
        print(d[n])
    elif n not in d:
        d[n] = f(n)
        print(d[n])



