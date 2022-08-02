m = int(input())
a = [m]
s = a[0]
while s!= 0:
    a += [int(input())]
    s = s + a[-1]

sum = 0
for i in range(0, len(a)):
    sum = sum + (a[i])**2

print(sum)


# n = int(input())
# s = 0
# while n != 0:
#     s = s+n
#     n = int(input())
# print(s)










