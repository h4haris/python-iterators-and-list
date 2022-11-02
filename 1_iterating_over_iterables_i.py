# Iterating over iterables
#
# You are provided with a list of strings flash. Iterate over the list by using a for loop. And also create an iterator for the 
# list and access the values from the iterator.


# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))
