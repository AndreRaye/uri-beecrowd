N = float(input())

if N > 0 and N <= 400.00:
    novo_salario = N + (N * 0.15)
    reajuste_salario = N * 0.15
    percentual = 15
    print("Novo salario: {0:.2f}".format(novo_salario))
    print("Reajuste ganho: {0:.2f}".format(reajuste_salario))
    print("Em percentual: {0} %".format(percentual))
    
elif N >= 400.01 and N <= 800.00:
    novo_salario = N + (N * 0.12)
    reajuste_salario = N * 0.12
    percentual = 12
    print("Novo salario: {0:.2f}".format(novo_salario))
    print("Reajuste ganho: {0:.2f}".format(reajuste_salario))
    print("Em percentual: {0} %".format(percentual))
    
elif N >= 800.01 and N <= 1200.00:
    novo_salario = N + (N * 0.10)
    reajuste_salario = N * 0.10
    percentual = 10
    print("Novo salario: {0:.2f}".format(novo_salario))
    print("Reajuste ganho: {0:.2f}".format(reajuste_salario))
    print("Em percentual: {0} %".format(percentual))
    
elif N >= 1200.01 and N <= 2000.00:
    novo_salario = N + (N * 0.07)
    reajuste_salario = N * 0.07
    percentual = 7
    print("Novo salario: {0:.2f}".format(novo_salario))
    print("Reajuste ganho: {0:.2f}".format(reajuste_salario))
    print("Em percentual: {0} %".format(percentual))
    
elif N > 2000.00:
    novo_salario = N + (N * 0.04)
    reajuste_salario = N * 0.04
    percentual = 4
    print("Novo salario: {0:.2f}".format(novo_salario))
    print("Reajuste ganho: {0:.2f}".format(reajuste_salario))
    print("Em percentual: {0} %".format(percentual))