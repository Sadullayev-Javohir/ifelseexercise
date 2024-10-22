"""A va B haqiqiy son berilgan. Shu sonlarni shunday o'zgartirish kerakki, A son kichik B son katta bo'lsin
. A va B ning qiymati ekranga chiqarilsin."""

A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))

if A > B:
    A, B = B, A
    print(A)
    print(B)
else:
    print("Error")
