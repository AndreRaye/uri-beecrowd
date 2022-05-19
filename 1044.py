a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    maior = a
    menor = b
elif b > a:
    maior = b
    menor = a
    
multiplo = maior % menor

if multiplo == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")