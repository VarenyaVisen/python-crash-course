# info about pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushroooms', 'extra cheese'],
}

# Summarize order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

