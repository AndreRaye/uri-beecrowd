strA, strB, strC = input().split()

A = float(strA)
B = float(strB)
C = float(strC)

pi = 3.14159

triangulo = (A * C)/2
circulo = (C ** 2) * pi
trapezio = ((A + B) * C ) / 2
quadrado = B ** 2
retangulo = A * B

print("TRIANGULO:", "{0:.3f}".format(triangulo))
print("CIRCULO:", "{0:.3f}".format(circulo))
print("TRAPEZIO:", "{0:.3f}".format(trapezio))
print("QUADRADO:", "{0:.3f}".format(quadrado))
print("RETANGULO:", "{0:.3f}".format(retangulo))