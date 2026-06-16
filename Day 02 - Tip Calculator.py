print("Welcome to the Tip Calculator!")

amount = float(input("What amountdo you have to pay?: ₹"))
tip = int(input("How much tip would you like to give? (in %): "))
person = int(input("How many people are splitting the bill?: "))

total_tip = amount + (tip / 100)
total_amount = amount + total_tip
amount_per_person = round(total_amount / person, 2)

print(f"Each persom has to pay: ₹{amount_per_person:.2f}")
