"""Ikkita butun son berilgan. Shu sonlarning kattasini aniqlovchi programma tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))

if (num1 > num2):
    print(f"{num1} <=> {num1} > {num2}")
else:
    print(f"{num2} <=> {num2} > {num1}")