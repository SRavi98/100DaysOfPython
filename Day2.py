print('Welcome to Tip Calculator!')

bill = float(input('What was the total bill? '+ "\n$"))

tip = int(input('How much tip would you like to give? 10, 12 or 15?\n'))

persons = int(input('How many people to split the bill?\n'))

total_bill = bill + (bill * (tip / 100))

bill_per_person = total_bill / persons

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")