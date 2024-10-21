"""Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshiring. aks holda 2 ga kamaytiring.
Hosil bo'lgan sonni ekranga chiqaruvchi programma tuzilsin."""

num = int(input("Son kiriting: "))

if num > 0:
    num += 1
else:
    num -= 2
    
print(num)