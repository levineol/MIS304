#Program header

import circle

def main():
    my_circle = circle.Circle()
    new_color = input("What color is the circle? ")
    my_circle.update_color(new_color)
    print(my_circle.color)
    act_area = my_circle.calc_area()
    print(act_area)
