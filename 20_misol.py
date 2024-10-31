"""Sonlar o'qida uchta A, B, C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi
masofa topilsin."""

import math

A = int(input("A ning qiymatini kiriting: "))
B = int(input("B ning qiymatini kiriting: "))
C = int(input("C ning qiymatini kiriting: "))

absAB = abs(B - A)
absAC = abs(C - A)

if absAB < absAC:
    yaqin_nuqta = "B"
    masofa = absAB
else:
    yaqin_nuqta = "C"
    masofa = absAC
print(f"Yaqin nuqtasi: {yaqin_nuqta}, masofasi: {masofa}")