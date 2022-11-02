# Using conditionals in comprehensions II
# 
# Given a list of strings "fellowship", create a list that keeps members of fellowship with 7 or more 
# characters and replaces others with an empty string. Use member as the iterator variable in the list 
# comprehension.


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)
