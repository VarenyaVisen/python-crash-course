# Using dictionary to store one kind of information about many objects

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favourite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")

print(favourite_languages.items())

print("Name of the students who like python: ")
for key, language in favourite_languages.items():
    if language == 'python':
        print(key)