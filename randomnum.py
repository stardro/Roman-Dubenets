num = input ("Введіть число: ")

if int (num) > 0 :
    if int (num) > 10 :
        print ("Ви ввели число більше 10")
    else :
            print("Ви ввели число більше 0 ")
elif int (num) < -10 :
    print("Ви ввели число - 10")
else :
    print("Ви ввели число меньше 0 і більше -10")
print("All is okey! ")

name = input()
A = "Yes" if name != "Test" else"No"
print(A)