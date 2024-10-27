"""Butun son berilgan. Berilgan sonni musbat toq son, manfiy juft son, son nolga teng va x.k ekranga yozadigan programma
tuzilsin."""

num = int(input("Son kiriting: "))

if (num % 2 == 1):
    if (num > 0):
        print(f"{num} musbat toq son")
    else:
        print(f"{num} manfiy toq son")

elif (num == 0):
    print(f"{num} == 0 ga teng")
    
else:
    if (num > 0):
        print(f"{num} musbat juft son")
    elif (num < 0):
        print(f"{num} manfiy juft son")

