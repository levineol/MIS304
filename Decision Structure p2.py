#Program comments

#Prompt user for gender and minority
gender = input("Please enter your gender (M or F): ")
minority = input("Are you a minority? (Y or N) ")

#Check eligibility
if gender == "F" or minority == "Y":
    print("You are eligible for the scholarship. Please apply.")
else:
    print("You are not eligible for the scholarship. Blame your parents.")
    
#Print blank line
print()

#Prompt user for age
age = int(input("Please enter your age: "))

#Check age
if age >= 18:
    #Prompt user for citizenship
    citizenship = input("Are you a U.S. citizen? (Y or N): ")
    #Check citzenship
    if citizenship == "Y":
        #Prompt user for felon
        felon = input("Are you a convicted felon? (Y or N): ")
        #Check for felon
        if felon == "N":
            #Print eligible
            print("You are eligible, go vote!")
        #Print ineligible
        else:
            print("You are a convicted felon, you are not eligible to vote.")
    #Print ineligible
    else:
        print("You are not a US citizen, you are not eligible to vote.")
#Print ineligible
else:
    print("You are not old enough to vote.")

#Print my campaign message
print("Vote Olivia for imperial overlord!")


        
