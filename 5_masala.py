"""Uchta butun son berilgan. Shu sonlar orasida nechta musbat va manfiy son borligini aniqlovchi programma
tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
num3 = int(input("Uchinchi sonni kiriting: "))

if (num1 > 0 and num2 > 0 and num3 > 0):
    print("3 ta musbat son")
if (num1 < 0 and num2 > 0 and num3 > 0) or (num1 > 0 and num2 < 0 and num3 > 0) or (num1 > 0 and num2 > 0 and num3 < 0):
    print("2 ta musbat va 1 ta manfiy son")
if (num1 > 0 and num2 < 0 and num3 < 0) or (num1 < 0 and num2 > 0 and num3 < 0) or (num1 < 0 and num2 < 0 and num3 > 0):
    print("1 ta musbat va 2 t amanfiy son")
if (num1 < 0 and num2 < 0 and num3 < 0):
    print("3 ta manfiy son")