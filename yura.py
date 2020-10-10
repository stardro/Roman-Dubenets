from random import *
import math
i=1
while(i<=10):
    print(i)
    i+=1
    
a = [x for x in range(1,6)]
print(a)

x=int(input("Which digit you are looking for?"))
if x in a:
    result = a.index(x) +1

print("Position in the list:" , result)
