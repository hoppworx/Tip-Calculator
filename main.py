# Start & capture inputs from user
print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill? $"))
tip = int(input("What percent tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Original version - But this truncates the 2-decimal output if ends in 0
# pay_amount = round(((total_bill * (tip / 100 + 1)) / people), 2)
# print(f"Each person should pay: ${pay_amount}")

# Ensures display of 2 digits even if ends in 0
bill_per_person = (total_bill * (tip / 100 + 1)) / people
pay_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${pay_amount}")
