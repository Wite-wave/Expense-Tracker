import time
import json
from data.save import save, load, start

options = []
costs = []
total = 0
#costs = [] #I can't figure out how to get the summed prices
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
    print(f"{mt:<12}Total: {getTotal():^30}frs") #f strings don't
    # accept empty string brackets "{}"

def getTotal():
    total = 0
    for i in options:
        total = total + i.get("price")
    return total


def addOptions():
    total = 0
    isdone = False
    while isdone == False:
        Name = input("Add item: ")
        if(Name.lower() != "done"):
            price = float(input("Price: "))
            options.append({"Name":Name, "price":price})
            #getTotal(options)

            printAll(options)
#            printAll(costs)
# So appararently the little bugger above me was
# replacing all the numerical variables from
# cost with the value "i" 
            print("\n")
        else:
            printAll(options)
            print(f"{getTotal()}frs")
            print("All done")
            
            isdone = True


def action():
    active = True
    while(active):
        action = input("Load, Save or Add: ")
        action = action.lower()
        if(action == "load"):
            load(options)
            print("Loaded!")
        elif(action == "save"):
            save(options)
            print("Saved!")
        elif(action == "add"):
            addOptions()
            print("Added")
        elif(action == "exit"):
            active = False
            print("Bye!")

print(options)
#start()
action()
#addOptions()

