strA, strB, strC = input().split()

A = int(strA)
B = int(strB)
C = int(strC)

maior = (A+B+abs(A-B))/2
maior = (C+maior+abs(C-maior))/2

print(int(maior), "eh o maior")