run = 1
while run == 1:
        def add_monitor(target_value, speed_indicator, height):
        counter = 0
        while height < target_value:
            counter += 1
            height += speed_indicator
            if height < target_value:
                print("Поки не сягнули потрібного значення. Зараз значення: " + str(height))
            elif height >= target_value:
                print("Дочекались! Готово, значення: " + str(height) + ". Знадобилось " + str(counter) + " цикла(ів).")
    try:
        add_monitor(
            int(input("\nВведіть мінімальне цільове значення: ")),
            int(input("Введіть значення для кожного 'кроку': ")),
            int(input("Задайте початкове значення: ")))
    except ValueError:
        print("Камон, працюємо тільки з числами.")

a=int(input("Введите число A:"))
b=int(input("Введите максимальное значение цикла:"))
c=int(input("Введите шаг увеличения цикла:"))
def my_function(a,b,c):
    i=a
    while i<b:
        i += c
        if i<b:
            print("Значение :"+str(i)+ " Пока что нет")
        elif i>=b:
         print("Дождались! "+"A="+ str(i))

my_function(a,b,c)
