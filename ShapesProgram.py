#Program header goes here

#Import relevant files here
import shape
import circle
import triangle
import square

#Define main function
def main():

    #CREATE A SHAPE: red, border (1), name: Generic Shape
    my_shape = shape.Shape("red", 1, "Generic Shape")

    #CREATE A CIRCLE: blue, border (2), name: Circle
    my_circle = circle.Circle("blue", 2, "Circle")

    #CREATE A SQUARE: yellow, border (3), name: Square
    my_triangle = triangle.Triangle("yellow", 3, "Triangle")

    #CREATE A TRIANGLE: orange, border (4), name: Triangle
    my_square = square.Square("orange", 4, "Square")

    #ADD CODE TO SET THE APPROPRIATE ATTRIBUTES OF EACH SUBCLASS:
    #CIRCLE: RADIUS = 4
    #SQUARE: SIDE = 5
    #TRIANGLE: BASE = 4, HEIGHT = 10
    my_circle.set_radius(10)
    my_triangle.set_height(5)
    my_triangle.set_base(4)
    my_square.set_side(10)

    #ADD CODE TO PRINT THE VALUES OF EACH SHAPE, INCLUDING SHAPE
    shapes_list = []
    shapes_list.append(my_shape)
    shapes_list.append(my_circle)
    shapes_list.append(my_triangle)
    shapes_list.append(my_square)

    for shapes in shapes_list:
        print(shapes)
      

    #ADD CODE TO PRINT THE AREA OF THE CIRCLE, SQUARE, AND TRIANGLE

    for shapes in shapes_list:
        if isinstance(shapes, circle.Circle):
            print("Circle circumference is:", shapes.calc_circumference())
        elif isinstance(shapes, triangle.Triangle):
            print("Triangle area:", shapes.calc_area())
        elif isinstance(shapes, square.Square):
            print("Square perimeter:", shapes.calc_perimeter())
            
            
    print(my_circle.calc_area())
    print(my_square.calc_area())
    print(my_triangle.calc_area())

#Call main function
main()
