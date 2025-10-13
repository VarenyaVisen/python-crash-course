# 1. Set a variable to a person's name with leading/trailing whitespace
name = "\t\n   Albert Einstein   \n\t"

# 2. Print the name with the whitespace displayed
print("Original name:")
print(f"'{name}'") # Using f-string to explicitly show quotes around the string

# 3. Print the name with the left-stripping function (lstrip())
print("\nAfter lstrip():")
print(f"'{name.lstrip()}'")

# 4. Print the name with the right-stripping function (rstrip())
print("\nAfter rstrip():")
print(f"'{name.rstrip()}'")

# 5. Print the name with the strip() function
print("\nAfter strip():")
print(f"'{name.strip()}'")