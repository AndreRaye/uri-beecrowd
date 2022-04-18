from math import sqrt

strA, strB, strC = input().split()

A = float(strA)
B = float(strB)
C = float(strC)

if A == 0 or (B**2-4*A*C) < 0:
    print("Impossivel calcular")
else:
    d = (B**2)- (4*A*C)
    x1 = (-B + sqrt(d))/ (2*A)
    x2 = (-B - sqrt(d))/ (2*A)
    print("R1 =", "{0:.5f}".format(x1))
    print("R2 =", "{0:.5f}".format(x2))