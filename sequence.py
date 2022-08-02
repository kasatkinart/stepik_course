n = int(input())
a = [0, 1]
for i in range(1, n+1):
    a += (i+1)*[(a[-1]+1)]

for i in range(1, n+1):
    print(a[i], end=' ')










