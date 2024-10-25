"""Uchta son berilgan. Shu sonlarning yig'indisini eng katta bo'ladigan ikkitasini ekranga chiqaruvchi programma
tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
num3 = int(input("Uchinchi sonni kiriting: "))

if (num1 + num2 > num2 + num3):
    print(num1 + num2)
elif(num2 + num3 > num1 + num2):
    print(num2 + num3)
else:
    print(num1 + num3)