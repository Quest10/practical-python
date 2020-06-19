# pcost.py
#
# Exercise 1.27, 1.30, 1.31, 1.32, 1.33

# 1.27
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase
# price of a single stock holding. Write a program called pcost.py that opens this file, reads
# all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

# 1.30
# Take the code you wrote for the pcost.py program in Exercise 1.27 and turn it into a function
# portfolio_cost(filename). This function takes a filename as input, reads the portfolio data in
# that file, and returns the total cost of the portfolio as a float.

# 1.31
# Modify the pcost.py program to catch the exception, print a warning message, and continue
# processingthe rest of the file.

# 1.32
# Modify your pcost.py program so that it uses the csv module for parsing and try running
# earlier examples.

# 1.33
# you might pass the name of the file in as an argument to a script. Try changing the
# bottom part of the program as follows:

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    try:
        with open(filename, 'rt') as file:
            for line in csv.reader(file):
                try:
                    # remember index start at 0
                    # strip for delete \n characters. 
                    total_cost = total_cost + ( int(line[1]) * float(line[2].strip()) )
                except:
                    # if line can not be parsed we continue the loop
                    continue
    except:
        print("Error file")
        exit(0)
    return total_cost

def get_file():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    return filename

cost = portfolio_cost(get_file())

print(f'Total amount: {cost}$')   
