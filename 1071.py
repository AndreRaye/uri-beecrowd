x = int(input())
y = int(input())

if x == y:
    print(0)

else:
    if x < y:
        inicio = x
        fim = y
    else:
        inicio = y
        fim = x
    
    if inicio % 2 != 0:
        inicio += 2
    else:
        inicio += 1

    if fim % 2 != 0:
        fim -= 2
    else:
        fim -= 1

    soma = 0

    i = inicio
    while i <= fim:
        soma = soma + i
        i += 2

    print(soma)
