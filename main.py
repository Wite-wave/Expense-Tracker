import time
from data.save import save, load, start

options = []
costs = [] #I can't figure out how to get the summed prices
#from options
isdone = None
mt = ""

# type checker
def isInt(var):
    return isintance(var, int)

# check if price is properly input
def checkPrice():
    price = float(input("Price: "))
    
    if not isInt(price):
        price = 0
    else:
        return price


def printAll(array):
    for i in array:
        print(f"{i.get('Name'):^30} {i.get('price'):<10}")
    print(f"{mt:-^80}") #Draw a dilimiter line
    print(f"{mt:<12}Total: {sum(costs):^30}") #f strings don't
    # accept empty string brackets "{}"


def addOptions():
    isdone = False
    while isdone == False:
        Name = input("Add item: ")
        if(Name.lower() != "done"):
            price = float(input("Price: "))
            costs.append(price)
            options.append({"Name":Name, "price":price})
            printAll(options)
            print("\n")
        else:
            printAll(options)
            print(f"{sum(costs)}")
            print("All done")
            
            isdone = True


def action():
    active = True
    while(active):
        action = input("Load, Save or Add: ")
        action = action.lower()
        if(action == "load"):
            load(options)
            #print("Loaded!")
        elif(action == "save"):
            save(options)
            #print("Saved!")
        elif(action == "add"):
            #print("Added")
            addOptions()
        elif(action == "stop"):
            active = False
            print("Bye")

print(options)
#start()    
action()
#addOptions()

