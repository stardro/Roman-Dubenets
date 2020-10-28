print("my_dictonarys")
run = 1
while run == 1:
    
    def my_dictonary(new_dict1, new_dict2):
        my_dictonary = new_dict1.copy()
        my_dictonary.update(new_dict2)
        return my_dictonary
    
    def argument1_2(x, y):
        argument1 = {}
        argument2 = {}
        id_num = 0
        
        for i in x:
            id_num += 1
            argument1[str(id_num)] = i
            
        for j in y:
            id_num += 1
            argument2[str(id_num)] = j
        print(my_dictonary(argument1, argument2), "\n")

    argument1_2(
        input("Введіть дані для першого словника: \n"),
        input("Введіть дані для другого словника: \n"))
