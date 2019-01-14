def myfunc(string):
    newString = ''
    for index, i in enumerate(string):
        if(index % 2 == 0):
            i = i.upper()
        else:
            i = i.lower()
        newString += i
        print(newString)
    return newString


myfunc('HitvArdhan')
