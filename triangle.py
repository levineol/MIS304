#Class header goes here

#Import relevant .py files
import shape

#Define Triangle class - inherits from Shape
class Triangle(shape.Shape):

    #Define initializer method
    def __init__(self, color, border, name):
        #Call initializer of parent and pass parent attribute values
        super().__init__(color, border, name)

        #Set default values for Triangle attributes
        self.__base = 1
        self.__height = 1

    #Define __str__ method
    def __str__(self):
        #Use __str__() from parent and add Triangle attributes
        string = super().__str__() + " Base: " + str(self.__base) + \
                 " Height: " + str(self.__height)
        return string

    #Create accessor
    def get_base(self):
        return self.__base

    #Create mutator
    def set_base(self, new_base):
        #Ensure base is positive
        if new_base > 0:
            self.__base = new_base
        else:
            print("Invalid base. Base not changed.")

    #Create accessor
    def get_height(self):
        return self.__height

    #Create mutator
    def set_height(self, new_height):
        #Ensure height is positive
        if new_height > 0:
            self.__height = new_height
        else:
            print("Invalid height. Height not changed.")

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = 0.5 * self.__base + self.__height

        return area
