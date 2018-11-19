#Author: Olivia LeVine
#Homework Number and Name: Homework 9 Serendipity 3
#Due DAte: November 14th
#Program Details: Use inheritance to allow users to order dessert, Candy Class

#Import super class
import dessert

#Define candy class
class Candy(dessert.Dessert):
    #Define the initializer method
    def __init__(self, name, kind):
        #Call initializer of parent
        super().__init__(name, kind)

        #Define candy attributes
        self.__weight = 1
        self.__price_per_pound = 1

    #Define __str__ method
    def __str__(self):
        #__str__ from parent + candy attributes
        string_candy = super().__str__() + " $" + str(format(self.calculate_cost(), '.2f'))
        return string_candy
    
    #Create accessors
    def get_weight(self):
        return self.__weight
    def get_price_per_pound(self):
        return self.__price_per_pound

    #Define function to update weight
    def update_weight(self, new_weight):
        #Validate input
        if new_weight > 0:
            self.__weight = new_weight
            return 'TRUE'
        else:
            print("Weight invalid. Must be a positive number.")
            return 'FALSE'
    #Define function to update price per pound
    def update_price_per_pound(self, new_price):
        #Validate input
        if new_price >= 0:
            self.__price_per_pound = new_price
            return 'TRUE'
        else:
            print("Price invalid. Must be a non-negative number.")
            return 'FALSE'
    #Define function to calulate cost    
    def calculate_cost(self):
        #Calculate cost
        cost = self.__weight * self.__price_per_pound
        return cost
    
    
