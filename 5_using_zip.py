# Using zip
# 
# Three lists of strings are pre-loaded: mutants, aliases, and powers. 
#
# First, use list() and zip() on these lists to generate a list of tuples. 
# 
# Then, create a zip object using zip(). 
# 
# Finally, unpack this zip object in a for loop to print the values in each tuple. 


# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)