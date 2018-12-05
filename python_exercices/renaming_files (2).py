import os
def nshuti():
    file_name=os.listdir(r"C:\Users\Technician\Desktop\python\photos")
    print(file_name)
    path=os.getcwd()
    print(path)
    os.chdir(r"C:\Users\Technician\Desktop\python\photos")
    for file_n in file_name:
        os.rename(file_n,file_n.translate(None,"0123456789"))
        os.chdir(path)
        print(file_n)
nshuti()
