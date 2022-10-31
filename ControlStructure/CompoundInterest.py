"""" A person invests $1000 in a savings account yielding 5 percent interest. Assuming that all
interest is left on deposit in the account, calculate and print the amount of money in the
account at the end of each year for 10 years. Use the following formula for determining
these amounts:
a=p(1+r)n
where
p is the original amount invested (i.e., the principal),
r is the annual interest rate,
n is the number of years and
a is the amount on deposit at the end of the nth year."""

if __name__ == '__main__':
    principal = 1000
    rate = 0.05
    print("%4s%24s" %("Year", "Amount of money"))
    for year in range(1, 11):
        amount = principal * (1 + rate) ** year
        print("%4d%24.2f" % (year, amount))
