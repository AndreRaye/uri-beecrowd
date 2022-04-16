N1, strQ1, strV1 = input().split()
N2, strQ2, strV2 = input().split()

Q1 = int(strQ1)
Q2 = int(strQ2)
V1 = float(strV1)
V2 = float(strV2)

valor = (Q1 * V1) + (Q2 * V2)

print("VALOR A PAGAR: R$", "{0:.2f}".format(valor))