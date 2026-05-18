requested_toppings = ['mushroom','extra cheese','pepperoni']

for toppings in requested_toppings:
    if toppings == "mushroom":
        print("Sorry, we are out of mushrooms right now")
    else:
        print(f"Adding {toppings}")
    
print("\nFinished making your pizza")