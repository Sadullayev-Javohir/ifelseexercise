"""Uchta butun son berilgan. Shu sonlarni ikkitasi o'zaro teng, qolgan bittasini tartib raqami aniqlansin."""

A = int(input("A ning qiymatini kiriting: "))
B = int(input("B ning qiymatini kiriting: "))
C = int(input("C ning qiymatini kiriting: "))

if A == B:
    print(f"{C} kichik son, tartib raqami - 3")
elif A == C:
    print(f"{B} kichik son, tartib raqami - 2")
elif B == C:
    print(f"{A} kichik son, tartib raqami - 1")
else:
    print("Ikkita o'zaro son yo'q")