a = int(input())
c = 0
b = 1
mass = []
f = open('делители числа.txt', 'w')
while a != 1:
    for i in mass:
        if i == b:
            b = b+1
    while c == 0:
        if a % b == 0:
            c = 1
        else:
            b = b + 1
    a = a // b
    mass.append(b)
    print(b, ', ')
    f.write(str(b))
    f.write(' ')
f.close()
