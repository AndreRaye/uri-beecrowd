N = int(input())

for i in range(N):
    dld = input()
    pint = int(dld[0])
    sint = int(dld[2])
    
    if pint == sint:
        resultado = pint * sint
        print(resultado)
    elif dld[1].isupper():
        resultado = sint - pint
        print(resultado)
    else:
        resultado = pint + sint
        print(resultado)
