<<<<<<< HEAD
a = float(input("Введіть мінімальне значення: "))
b = float(input("Введіть максимальне значення: "))
с = float(input("Введіть крок збільшення циклу: "))

def add_function(a, b, c):
    i = a
    while i < b:
        i += c
        if i < b:
            print("Значение: " + str(i) + "Поки що немає")
        elif i >= b:
            print("Дождались!Фінальный: " + str(i))



add_function(a, b, c)
=======
def add_function (a,b,c):
       i=a
       while i<b:
           i+=c
           if i<b:
              print("Значение: " +str(i)+ "Поки що немає")
           elif i>=b:
              print("Дождались!Фінальный: " +str(i))
     
a=float(input("Введіть мінімальне значення: "))
b=float(input("Введіть максимальне значення: "))
с=float(input("Введіть крок збільшення циклу: "))
add_function (a,b,c)
>>>>>>> 0243506bf6ef57d8b5f44544d1f26cebf7c59bcb
