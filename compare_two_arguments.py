print ("Порівняєм числа")
x = float(input("Введіть перше число: "))
y = float(input("Введіть другее число: "))
def myfunc(x, y):
    if x>y:
        print("Вітаю! Ви позитивно мислите!")
    elif x<y:
        print("Вам погано? Зверніться до лікаря!")
    else:
        print("А початок був такий обтимістичний!")
myfunc(x, y)
                
