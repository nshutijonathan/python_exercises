import statistics
import random
for m in range(0,11):
    for k in range(1,m):
        print("*",end="")
    print()
for n in range(1,4):
     c=n+(n+1)
     print(c)
    
a=statistics.mean([1,2,3,4,4])
b=[str(num) for num in range(10)]
g=random.shuffle(b)
print(g)

