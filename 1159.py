while(True):
    p = 0

    x = int(input())
    if x == 0:
        break
        
    if x % 2 != 0:
        x = x + 1

    for i in range(1, 6):
        p = p + x
        x = x + 2

    print(p)