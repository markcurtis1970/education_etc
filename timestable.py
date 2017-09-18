# Simple example to show how to calculate a times table grid
# for a given times table for a given length.
#
# Note there's no input validation to check for valid numbers or
# data types etc, just to keep the example as simple. Plus I'm not
# a python developer :-)


# Ask user for multiplier and max range of times table
# the input statement asks for a value and loads it into the variable
# on the left

tt_num = input("Enter times table number: ") # this is the times table number you want
tt_len = input("Enter times table length: ") # this is the length of the above times table

# loop 1: we execute this loop every time up to the times table number.
# Note the range statement will execute up to 1 less than the maximum set,
# for more info see: https://docs.python.org/2/library/functions.html#range
# this is what makes each row
for tt_val in range(1,tt_num + 1):

    # reset the results each time we execute this loop to the starting
    # value of the row, note the str() changes the integer to a string type
    # so we can do things like concatenation later
    results = str(tt_val)
    # loop 2: we execute this loop up to the value of the times table length
    # this is what makes each column in a given row. Note we start the range
    # at 2, this is because the intial value is already loaded into the string
    # variable above when we reset it
    for multiplier in range(2,tt_len + 1): 
        result = tt_val * multiplier # calculate the result
        results = str(results) + "\t" + str(result) # concatenate the string, the "\t" is a tab character
    # print the results out once all columns are calculated and before moving to the next row
    print results
