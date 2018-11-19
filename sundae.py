#Author: Olivia LeVine
#Homework Number and Name: Homework 9 Serendipity 3
#Due DAte: November 14th
#Program Details: Use inheritance to allow users to order dessert, Sundae Class

#Import super classes
import dessert
import ice_cream

#Define global variables
PRICE = .29

#Define sundae class
class Sundae(ice_cream.Ice_Cream):

    #Define initializer
    def __init__(self, name, kind):
        #Call initializer of parent
        super().__init__(name, kind)

        #Define sundae attributes
        self.__toppings = 1

    #Define __str__ method
    def __str__(self):
        string_sundae = str(self.get_name()) + " " + str(self.get_kind()) +" $" + str(format(self.calculate_cost_sundae(), '.2f'))
        return string_sundae

    #Define get toppings method
    def get_toppings(self):
        return self.__toppings

    #Define update toppings method
    def update_toppings(self, new_toppings):
        #Validate user entry for toppings
        if new_toppings > 0:
            self.__toppings = new_toppings
            return 'TRUE'
        else:
            print("Toppings is invalid. Must be a positive value.")
            return 'FALSE'
    #Define calculate cost for sundaes function
    def calculate_cost_sundae(self):
        #Get cost from ice cream
        ice_cream_cost = super().calculate_cost()
        #Calculate cost of toppings
        toppings_cost = self.__toppings * PRICE
        #Calculate total cost of sundae
        cost = ice_cream_cost + toppings_cost
        return cost
        
