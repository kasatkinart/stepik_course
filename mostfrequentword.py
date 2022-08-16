with open('dataset_3363_3.txt') as inputFile:
    a = []
    c = ''
    for line in inputFile:
        line = line.strip().lower()
        c += line

a = c.split()

d = ''
f = {}
for i, n in enumerate(a):
    s = a.count(n)
    f[n] = s

s = sorted(f.values(), reverse=True)
print(s)

m = []
for key, value in f.items():
    if f[key] == max(f.values()):
        m.append([key, value])

m = min(m)
print(m)
for i, n in enumerate(a):
    print(n, end=' ')










