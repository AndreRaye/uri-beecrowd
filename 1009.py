Nome = input()

fixo = float(input())
vendas = float(input())

total = (vendas * 0.15) + fixo

print("TOTAL = R$", "{0:.2f}".format(total))