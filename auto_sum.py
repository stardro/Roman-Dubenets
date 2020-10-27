print("auto sum")
run = 1
while run == 1:
    def my_auto_sum(a):
        try:
            b=[int(x) for x in str(a)]
            result=sum(b)
            print("Сума елементів введених чисел:"+str(result))
           
        except ValueError:
            print("Працюємо тільки з числами")
    my_auto_sum(a=int(input("Вкажіть число: ")))
    run -= 1
