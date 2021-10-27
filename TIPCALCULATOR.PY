#This tip calculator should make dining out as smooth as possible 
#the welcome message is the first thing people see
print("Welcome to the tip calculator! This should make dining easy!")
food = float(input("What was the cost of your food? $"))
people = int(input("How many people are splitting the bill? "))
tip = int(input("How much tip percentage would you like to give? ")) 

#final bill = (percentage + tax + cost of food)
final_bill = ((tip / 100 * food) + (food * .10) + (food)) 
final_bill_total = round(final_bill, 2)
print(f"Total bill: ${final_bill_total}")
due_for_each_person = (final_bill / people)
final_bill_for_each_person = round(due_for_each_person, 2)
print(f"Amount due by each person: ${final_bill_for_each_person}")