


options = []
isdone = None

def addOptions():
    isdone = False
    while isdone == False:
        item = input("Add item: ")
        if(item.lower() != "done"):
            options.append[item]
        else:
            isdone = True

addOptions()

