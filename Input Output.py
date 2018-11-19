#Prompt header goes here

#Prompt user to enter first name
first_name = input("What is your first name? ")

#Prompt user to enter last name
last_name = input("What is your last name? ")

#Print first and last name
print(first_name, last_name)

#Promt user to enter hours worked and pay rate
hours_worked = input("How many hours did you work? ")
pay_rate = input("What is your pay rate? $")

#Cast hours_worked and pay_rate from user to float
hours_worked = float(hours_worked)
pay_rate = float(pay_rate)

#Calculate total pay
total_pay = hours_worked * pay_rate

#Display hours_worked, pay_rate, and total_pay
print(hours_worked, pay_rate)
print(total_pay)
