strA, strB, strC = input().split()

maior = 0
meio = 0
menor = 0

strA = float(strA)
strB = float(strB)
strC = float(strC)

if strA > strB and strA > strC:
    maior = strA
    if strB > strC:
        meio = strB
        menor = strC
    else:
        meio = strC
        menor = strB

if strB > strA and strB > strC:
    maior = strB
    if strA > strC:
        meio = strA
        menor = strC
    else:
        meio = strA
        menor = strC

else:
    maior = strC
    if strA > strB:
        meio = strA
        menor = strB
    else:
        meio = strB
        menor = strA

A = float(maior)
B = float(meio)
C = float(menor)

if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")

    if A == B != C or A == C != B or C == B != A:
        print("TRIANGULO ISOSCELES")