#Author: Olivia LeVine
#Homework Number and Name: Homework 9 Serendipity 3
#Due DAte: November 14th
#Program Details: Use inheritance to allow users to order dessert, Ice Cream Class

#Import super class
import dessert

#Define Global variables
SMALL = 1.49
MEDIUM = 1.99
LARGE = 2.49

#DEfine class
class Ice_Cream(dessert.Dessert):
    #Define initializer
    def __init__(self, name, kind):
        #Call initializer of parent
        super().__init__(name, kind)

        #Define ice_cream attributes
        self.__size = "L"
        self.__price = 1

        #Define __str__ method
    def __str__(self):
        string_icecream = super().__str__() + " $" + str(format(self.calculate_cost(), '.2f'))
        return string_icecream
    
    #Define accessors
    def get_size(self):
        return self.__size
    def get_price(self):
        return self.__price

    #Define function to update size
    def update_size(self, new_size):
        #Check if size small
        if new_size == "S":
            self.__size = new_size
            return 'TRUE'
        #Check if size medium
        elif new_size == "M":
            self.__size = new_size
            return 'TRUE'
        #Check if size large
        elif new_size == "L":
            self.__size = new_size
            return 'TRUE'
        #Check if size is invalid
        else:
            print('Size not valid. Must enter "S", "M", or "L"')
            return 'FALSE'
    #Define function to update price
    def update_price(self, size):
        #Check is size small
        if size == "S":
            self.__price = SMALL
        #Check if size medium
        elif size == "M":
            self.__price = MEDIUM
        #Check if size large
        elif size == "L":
            self.__price = LARGE
    #Define function to calculate cost           
    def calculate_cost(self):
        #Calculate cost
        cost = self.__price
        return cost
    
        
