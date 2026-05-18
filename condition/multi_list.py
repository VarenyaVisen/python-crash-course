available_toppings = ["pepperoni", "mushroom", "green pepper","chilli flakes", "extra cheese"]

requested_toppings = ["mushroom", "olives", "french fries", "extra cheese"]

for toppings in requested_toppings:
    if toppings in available_toppings:
        print(f"Adding - {toppings}")
    else:
        print(f"Sorry, we dont have {toppings}")

print("\nFinished making your pizza")