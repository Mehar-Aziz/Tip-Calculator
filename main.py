print("Welcome to Tip Calculator")
bill= input("What was the total bill? $")
tip = input("What percentage tip would you want to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)

percent = tip_int / 100
total_tip = bill_float * percent #total tip to be givin
bill = bill_float + total_tip
equal_bill = bill / people_int
final_amount = round(equal_bill, 2)
print(f"The bill is: ${final_amount}")
