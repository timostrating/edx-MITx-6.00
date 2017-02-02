balance = 42   # the outstanding balance on the credit card
annualInterestRate = 0.2   # annual interest rate as a decimal
monthlyPaymentRate = 0.04   # minimum monthly payment rate as a decimal


paymentBase = 0
balanceNew = balance

while balanceNew > 0:
    balanceNew = balance
    paymentBase += 10
    if paymentBase > (balanceNew * annualInterestRate / 12):
        for i in range(0, 12):
            balanceNew -= paymentBase
            balanceNew += (balanceNew * annualInterestRate / 12)

print("Lowest Payment:", paymentBase)