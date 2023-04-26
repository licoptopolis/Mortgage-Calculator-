import math
import sys
import random

# User Input
def get_user_input(prompt, data_type=float, min_value=None, max_value=None):
    while True:
        try:
            value = data_type(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError("Value must be greater or equal to {}".format(min_value))
            if max_value is not None and value > max_value:
                raise ValueError("Value must be less or equal to {}". format(max_value))
            return value
        except ValueError as e:
            print("Error: {}".format(e))

# Access system
staff_id = 12345
staff_id_user = get_user_input("Enter Staff ID: ")
if staff_id_user == staff_id:
         print("Welcome")
else:
    print("Incorrect ID. Access denied")
    sys.exit()

# Assessing clients suitability for loan
annual_income_allowance = get_user_input("Enter income figure for 2021-2022 (Pre Tax): ")
annual_income = 25000
if annual_income_allowance >= annual_income:
        print("Client meets minimum lending requirements")
if annual_income_allowance < annual_income:
    print("Client does not meet minimum requirements")
    sys.exit()

total_assets = float(input("Clients total asset value in GBP: "))
asset_threshold = annual_income * 0.10
if total_assets >= asset_threshold:
   print("Client meets asset requirements")
else:
    print("Client does not qualify for loan")
    sys.exit()

# Amount client wishes to borrow
loan_amount = get_user_input("Enter loan amount (in GBP): ", min_value=1, max_value=annual_income_allowance * 4.5)

# Get annual interest rate from user
annual_interest_rate = get_user_input("Enter annual interest rate (%): ", min_value=4.5, max_value=13.6)

# Get term of loan in years
loan_term_years = get_user_input("Enter loan term (in years): ", data_type=int, min_value=1, max_value=25)

# Get option to calculate and display payment schedule
calculate_schedule = input("Calculate and display payment schedule? (y/n): ").lower() =="y"     # y = Payment schedule
                                                                                                # n = Monthly payment
# Convert annual interest rate to monthly rate
monthly_interest_rate = annual_interest_rate / 100 / 12

# Convert loan term to months
loan_term_months = loan_term_years * 12

# Calculate monthly mortgage payment
monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / (((1 + monthly_interest_rate) ** loan_term_months) - 1)

# Displaying monthly mortgage payment
print("Monthly Mortgage Payment: £", round(monthly_payment, 2))

# Calculate and display payment schedule if option selected
if calculate_schedule:
    remaining_balance = loan_amount
    print("\nPayment Schedule:")
    print("{:<10} {:<15} {:<15} {:<15}".format("Month", "Payment", "Interest", "Principal"))
    for month in range(1, loan_term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        print("{:<10} {:<15} {:<15} {:<15}".format(month, round(monthly_payment, 2), round(interest_payment, 2), round(principal_payment, 2)))
