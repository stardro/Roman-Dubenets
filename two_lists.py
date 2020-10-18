import random
a=random.sample(range(30),10)
print("список а:"+str(a))
b=random.sample(range(30),10)
print("список b:"+str(b))
result = list( set(a) & set(b))
print("Однакові елементи списків:" +str(result))

