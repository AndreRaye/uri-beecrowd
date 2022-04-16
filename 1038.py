c, strQ = input().split()

q = int(strQ)

if c == str(1):
    T = (q * 4.00)
    print("Total: R$", "{0:.2f}".format(T))
elif c == str(2):
    T = (q * 4.50)
    print("Total: R$", "{0:.2f}".format(T))
elif c == str(3):
    T = (q * 5.00)
    print("Total: R$", "{0:.2f}".format(T))
elif c == str(4):
    T = (q * 2.00)
    print("Total: R$", "{0:.2f}".format(T))
else:
    T = (q * 1.50)
    print("Total: R$", "{0:.2f}".format(T))