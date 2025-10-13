first_name = "ada"
last_name = "lovelace"
full_namee = f"{first_name} {last_name}"

print(full_namee)

print(f"Hello, {full_namee.title()}!")

#We can aslo compose a message using f string and assign it to a variable
message = f"Welcome to the team : {full_namee.title()}!!"
print(message)