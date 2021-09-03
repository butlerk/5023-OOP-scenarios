class Shape:
    def __init__(self, colour:str, points:list, myturtle):
        self.color = colour
        self.points = points
        self.myturtle = myturtle

    def draw_shape(my_turtle, shape):
           
        points = shape['points'] # gets list of points to draw
        # Put the pen up, so the turtle isn't drawing on the canvas and move to first point
        my_turtle.penup()
        my_turtle.goto(points[0])

        # Sets up colour for shape fill colour and puts pen down
        my_turtle.color(shape['colour'])
        my_turtle.begin_fill()
        my_turtle.pendown()

        # Moves around to different points to draw the shape
        for point in points:
            my_turtle.goto(point)
        
        # Moves to first point, to close the shape
        my_turtle.goto(points[0])
        my_turtle.end_fill()`
    
    
class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        
    
