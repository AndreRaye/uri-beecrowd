x = int(input())

if x % 2 == 0:
    x = x + 1
    
for i in range(1,7):
    if x % 2 != 0:
        print(x)
        x = x + 2
