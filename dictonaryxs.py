print("my_dictonarys")
run = 1
while run == 1:
    a = input("Введите данные словаря:")
    b = input("Введите данные второго словаря:")
    
    def mergedicts(a, b):
        for key in b:
            if isinstance(a.get(key), dict) or isinstance(b.get(key), dict):
                mergedicts(a[key], b[key])
            else:
                a[key] = b[key]
        return a
    print(a,b)

