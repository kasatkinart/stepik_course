n = int(input())
a = n // 1000  # первые три цифры
b = n % 1000  # вторые три цифры
c = a // 100 + (a % 100) // 10 + (a % 100) % 10  # addition first three digits
d = b // 100 + (b % 100) // 10 + (b % 100) % 10  # addition second three digits
if c == d:
    print('Счастливый')
else:
    print('Обычный')
