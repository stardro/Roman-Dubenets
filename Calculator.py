print("Простий калькулятор")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("ВВедіть необхідну операцію:")
result = None
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    print("Помилка")
if result is not None:
    print("Результат:", result)
