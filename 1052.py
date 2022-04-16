D = int(input())

while D < 0 or D > 12:
    D = int(input())

if D == 1:
    print("January")
elif D == 2:
    print("February")
elif D == 3:
    print("March")
elif D == 4:
    print("April")
elif D == 5:
    print("May")
elif D == 6:
    print("June")
elif D == 7:
    print("July")
elif D == 8:
    print("August")
elif D == 9:
    print("September")
elif D == 10:
    print("October")
elif D == 11:
    print("November")
else:
    print("December")