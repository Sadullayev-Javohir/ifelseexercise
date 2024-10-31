"""A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa, A va B sonlarning
kattasini o'zlashtirsin. Agar teng bo'lsa, 0 ni o'zlashtirsin.
A va B ning qiymati ekranga chiqarilsin."""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))

if (A != B):
    
    if (A > B):
        B = A
    else:
        A = B
else:
    pass    
print(f"A = {A}, B = {B}")