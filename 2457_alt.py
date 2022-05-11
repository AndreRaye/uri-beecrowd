letra = input()
frase = input().split()
index = 0
qb = 0
qt = 0

for i in range(len(frase)):
    for j in (frase[index]):
        if j == letra:
            qb += 1
            qt += 1
        else:
            qt += 1
    index += 1
        
quociente = qb / qt
porcentagem = quociente * 100

print('{0:.1f}'.format(porcentagem))