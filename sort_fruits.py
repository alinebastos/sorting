print("Starting the program")

# Specify where the input file is
inputFile = open('unsorted_fruits.txt', 'r')

# Specify where the output file is
outputFile = open('sorted_fruits.txt', 'w')

# Read the input file
fruits = inputFile.readlines()

# Sort the items in the list
fruits.sort()

# For each fruit in the Fruits list
for fruit in fruits:
    # If the line is not blank
    if fruit <> "\n":
        # Then write the fruit to the output file
        outputFile.write(fruit)

# Close the files
inputFile.close()
outputFile.close()

print("Ending the program")
