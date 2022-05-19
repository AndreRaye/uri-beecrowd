inteiros = 0
soma = 0

for i in range(6):
    n = float(input())
    if n > 0:
        inteiros += 1
        soma += n
        
soma = soma / inteiros

print("{} valores positivos".format(inteiros))
print("{:.1f}".format(soma))