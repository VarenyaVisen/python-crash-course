favourite_languages = {
    'jen': 'c',
    'sarah': 'python',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")


# Looping through all the keys in dict
for name in favourite_languages.keys(): # looping through keys is the default behavior, using .keys() is optional
    print(name.title())

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our pole")