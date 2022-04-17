dias_str = input()
total_dias = int(dias_str)

anos = total_dias // 365
meses = (total_dias % 365) // 30
dias =  (total_dias % 365) % 30


print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")