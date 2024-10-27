"""1-999 oraliqdagi sonlar berilgan. Berilgan sonni ikki xonali juft son, uch xonali toq son va x.k ekranga yozadigan
programma tuzilsin."""

num = int(input("Son kiriting: "))

if (num > 0 and num <= 9):
    if(num % 2 == 0):
        print(f"{num} bir xonali juft son")
    else:
        print(f"{num} bir xonali toq son")

elif (num > 0 and num <= 99):
    if(num % 2 == 0):
        print(f"{num} ikki xonali juft son")
    else:
        print(f"{num} ikki xonali toq son")

else:
    if (num % 2 == 0 and num <= 999):
        print(f"{num} Uch xonali juft son")
    elif (num % 2 == 1 and num <= 999):
        print(f"{num} Uch xonali toq son")