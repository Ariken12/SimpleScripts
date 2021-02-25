s = 1
a = int(input()) +1
for i in list(range(1, a)):
    s = s*i
print(s)
s = str(s)
b = input()
f = open('факториал.txt', 'w')
f.write(s)
f.close()
