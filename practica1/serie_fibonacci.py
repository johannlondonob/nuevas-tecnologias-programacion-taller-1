def fibonacci():
    a = 0
    b = 1
    c = 0
    for i in range(6):
        a = b
        b = c
        c = a + b
        print(c)


fibonacci()
