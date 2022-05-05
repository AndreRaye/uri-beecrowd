# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    list = input().split()
    tam = len(list)
    msg = ""

    for j in range(0,tam):
        palavra = list[j]

        msg += palavra[0]

    print(msg)