def maiorepos():
    maior = 0
    pos = 0
    q = 0

    while q != 100:
        q += 1
        n = int(input())
        
        if n > maior:
            maior = n
            pos = q
    print(maior)
    print(pos)

maiorepos()