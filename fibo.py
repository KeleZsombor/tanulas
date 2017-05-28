x = 1
y = 0


for i in range(1, 10):
    x2 = x
    x = x + y
    y = x2
    print(x)