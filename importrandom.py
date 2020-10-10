from random import randint
a =[randint(0, 9) for i in range (10)]
print ("Список: ", a)
b = int (input("ВВедіть цифру: "))
if b not in a:
    print ("Ваша цифра не входить в список")
else:
    print("Порядковий номер цифри: \n", a.index (b)+1)
