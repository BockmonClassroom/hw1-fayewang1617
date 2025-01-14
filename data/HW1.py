
# Name: Faye(Lifei) Wang
# Date: 01/14/2025

# First, import the csv module to work with the data
import csv

# Open the Iris.csv file in read mode
with open('Iris.csv', mode='r') as file:
    # Create a reader object to read the file
    reader = csv.reader(file)
    
    # Loop through each row in the csv file
    for row in reader:
        # Print each row (it's a list of values)
        print(row)
