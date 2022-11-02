# Nested list comprehensions

# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]
# 
# Recreate this matrix by using nested listed comprehensions. 
# 
# NOTE: To create the list of lists, you simply have to supply the list comprehension as the output expression # of the overall list comprehension:
# 
# [[output expression] for iterator variable in iterable]
# 
# NOTE: the output expression is itself a list comprehension.


# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)