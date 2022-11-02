# Dict comprehensions
# 
# Given a list of strings "fellowship", create a dictionary with the members of the list as the keys 
# and the length of each string as the corresponding values.


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
