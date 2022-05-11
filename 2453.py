frase = input().split()
msg = ''
index = 0
space = False
Pp = True
for i in range(len(frase)):
    if space == True:
        msg += " "
    for j in (frase[index]):
        if (j == "P" or j == "p") and Pp == True:
            j = ""
            Pp = False
        else:
            msg += j
            Pp = True
    index += 1
    space = True
print(msg)