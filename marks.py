with open('dataset_3363_4.txt') as inputFile:
    a = []
    for line in inputFile:
        line = line.strip().split(';')
        a.append(line)

ouf = open('outputFile.txt', 'w')
avrg = ''
for i in range(0, len(a)):
    c = 0
    for j in range (1, len(a[i])):
        c += int(a[i][j])
    avrg = c/3 #  len(a[i]) - 1
    ouf.write(str(avrg))
    ouf.write('\n')


for j in range (1, len(a[0])):
    subjAvrg = 0
    for i in range(0, len(a)):
        subjAvrg += int(a[i][j])
    subject = subjAvrg/(len(a))
    print(subject, end=' ')
    ouf.write(str(subject))
    ouf.write(' ')

ouf.close()











