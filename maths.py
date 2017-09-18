times_number = input("Enter times table number: ")
times_length = input("Enter times table length: ")
for multiplier in range(1,times_length + 1):
    result = times_number * multiplier
    print str(multiplier) + " x " + str(times_number) + " = " + str(result)

