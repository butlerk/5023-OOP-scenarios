import turtle
import drawing

'''
    The mainline of the drawing program starts here
'''

# A list of shapes, which we'll loop through later in the program to draw our shapes
shapes = []
# Creates an instance of a turtle which will be used for drawing the shapes
my_turtle = turtle.Turtle()

# Adds the blue triangle to the list of shapes
bt_points = [ drawing.Point(-120, 200), drawing.Point(-20, 200), drawing.Point(-70, 100) ]
blue_triangle = drawing.Shape('blue', bt_points, my_turtle)
shapes.append(blue_triangle)


# Adds the orange square to the list of shapes
os_points = [ drawing.Point(-200, -100), drawing.Point(-200, -150), drawing.Point (-150, -150), drawing.Point(-150, -100) ]
orange_square = drawing.Shape('orange',  os_points, my_turtle)
shapes.append(orange_square)


# Adds the red triangle to the list of shapes
rt_points = [ drawing.Point(100, 200), drawing.Point(250, 200), drawing.Point(175, 50)]
red_triangle = drawing.Shape('red',  rt_points, my_turtle)
shapes.append(red_triangle)

# Adds a purple octagon to the list of shapes
po_points = [ drawing.Point(108, -193), drawing.Point(92, -193), drawing.Point(82, -183), drawing.Point(82, -167), drawing.Point(92, -157), drawing.Point(108, -157), drawing.Point(118, -167), drawing.Point(118, -183)]
purple_octagon = drawing.Shape('purple',  po_points, my_turtle)
shapes.append(purple_octagon)
    


# Draws all of the shapes that are in the list in the window
for shape in shapes:
    # TODO: Modify the next line to use the draw method on the Shape object
    shape.draw()
    
# This line will mean that the Turtle window won't close until we click
turtle.Screen().exitonclick() 