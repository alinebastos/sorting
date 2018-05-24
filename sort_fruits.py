print("Starting the program")

# Specify where the input file is
InputFile = open('unsorted_fruits.txt', 'r')

# Specify where the output file is
OutputFile = open('sorted_fruits.txt', 'w')

# Read the input file
Fruits = InputFile.readlines()

# Sort the items in the list
Fruits.sort()

# For each fruit in the Fruits list
for fruit in Fruits:
    # If the line is not blank
    if fruit <> "\n":
        # Then write the fruit to the output file
        OutputFile.write(fruit)

# Close the files
InputFile.close()
OutputFile.close()

print("Ending the program")