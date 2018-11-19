#Class header goes here

#Import relevant .py files
import shape

#Define constants
PI = 3.14

#Define the Circle class - inherits from Shape
class Circle(shape.Shape):

    #Define the initializer method
    def __init__(self, color, border, name):
        #Call initializer of parent and pass parent attribute values
        super().__init__(color, border, name)

        #Set default values for Circle attributes
        self.__radius = 1

    #Define __str__ method
    def __str__(self):
        #Use __str__() from parent and add Circle attributes
        string = super().__str__() + " Radius: " + str(self.__radius)
        
        return string

    #Create accessor
    def get_radius(self):
        return self.__radius

    #Create mutator
    def set_radius(self, new_radius):
        #Ensure radius is positive
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Invalid radius. Radius not changed.")
    
    #Define calculate circumference method
    def calc_circumference(self):

        #Calculate circ
        circ = PI * 2 * self.__radius

        return circ

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = PI * self.__radius**2

        return area
