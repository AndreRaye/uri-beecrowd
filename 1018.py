D = int(input())

C = 0
cc = 0
v = 0
d = 0
c = 0
dd = 0
u = 0

print(D)

while D >= 100:
    D -= 100
    C += 1

while D >= 50:
    D -= 50
    cc += 1

while D >= 20:
    D -= 20
    v += 1

while D >= 10:
    D -= 10
    d += 1

while D >= 5:
    D -= 5
    c += 1

while D >= 2:
    D -= 2
    dd += 1

while D >= 1:
    D -= 1
    u += 1

print(C, "nota(s) de R$ 100,00")
print(cc, "nota(s) de R$ 50,00")
print(v, "nota(s) de R$ 20,00")
print(d, "nota(s) de R$ 10,00")
print(c, "nota(s) de R$ 5,00")
print(dd, "nota(s) de R$ 2,00")
print(u, "nota(s) de R$ 1,00")