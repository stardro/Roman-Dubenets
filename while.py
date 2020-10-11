def add_function (a,b,c):
       i=a
       while i<b:
           i+=c
           if i<b:
              print("Значение: " +str(i)+ "Пока що немає")
           elif i>=b:
              print("Дождались!Фінальный: " +str(i))
       try:
         add_function(
              a=float(input("Введіть мінімальне значення: ")),
              b=float(input("Введіть максимальне значення: ")),
              с=float(input("Введіть крок збільшення циклу: ")))
       except Error:
          print("Працюємо тільки з числами.")
