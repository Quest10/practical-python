# mortgage.py
#
# Exercises 1.7

# 1.7 
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
# Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly
# payment is $2684.11.
# We have to obtain: 966,279.6.

# 1.8
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the total amount
# paid along with the number of months required.
# When you run the new program, it should report a total payment of 929,965.62 over 342 months.

# 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally handled.
# Make it so that the user can set these variables:

# extra_payment_start_month = 60
# extra_payment_end_month = 108
# extra_payment = 1000

# Make the program look at these variables and calculate the total paid appropriately.
# How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5
# of the mortgage?

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000

month_count = 1

extra_payment_start_month = 60
extra_payment_end_month = 108


while (principal - payment) > 0:

    if month_count >= extra_payment_start_month and month_count < extra_payment_end_month:
    # less than because we start in month 0 so if we stop at _last month_
    # we finish 1 month later
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
    # better option is doing this fragment as main function
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(f'{month_count} \t\t {round(total_paid,2)} \t{round(principal,2)}')
    month_count = month_count + 1


print(f'Total paid: \t {round(total_paid, 2)}')
print(f'Total months:  \t{month_count}')
