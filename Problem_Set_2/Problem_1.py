"""
0	5000.00	                        100 (= 5000 * 0.02)	        4900 (= 5000 - 100)	            73.50 (= 0.18/12.0 * 4900)
1	4973.50 (= 4900 + 73.50)	    99.47 (= 4973.50 * 0.02)	4874.03 (= 4973.50 - 99.47)	    73.11 (= 0.18/12.0 * 4874.03)
2	4947.14 (= 4874.03 + 73.11)	    98.94 (= 4947.14 * 0.02)	4848.20 (= 4947.14 - 98.94)	    72.72 (= 0.18/12.0 * 4848.20)
"""


balance = 42   # the outstanding balance on the credit card
annualInterestRate = 0.2   # annual interest rate as a decimal
monthlyPaymentRate = 0.04   # minimum monthly payment rate as a decimal

totalPaid = 0

for x in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid += minimumMonthlyPayment
    balance -= minimumMonthlyPayment
    balance += balance * (annualInterestRate / 12)

print("Remaining balance:", round(balance, 2))
