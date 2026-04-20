my_foods = ['pizza',' falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: {}".format(my_foods))

print("My friend favourite foods are: {}".format(friend_foods))

my_foods.append('ice cream')
friend_foods.append('cannoli')

print("My favorite foods are: {}".format(my_foods))

print("My friend favourite foods are: {}".format(friend_foods))

# Thus method only assings the list to another variable it does not actually make a copy
# we cant work on both list separately
a = ['a','b','c']
b = a
print(b)
b.append('z')
print(a) # see i appended the value in list b but a automatically updated because they are pointing the same list