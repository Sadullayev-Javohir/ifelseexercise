"""Uchta butun son berilgan. Shu sonlarni o'rtachasi (ya'ni katta va kichik sonlar orasidagi son) ni aniqlovchi
programma tuzilsin."""

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print(f"o'rtacha son = {a}")
    
elif (b >= a and b <= c) or (b <= a and b >= c):
    print(f"o'rtacha son = {b}")

else:
    print(f"o'rtacha son = {c}")