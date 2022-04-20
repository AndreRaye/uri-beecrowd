N = int(input())

anterior = 0
proximo = 1
soma = 1

for i in range(1, N):
    print(anterior, end=' ')
    soma = anterior + proximo
    anterior = proximo
    proximo = soma

print(anterior)