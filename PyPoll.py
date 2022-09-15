# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file. 
election_data = open(file_to_load, 'r')

# Close the file
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)

import csv
import os

# Assign a varaiable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Use the open statement to open the file as a text file
outfile = open(file_to_save, "w")

# Write some data to the file
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path
file_to_load =  os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)
    



