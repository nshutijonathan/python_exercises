import webbrowser
import getpass
print("welcome")
username=str(input("please enter your name"))
password=getpass.getpass("please enter your password")
if(username=="nshuti"  and password=="jonathan"):
    print("thank you very much")
    print("you have successfully loged in")
    webbrowser.open("https://www.youtube.com/watch?v=NqkiKnTwLbQ")
elif(username!="nshuti" and password!="jonathan"):
    print("wrong auntentifications")
c=int(input("enter value"))
u=bin(c)
print(u)
