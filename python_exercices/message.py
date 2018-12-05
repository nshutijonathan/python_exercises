import webbrowser
import time
def determine_direction(message=int(input("enter value"))):
    if message=="take the load less travelled":
        print("turn left")
    elif message=='3':
            print("turn right")
    else:
            print("don't know")
determine_direction("message")
print("the current time is",time.ctime())
total_breaks=3
break_count=0
while(break_count<total_breaks):
    time.sleep(3)
    webbrowser.open("jonathan.html")
    break_count=break_count+1
for m in range(0,5):
    print(m)
z=m+(m+1)
print(z)


   
   





