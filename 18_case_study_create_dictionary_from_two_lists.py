# Task 1: 
# Create Dictionaries from 2 lists for data science

# combine two lists into a dictionary

# The first list "feature_names" contains header names of the dataset and the second list "row_vals" 
# contains actual values of a row from the dataset, corresponding to each of the header names.



# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary from zip object: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)





# Task 2: 
# Write a function which create dictionary with lists



# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)





# Task 3: 
# Using a list comprehension to generate a list of dicts, where the keys are the header names and the 
# values are the row entries.



# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])




# Task 4: 
# convert the list of dictionaries into a pandas DataFrame.




# Import the pandas package
import pandas as pd

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())