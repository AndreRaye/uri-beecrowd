A, B, C, D = input().split()

intA = int(A)
intB = int(B)
intC = int(C)
intD = int(D)

if intB>intC and intD>intA and (intC+intD)>(intA+intB) and intC>0 and intD>0 and intA % 2 ==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")