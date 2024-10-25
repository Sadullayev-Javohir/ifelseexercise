"""Uchta son berilgan. Shu sonlarni kichigini aniqlovchi programma tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
num3 = int(input("Uchinchi sonni kiriting: "))

if (num1 < num2 and num2 < num3):
    print(f"{num3} katta")

elif (num1 > num2 and num2 > num3):
    print(f"{num1} katta")

else:
    print(f"{num2} katta")