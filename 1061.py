str1, dia1 = input().split()
hh1,mm1,ss1 = input().split(sep=":")

str2, dia2 = input().split()
hh2,mm2,ss2 = input().split(sep=":")

dia1 = int(dia1)
dia2 = int(dia2)
hh1 = int(hh1)
hh2 = int(hh2)
mm1 = int(mm1)
mm2 = int(mm2)
ss1 = int(ss1)
ss2 = int(ss2)

dia1 = dia1 * 86400
dia2 = dia2 *86400

hh1 = hh1 * 3600
hh2 = hh2 * 3600

mm1 = mm1 * 60
mm2 = mm2 * 60

segundos_totais1 = dia1 + hh1 + mm1 + ss1
segundos_totais2 = dia2 + hh2 + mm2 + ss2
segundos_finais = segundos_totais2-segundos_totais1

w = 0
x = 0
y = 0
z = 0

while segundos_finais >= 86400:
    w = w + 1
    segundos_finais = segundos_finais - 86400

while segundos_finais >= 3600:
    x = x + 1
    segundos_finais = segundos_finais - 3600

while segundos_finais >= 60:
    y = y + 1
    segundos_finais = segundos_finais - 60
    
while segundos_finais > 0:
    z = z + 1
    segundos_finais = segundos_finais - 1

dia_final = dia2 - dia1 - 1

if w == 0 and x == 0 and y == 0 and z == 0:
    y = y + 1

print("{0} dia(s)".format(w))
print("{0} hora(s)".format(x))
print("{0} minuto(s)".format(y))
print("{0} segundo(s)".format(z))