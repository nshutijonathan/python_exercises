import os
from os import listdir
def renaming():
    p=os.listdir(r"E:\python_exercices\renaming_a_file\pic")
    print(p)
    current_directory=os.getcwd()
    print(current_directory)
    v= os.chdir(r"E:\python_exercices\renaming_a_file\pic")
    for m in p:
        os.rename(m,m.translate("abc","nshuti"))
renaming()

