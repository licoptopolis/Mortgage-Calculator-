# Mortgage Calculator
(ID -12345)

The Mortgage Calculator built using Python assess a clients suitability for a loan and calcuates their monthly repayment schedule.

The script imports the math and sys modules.

The get_user_input() function is defined, which takes a user prompt, data type, minimum and maximum values, and returns the user's input. It includes error handling to ensure that the input is valid.

The staff access system prompts the user for a staff ID, compares it to a predefined ID, and grants or denies access accordingly. If the user enters an incorrect ID, the program exits.

The script prompts the user for their annual income and compares it to a minimum value. If the user's income is below the minimum, the program exits. The script also prompts the user for their total assets and compares it to a threshold based on their annual income. If the user's assets are below the threshold, the program exits.

The script prompts the user for the loan amount, interest rate, and term of the loan in years. It also gives the option to calculate and display a payment schedule.

The script converts the annual interest rate to a monthly rate and the loan term to months.

The script calculates the monthly mortgage payment using the formula for a fixed-rate mortgage.

The script displays the monthly mortgage payment, rounded to two decimal places.

If the user opted to calculate and display a payment schedule, the script calculates and displays the monthly payments, interest payments, and principal payments for each month of the loan term.

This code can be used by banks, mortgage lenders, or other financial institutions to assess loan eligibility and calculate monthly payments. It can be further developed by adding more features such as:

Adding different loan types and interest rates, such as adjustable-rate mortgages.

Incorporating credit scores and other financial information to determine loan eligibility.

Adding the ability to save client information and loan details for future reference.

Adding a graphical user interface (GUI) to make the program more user-friendly.
