letra = input()
frase = input().split()

index = -1

qp = len(frase)
qpl = 0
    
for i in range(qp):
    index += 1
    for j in (frase[index]):
        if j == letra:
            qpl += 1
            break


        
quociente = qpl / qp
porcentagem = quociente * 100

print('{0:.1f}'.format(porcentagem))
print(frase)