with open('dataset_3363_2.txt', 'r') as inputFile:
    s = inputFile.readline().strip()
s = s + 'f'
a = []
for i in s:
    a.append(i)

f = ''
d = ''
ouf = open('outputFile.txt', 'w')
for i in range(0, len(a)):
    if 'A' <= a[i] <= 'Z' or 'a' <= a[i] <= 'z':
        f = a[i]
        continue
    elif '0' <= a[i] <= '9':
        d = d + a[i]
        i += 1
        if 'A' <= a[i] <= 'Z' or 'a' <= a[i] <= 'z':
            g = str(f*int(d))
            ouf.write(str(g))
            ouf.write('')
            f = ''
            d = ''
            i -= 1
        else:
            i -= 1
            continue

ouf.close()




































