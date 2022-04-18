A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

p = 0
i = 0
m = 0
n = 0

if A % 2 == 0:
    p = p + 1
if B % 2 == 0:
    p = p + 1
if C % 2 == 0:
    p = p + 1
if D % 2 == 0:
    p = p + 1
if E % 2 == 0:
    p = p + 1

if A % 2 != 0:
    i = i + 1
if B % 2 != 0:
    i = i + 1
if C % 2 != 0:
    i = i + 1
if D % 2 != 0:
    i = i + 1
if E % 2 != 0:
    i = i + 1

if A > 0:
    m = m + 1
if B > 0:
    m = m + 1
if C > 0:
    m = m + 1
if D > 0:
    m = m + 1
if E > 0:
    m = m + 1

if A < 0:
    n = n + 1
if B < 0:
    n = n + 1
if C < 0:
    n = n + 1
if D < 0:
    n = n + 1
if E < 0:
    n = n + 1

print(p, "valor(es) par(es)")
print(i, "valor(es) impar(es)")
print(m, "valor(es) positivo(s)")
print(n, "valor(es) negativo(s)")