#This tip calculator should make dining out as smooth as possible 
#the welcome message is the first thing people see
print("Welcome to the tip calculator! This should make dining easy!")
food = float(input("What was the cost of your food? $"))
people = int(input("How many people are splitting the bill? "))
tip = int(input("How much tip percentage would you like to give? ")) 

#final bill = (percentage + tax + cost of food)
final_bill = ((tip / 100 * food) + (food * .10) + (food)) 
#I am rounding since we can only pay up to two decimal points
#$12.50 as tip for example. Not $12.5843
final_bill_total = round(final_bill, 2)
#You can see it as a normal numerical value here
print(f"Total bill: ${final_bill_total}")
#here we can see how much each person owes
due_for_each_person = (final_bill / people)
#Again, it needs to be rounded. Like how we would see it on a regular bill or invoice
final_bill_for_each_person = round(due_for_each_person, 2)
print(f"Amount due by each person: ${final_bill_for_each_person}")