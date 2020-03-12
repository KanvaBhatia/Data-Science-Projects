# compound_interest.py
#   this program calculates the future value of an investment
#   user provides principal, interest rate and duration of investment.

print("This program calculates the future value on an investment")

# Requests inputs from user.
principal = eval(input("Enter initial amount invested: "))
interest = eval(input("Enter interest rate in decimals: "))
years = eval(input("Enter number of years invested: "))

# calculates interest
for i in range(years):
    principal += (principal * interest)

print("The value in ", years, "years is: ", principal)
