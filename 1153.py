def fatorial():
    n = int(input())
    while n <= 0 or n >= 13:
        n = int(input())
    
    fat = 1
    i = 2
    
    while i <= n:
        fat = fat*i
        i = i + 1

    print(fat)

fatorial() 
