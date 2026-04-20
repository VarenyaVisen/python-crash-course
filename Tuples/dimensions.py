# An immutablr list is called tuple - basically its a list of items that cannot be changed 

#Define a tuple - we use () to define tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# If i try to change the tuple it will throw an error 
dimensions[0] = 250

# tuples are technically defined by comma. paranthesis just make them look neater
a = 3,
print(a)
a[0] = 3