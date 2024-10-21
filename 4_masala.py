"""Uchta butun son berilgan. Shu sonlar orasidan nechta musbat son borligini aniqlovchi programma tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
num3 = int(input("Uchinchi sonni kiriting: "))

if (num1 > 0 and num2 > 0 and num3 > 0):
    print("Uchta musbat son")

if (num1 < 0 and num2 > 0 and num3 > 0) or (num1 > 0 and num2 < 0 and num3 > 0) or (num1 > 0 and num2 > 0 and num3 < 0):
    print("ikkita musbat son")

elif (num1 < 0 and num2 < 0 and num3 > 0) or (num1 < 0 and num2 > 0 and num3 < 0) or (num1 > 0 and num2 < 0 and num3 < 0):
    print("bitta musbat son")

if (num1 < 0 and num2 < 0 and num3 < 0):
    print("Musbat son yo'q") 