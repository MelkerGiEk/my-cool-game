import time


inv = []


def inventory(): 
    global inv
    if len(inv) < 1: 
        print("Your inventory is empty! Choose a door to have a chance of receiving items!") 
    elif len(inv) > 0:
        print("YOUR INVENTORY:")
        for item in inv: 
            print(item)
            time.sleep(1.0)
    
        


 
