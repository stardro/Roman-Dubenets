print('first and last number')
run = 1
while run ==1:
    def my_list(new_list):
        try:
            output_value = list(
                float(item)
                for item in new_list.split())
            print("Перше число", output_value[0])
            print("Останнє число", output_value[-1], "\n")
        except ValueError:
            print("Вводимо тільки цифри!\n")
    my_list(input("Введіть ряд чисел: "))
            
