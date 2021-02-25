a23 = input().split(' ')
a12 = int(a23[0])
a34 = int(a23[1])
a = list(range(1, a12 + 1))
i = int(1)
c12 = [0 , 1]
while i <= a34:
    с12 = input().split(' ')
    c = int(c12[0])
    d = int(c12[1])
    print(c, d,)
    a1 = a.index(c) + 1
    a2 = a.index(d) + 1
    k = a[a2]
    a[a2-1] = [a1]
    a[a1-1] = k
for elem in a: 
    print (elem)
