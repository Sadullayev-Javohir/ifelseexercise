"""A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa, A va B o'zgaruvchilari ularning
yig'indisini o'zlashtirsin. Agar teng bo'lsa, 0 ni o'zlashtirsin. A va B ning qiymati ekranga chiqarilsin."""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))

if (A != B):
    A = A + B
    B = A
elif (A == B):
    A = 0
    B = A

print(f"A = {A}")
print(f"B = {B}")