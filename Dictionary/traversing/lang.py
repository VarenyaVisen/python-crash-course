favourite_language = {
    'jen': 'C',
    'phil': 'Python',
    'edward': 'Rust',
    'sarah': 'Python'
}

# use keys() if interested in keys
for name in sorted(favourite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# use values() if interested in values
print("The following languages have been mentioned - ")
for value in set(favourite_language.values()): # When we use set() in python it removes duplicate items 
    print(value.title())
    