
def my_string(txt):
    for i in txt:
        x = input("Введіть символ, який Вы хочете найти в тексті:")
        count=txt.count(x)
        print("Кількість символів в тексті: "+str(count))
txt = input("Введіть текст:")
my_string(txt)
