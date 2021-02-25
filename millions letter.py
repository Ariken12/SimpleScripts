f = open('output.txt', 'w')
for i in range(10 ** 6):
    f.write(chr(i%128))
f.close()
