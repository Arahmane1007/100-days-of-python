# tip calculator

print("Welcome to the tip calculator")

total_bill = float(input("What is the total bill?\n").replace('$',''))

people = int(input("How many people to split the bill with?\n"))

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

tip = (percentage / 100) * total_bill

bill_for_each = (total_bill + tip) / people

print(f"Each person should give: {bill_for_each:.2f}")

