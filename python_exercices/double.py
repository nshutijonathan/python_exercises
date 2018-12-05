import os
def nshuti():
    list_files=os.listdir(r"C:\Users\Technician\Desktop\python\photos")
    print(list_files)
    for file_name in list_files:
        os.rename(file_name, file_name.translate(None,"0123456789"))
nshuti()
