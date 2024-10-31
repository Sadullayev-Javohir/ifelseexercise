"""A, B, C haqiqiy sonlari berilgan. Agar berilgan sonlar o'sish tartibida berilgan bo'lsa, sonlarni ikkilantiring,
aks holda sonlarni ishorasi o'zgartirilsin. A, B, C ning qiymatlari ekranga chiqarilsin."""

A = int(input("A ning qiymatini kiriting: "))
B = int(input("B ning qiymatini kiriting: "))
C = int(input("C ning qiymatini kiriting: "))

if (A < B < C):
    A = A * 2
    B = B * 2
    C = C * 2
else:
    A = -A
    B = -B
    C = -C
    
print(f"A ning qiymati = {A}")
print(f"B ning qiymati = {B}")
print(f"C ning qiymati = {C}")