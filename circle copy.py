#Class header

PI = 3.14

class Circle:
    #Define __init__
    def __init__(self):
        #Define attributes
        self.radius = 1
        self.color = "Blue"
        self.border = 1

    #Define calc_area method
    def calc_area(self):
        area = PI * self.radius**2
        return area

    #Define calc_circumference
    def calc_circumference(self):
        circ = 2 * PI * self.radius
        return circ

    def update_color(new_color)
        self.color = new_color
