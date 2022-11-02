# List comprehensions for time-stamped data

# solve a simple data extraction problem by extracting the time from time-stamped Twitter data.

# The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df 
# DataFrame.

# NOTE: DataFrame columns as single-dimension arrays called "Series" data structure

# Extract the column 'created_at' from df and assign the result to tweet_time. 

# Create a list comprehension that extracts the time from each row in tweet_time. 



# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)



# Conditional list comprehensions for time-stamped data

# add a conditional expression to the list comprehension so that you only select the times in which 
# entry[17:19] is equal to '19'



# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)

