# Simple example to show how to calculate a times
# table for a given number and a given length
times_number = input("Enter times table number: ")
times_length = input("Enter times table length: ")

# Execute this loop up to the length we want for the times table
# For example is we are doing the 5 times table up to 15 then the
# length will be 15. Note the range function needs to be increased
# by 1 in order to get the full range
for multiplier in range(1,times_length + 1):
    result = times_number * multiplier
    print str(multiplier) + " x " + str(times_number) + " = " + str(result)

