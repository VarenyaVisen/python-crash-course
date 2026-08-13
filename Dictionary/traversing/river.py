rivers = {'ganga': 'India', 'nile': 'Egypt', 'Yamuna': 'India'}
for keys, value in rivers.items():
    print(f"The {keys.title()} runs through {value.title()}.")

print("The name of the rivers in the list are - ")
for keys in rivers.keys():
    print(keys.title())

print("The name of the countrys mentioned in the list are - ")
for values in set(sorted(rivers.values())):
    print(values.title())