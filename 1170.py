# -*- coding: utf-8 -*-

u = int(input())
dias = 0

for i in range(u):
    N = float(input())
    while N > 1:
        dias += 1
        N = N / 2
    else:
        print("{} dias".format(dias))
        dias = 0