# Accessing values using square brackets might cause one problem
# If the key does not exist it will throw an errror

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

print(alien_0.get('points','No points value assigned'))

#In the above method if the key exists it will print the value and if not it handles the error gracefully