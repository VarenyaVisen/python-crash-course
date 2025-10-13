# lstrip() is used to remove extra white spaces from the left of the string
# rstrip() it is used to remove extra space from the right side of the string
# strip() it is used to remove spaces from both beginning and the end of the string
favourite_language = '  Python is very cool  '

name = " Varenya "
print(name,favourite_language)

print(name,favourite_language.lstrip())

# To remove the whitespace permanently
favourite_language = favourite_language.lstrip()
print(favourite_language)