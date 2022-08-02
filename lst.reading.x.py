a = [int(i) for i in input().split()]
x = int(input())
if x in a:
    for i, n in enumerate(a):
        if x == n:
            print(i, end=' ')
        else:
            continue
else:
    print('Отсутствует')




