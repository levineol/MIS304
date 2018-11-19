#Author: Olivia LeVine
#Homework Number and Name: Homework 9 Serendipity 3
#Due DAte: November 14th
#Program Details: Use inheritance to allow users to order dessert, Cookie Class

#Import dessert file
import dessert

#Define cookie class
class Cookie(dessert.Dessert):

    #Define initalizer method
    def __init__(self, name, kind):
        #Call initializer of dessert 
        super().__init__(name, kind)

        #Set values for cookie attributes
        self.__quantity = 1
        self.__price_per_dozen = 1

    #Define __Str__ method
    def __str__(self):
        string_cookie = super().__str__() + " $" + str(format(self.calculate_cost(), '.2f'))
        return string_cookie
    
    #Define accessors
    def get_quantity(self):
        return self.__quantity
    def get_price_per_dozen(self):
        return self.__price_per_dozen

    #Define function to update quantity
    def update_quantity(self, new_quantity):
        #Validate input
        if new_quantity > 0:
            self.__quantity = new_quantity
            return 'TRUE'
        else:
            print("Quantity is invalid. Must be a positive value.")
            return 'FALSE'

    #Define function to update price per dozen
    def update_price_per_dozen(self,new_price):
        #Validate input
        if new_price >= 0:
            self.__price_per_dozen = new_price
            return 'TRUE'
        else:
            print("Price is invalid. Must be a non-negative value.")
            return 'FALSE'
    #DEfine function to calculate cost
    def calculate_cost(self):
        #Calculate cost
        cost = self.__quantity * (self.__price_per_dozen / 12)
        return cost

