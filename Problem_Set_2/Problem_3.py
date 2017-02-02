balance = 42   # the outstanding balance on the credit card
annualInterestRate = 0.2   # annual interest rate as a decimal
monthlyPaymentRate = 0.04   # minimum monthly payment rate as a decimal

def chargeInterest(balance, annualInterestRate):
    lowerBound = balance
    upperBound = (balance * ((annualInterestRate / 12.0) + 1) ** 12)

    lowerBound /= 12.0
    upperBound /= 12.0

    Elipse = 0.01
    while(True):
        curBalance = balance
        monthlyPayout = (lowerBound + upperBound) / 2.0

        for i in range(0, 12):
            curBalance = (curBalance - monthlyPayout) * (1 + (annualInterestRate / 12))

        if round(curBalance, 2) < Elipse:
            upperBound = monthlyPayout
        elif round(curBalance, 2) > Elipse:
            lowerBound = monthlyPayout
        else:
            return round(monthlyPayout, 2)


print("Lowest Payment:", (chargeInterest(balance, annualInterestRate)))