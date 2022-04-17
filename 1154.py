def idades():
    
    n = int(input())
    q = 0
    aux = 0
    
    while n > 0:
        q = q + 1
        n = n + aux
        aux = n
        n = int(input())
           
    if n < 0:
        media = (aux/q)
        print("{0:.2f}".format(media))

idades()