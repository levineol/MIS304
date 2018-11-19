#Olivia

#prompt the user to enter their age
age = float(input("How old are you? "))

#Check to see if they are old enough to vote
if age >= 18:
    #Tell user they are old enough to vote
    print("Congrats! You are old enough to vote.")

#Tell user they're not old enough
else:
    print("You're not old enough to vote. Keep drinking your milk.")

#Print election in November
print("There is a presidential election this November.")

#Print a blank line
print()

#Prompt user for number
number = int(input("Please enter a number: "))

#Check to see if number is negative
if number < 0:
    #Calculate absolute value of number
    number = number * -1

print("The absolute value is ", number, ".", sep="")

#Print blank line
print()

#Prompt the user for pay rate, and the number of hours worked
hours_worked = float(input("How many hours did you work? "))
pay_rate = float(input("What is your pay rate? $"))

#Check for overtime
if hours_worked > 40:
    #Calculate total pay
    total_pay = (hours_worked - 40) * pay_rate * 1.5 + (40 * pay_rate)

#If less than or equal to 40, multiply hours by pay rate
else:
    total_pay = hours_worked * pay_rate

#Print number os hours worked
print("How many hours did you work?", hours_worked)

#Print pay rate
print("What is your pay rate? $", pay_rate, sep="")

#Print total pay
print("Your total pay is $", format(total_pay, ".2f"), sep="")
