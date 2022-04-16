A, B, C, D = input().split()

fA = float(A)
fB = float(B)
fC = float(C)
fD = float(D)

fA = fA * 2
fB = fB * 3
fC = fC * 4

M = (fA + fB + fC + fD)/10

print("Media: {0:.1f}".format(M))

if M >= 7:
    print("Aluno aprovado.")
elif M < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {0:.1f}".format(exame))
    eM = (M + exame)/2
    
    if eM >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {0:.1f}".format(eM))