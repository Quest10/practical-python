# pcost.py
#
# Exercise 1.27, 1.30, 1.31

# 1.27
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase
# price of a single stock holding. Write a program called pcost.py that opens this file, reads
# all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

# 1.30
# Take the code you wrote for the pcost.py program in Exercise 1.27 and turn it into a function
# portfolio_cost(filename). This function takes a filename as input, reads the portfolio data in
# that file, and returns the total cost of the portfolio as a float.

# 1.31
# Modify the pcost.py program to catch the exception, print a warning message, and continue processing
# the rest of the file.


def portfolio_cost(filename):
    total_cost = 0
    
    f = open(filename, 'rt')
    # Skipp headers
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        # remember index start at 0
        # strip for delete \n characters. 
        total_cost = total_cost + ( int(row[1]) * float(row[2].strip()) )
    f.close()    
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total amount: {cost}$')   
