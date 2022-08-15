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

print(f)








