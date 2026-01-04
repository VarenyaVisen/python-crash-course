motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}.")

# popping item from any position 
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")

# removing item when we dont know the position of the element
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati') 
print(motorcycles)
