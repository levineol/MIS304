#program comments

#Prompt for lists
lists = int(input("How many lists do you want to create? "))

for value in range(lists):

    #Promt user for starting number
    start = int(input("What is the starting value of the list? "))

    #Prompt user for ending number
    end = int(input("What is the ending value of the list? "))

    #Validate input
    while start >= end:
        #Print bad message
        print("Bad data. Try again")
        
        #Promt user for starting number
        start = int(input("What is the starting value of the list? "))

        #Prompt user for ending number
        end = int(input("What is the ending value of the list? "))


    #Assign total variable
    total = 0

    #Print values between starting and ending values entered by users
    for number in range(start, end + 1):
        #Print values
        print(number, end=" ")
        total = total + number
        
    #Print Sum
    print("\nSum:",total)




#print blank line
print()

#Loop to print name 5 times
for name in [1, 2, 3, 4, 5]:
    #Print my name
    print("Olivia LeVine")

#Print blank line
print()

#Print numbers from 0 to 10    
for num in range(11):
    #Print num
    print("num: ", num)

#Print blank line
print()

#Print values from 10 to 20
for number in range(10, 21):
    #Print number
    print(number)

#Print blank line
print()
    
#Print even values between 1 and 9
for even in range(2, 10, 2):
    #Print even
    print(even)


