def save(items):
    action = input("Save: Y or N - ")
    name = input("Name of file: ")
    #users = []
    #users.append(name)
    #if action.lower() == "y":
        #with open(f"{name}.csv", "w") as file:
            #file.write("Something")
    if action.lower() == "y": 
        with open(f"{name}", "w") as file:
            for item in items:
                file.write(f"{item}\n")

def load(items):
    action = input("Load: Y or N? ")
    name = input("Name of file: ")
    if action.lower() == 'y':
        with open(f'{name}', 'r') as file:
            items = file.read().splitlines()
        print(items)
    else:
        print("Good bye!")
        #print(items)


def start():
    
    action = input("Load or save? ")
    if action.lower() == "save":
        save(["Dave", "Steve", "Frank"])
    elif action.lower() == "load":
        load()

#start()
