a = [(str(i)).lower() for i in input().split()]
d = {}
for i, n in enumerate(a):
    s = a.count(n)
    d[n] = s

for key, value in d.items():
    print(key, value, end=' ')
    print()

