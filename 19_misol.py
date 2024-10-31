"""To'rtta butun son berilgan. Shu sonlarni uchtasi o'zaro teng, qolgan bittasini tartib 
raqami aniqlansin."""

A = int(input("A ning qiymatini kiriting: "))
B = int(input("B ning qiymatini kiriting: "))
C = int(input("C ning qiymatini kiriting: "))
D = int(input("D ning qiymatini kiriting: "))

if (B == C and C == D):
    print(f"{A}, tartib raqmi - 1")
elif (A == C and C == D):
    print(f"{B}, tartib raqmi - 2")
elif (A == B and B == D):
    print(f"{C}, tartib raqmi - 3")
elif (A == B and B == C):
    print(f"{D}, tartib raqami - 4")
else:
    print("Uchta bir xil son kiriting")