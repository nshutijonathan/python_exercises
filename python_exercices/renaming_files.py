import os
def rename_files():
    file_list=os.listdir(r"C:\Users\Technician\Desktop\python\photos")
    print(file_list)
    g=os.getcwd()
    print(g)
    os.chdir(r"C:\Users\Technician\Desktop\python\photos")
    for file_name in file_list:
        b=os.rename(file_name,file_name.translate("0123456789"))
        print(b)
rename_files()
