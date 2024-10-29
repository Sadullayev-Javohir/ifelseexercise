"""Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshiring, agar manfiy bo'lsa 2 ga kamaytiring.
Agar 0 ga teng bo'lsa, 10 ni o'zlashtirsin. Hosil bo'lgan sonni ekranga chiqaruvchi programma tuzilsin."""

num = int(input("Son kiriting: "))

if num > 0:
    num += 1
elif num < 0:
    num -= 2
else:
    num = 10

print(num)