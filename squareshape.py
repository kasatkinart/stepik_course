shape = (input())
if shape == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print(S)
elif shape == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
elif shape == 'круг':
    pi = 3.14
    a = float(input())
    S = pi*(a**2)
    print(S)
