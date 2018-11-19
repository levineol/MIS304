#Author: Olivia LeVine
#Homework Number and Name: Homework 9 Serendipity 3
#Due DAte: November 14th
#Program Details: Use inheritance to allow users to order dessert, Dessert Class

#Define Dessert class
class Dessert:

    #Define initializer method
    def __init__(self, start_name, start_kind):
        #Define name and kind attributes
        self.__name = start_name
        self.__kind = start_kind

    #Define name and kind accesors
    def get_name(self):
        return self.__name
    def get_kind(self):
        return self.__kind

    #Define __str__ method
    def __str__(self):
        string = self.__name + " " + self.__kind
        return string
