# l = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] % 2 != 0:
            del l[i]
        elif l[i] % 2 == 0:
            l[i] = int(l[i]/2)
    return

# print(l)

