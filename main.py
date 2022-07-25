a = int(input())
b = int(input())
if b!=0:
    print(a / b)
else:
    print('Division by 0. Division is impossible!')
    b=int(input('Please enter non-zero number'))
    if b==0:
        print('You are idiot!')
    else:
        print(a / b)





