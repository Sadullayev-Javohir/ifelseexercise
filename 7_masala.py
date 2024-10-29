"""Ikkita butun son berilgan. Shu sonlarning kichigini tartib raqamini aniqlovchi programma tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))

if (num1 < num2):
    print(f"{num1} sonning tartib raqami = 1")
elif (num1 > num2):
    print(f"{num2} sonning tartib raqami = 2")
else: 
    print(f"Ikkalasi teng")