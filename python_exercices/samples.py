a=int(input("enter first range you want"))
b=int(input("enter second range you want"))
for m in range(a,b):
    if all(m%n!=0 for n in range(2,m)):
           print(m)
