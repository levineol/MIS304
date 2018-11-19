#Class header goes here

#Import relevant .py files
import shape

#Define Square class - inherits from Shape
class Square(shape.Shape):

    #Define initializer method
    def __init__(self, color, border, name):
        #Call initializer of parent and pass parent attribute values
        super().__init__(color, border, name)

        #Set default values for Square attributes
        self.__side = 1

    #Define __str__ method
    def __str__(self):
        #Use __str__() from parent and add Square attributes
        string = super().__str__() + " Side: " + str(self.__side)

        return string

    #Create accessor
    def get_side(self):
        return self.__side

    #Create mutator
    def set_side(self, new_side):
        #Ensure side is positive
        if new_side > 0:
            self.__side = new_side
        else:
            print("Invalid side. Side not changed.")

    #Define calculate perimeter method
    def calc_perimeter(self):

        #Calculate circ
        perimeter = 4 * self.__side

        return perimeter

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = self.__side**2

        return area
