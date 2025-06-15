a, b = 0, 1
while True:
    print(a)
    a, b = b, a + b
    if a > 500:
        print(a)   
        break