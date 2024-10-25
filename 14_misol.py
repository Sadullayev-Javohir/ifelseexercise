""""Uchta son berilgan. Shu sonlarni avval kichigini keyin kattasini ekranga chiqaruvchi programma tuzilsin."""

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
num3 = int(input("Uchinchi sonni kiriting: "))

if (num1 < num2 and num1 < num3):
    print(num1)
    if (num1 < num2 and num2 > num3):
        print(num2)
    else:
        print(num3)
elif (num2 < num1 and num2 < num3):
    print(num2)
    if (num2 < num1 and num1 < num3):
        print(num3)
    else:
        print(num1)
else:
    print(num3)
    if (num3 < num2 and num2 < num1):
        print(num1)
    else:
        print(num2)