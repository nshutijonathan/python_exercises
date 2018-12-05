import array
list_one=[str(x) for x in input("please enter your anything")]
if list_one[0]!=list_one[1] and (list_one[2]!=list_one[0] and list_one[1]+1):
    print("the list doesn't have duplicates",)
else:
    print("the list contains duplication")
