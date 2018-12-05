def is_isogram():
    word=str(input("please enter anything"))
    word_set=set(word)
    if word.strip()=="":
        print(word,False)
    elif len(word)==len(word_set):
        print(word,True)
    elif type(word)!= str:
        raise typeError
        
    else:
        print(word,False)
is_isogram()
