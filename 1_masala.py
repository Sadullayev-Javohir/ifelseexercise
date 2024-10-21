"""Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshirilsin. aks holda o'zgartirilmasin.
Hosil bo'lgan sonni ekranga chiqaruvchi programma tuzilsin."""

num = int(input("Son kiriting: "))

if num > 0:
    num += 1
else:
    num = num

print(num)