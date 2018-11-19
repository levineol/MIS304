#Author: 
#Homework Number and Name: Homework 9 
#Due DAte: November 14th
#Program Details: 

#Import class files
import dessert
import candy
import cookie
import ice_cream
import sundae

#Assign global variables
CANDY = 1
COOKIE = 2
ICECREAM = 3
SUNDAE = 4
EXIT = 5
SALES_TAX = .0825

#Define print_menu function
def print_menu():
    #print statement
    print(Dessert Menu:\n 1. Candy\n 2. Cookie\n 3. Ice Cream\n 4. Sundae\n 5. Exit\n")

#Define get menu choice function
def get_menu_choice():
    #Prompt user for choice
    choice = int(input("What would you like to order? (5 to finish): "))
    #Validate user entry
    while choice < 1 or choice > 5:
        #Ask for new menu choice
        choice = int(input("Menu choice is invalid. Must enter a number between 1 and 5: "))
    return choice

#Define purchase candy function
def purchase_candy(item_list, cost_list):
    #Define name
    name = "Candy"
    #Ask user for kind of candy
    kind = input("What kind of candy would you like? ")
    #Capitilize first letter
    kind = kind[0].upper() + kind[1:]
    #Create object
    candy_ordered = candy.Candy(name, kind)

    #Prompt user for weight
    weight =  float(input("How many pounds? "))


    #Validate user entry
    while candy_ordered.update_weight(weight) == "FALSE":
        weight =  float(input("How many pounds?"))

    #Prompt user for price per pound
    price = float(input("What is the price per pound? $"))
    #Validate user input
          
    while candy_ordered.update_price_per_pound(price) == 'FALSE':
        price =  float(input("What is the price per pound? $"))
    #Add object to list
    item_list.append(candy_ordered)
    #Add cost to list
    cost_list.append(candy_ordered.calculate_cost())

#Define purchase cookie function
def purchase_cookie(item_list, cost_list):
    #Define name
    name = "Cookie"
    #Prompt user for flavor of cookie
    kind = input("What flavor of cookie? ")
    #Capitilize user input
    kind = kind[0].upper() + kind[1:]
    #Create cookie object
    cookie_ordered = cookie.Cookie(name, kind)

    #Prompt user for price per dozen
    price = float(input("What is the price per dozen? $"))
    #Validate user input
    while cookie_ordered.update_price_per_dozen(pricee) == "FALSE":
        price = float(input("What is the price per dozen? $"))
    #Prompt user for quantity of cookies
    quantity =  float(input("Number of cookies: "))
    #Validate user input
    while cookie_ordered.update_quantity(quantity) == "FALSE":
        quantity = float(input("Number of cookies: "))
    #Add object to list
    item_list.append(cookie_ordered)
    #Add cost to list
    cost_list.append(cookie_ordered.calculate_cost())

#Define function to purchase ice cream
def purchase_icecream(item_list, cost_list):
    #Define name
    name = "Ice Cream"
    #Prompt user for flavor of ice cream
    kind = input("What flavor of ice cream would you like? ")
    #Capitilize user input
    kind = kind[0].upper() + kind[1:]

    #Prompt user ofr size
    size = input("Please choose a size: ('S', 'M', or 'L') ")
    #Validate user input
    icecream = ice_cream.Ice_Cream(name, kind)
          
    while icecream.update_size(size) == "FALSE":
        size = input("Please choose a size: ('S', 'M', or 'L') ")
    #Update price
    icecream.update_price(size)

    #Add object to list
    item_list.append(icecream)
    #Add cost to list
    cost_list.append(icecream.calculate_cost())

#Define function to purchase sundae
def purchase_sundae(item_list, cost_list):
    #Define name
    name = "Sundae"
    #Ask user for input on flavor
    kind = input("What flavor of ice cream would you like? ")
    #Capitilize user input
    kind = (kind[0].upper() + kind[1:])
    #Create sundae object
    sundae_ordered = sundae.Sundae(name, kind)

    #Prompt user for size
    size = input("What size would you like? ('S', 'M', or 'L') ")
    while sundae_ordered.update_size(size) == "FALSE":
        size = input("What size would you like? ('S', 'M', or 'L') ")

    #Update price for sundae
    sundae_ordered.update_price(size)

    #Prompt user for number of toppings
    toppings = int(input("How many toppings would you like to order? "))
    #Validate toppings input
    while sundae_ordered.update_toppings(toppings)== "FALSE":
        toppings = int(input("How many toppings would you like to order? "))
 

    #Add cost to list
    cost_list.append(sundaes.calculate_cost_sundae())
    #Add object to list
    item_list.append(sundae_ordered)

#Define function to calculate sales tax
def calculate_sales_tax(subtotal):
    #Calculate sales tax
    sales_tax = SALES_TAX * subtotal
    return sales_tax

def main():
    #Create empty lists
    items_list = []
    costs_list = []
    
    #Call print menu function
    print_menu()

    #Call get menu choice function
    menu = get_menu_choice()
    
    #Check if user ordered anything
    if menu == EXIT:
        #If not print message
        print("Thank you for shopping")

    #Check if user is done
    while menu != EXIT:

        #Check if they ordered candy
        if menu == CANDY:
            #Call purchase candy function
            purchase_candy(items_list, costs_list)
            
        #Check if they ordered a cookie
        elif menu == COOKIE:
            #Call purchase cookie function
            purchase_cookie(items_list, costs_list)
            
        #Check if they ordered a cookie        
        elif menu == ICECREAM:
            #Call purchase ice cream function
            purchase_icecream(items_list, costs_list)
            
        #Check if they ordered a cookie        
        elif menu == SUNDAE:
            #Call purchase sundae function
            purchase_sundae(items_list, costs_list)
        total += 1
        menu = get_menu_choice()
    #Initialize variables
    due = 0
    subtotal = 0
          
    #Check if they ordered anything
    if total > 0:
        #Calculate subtotal
        for number in costs_list:
            subtotal += number
        #Calculate sales tax           
        sales_tax = calculate_sales_tax(subtotal)

        #Calculate total due
        total_due = subtotal + sales_tax

        #Print invoice
        print("\nDone Shopping, you have ordered", total, "items:")
        for stuff in items_list:
            print(stuff.__str__())
        #Print Receipt
        print("\nHere is your receipt:\nNumber of desserts: ", total, "\nSubtotal: $", format(subtotal, ".2f"), "\nSales Tax: $",
              format(sales_tax, ".2f"), "\nTotal due: $", format(total_due, ".2f"))
#Call main function
main()
