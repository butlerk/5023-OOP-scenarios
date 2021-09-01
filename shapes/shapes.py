import math

class Rectangle:
    length:float
    width:float
    area:float
    perimeter:float

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(length, width):
        perimeter = 2 * length + 2 * width
        return perimeter
    
    def calculate_area(length,width):
        area = length * width
        return area
       
        
class Circle:
    radius:float
    area:float

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(radius):
        area = (radius * radius) * math.pi 
        return area
        #(f'Circle area: {round(area,2)}')
    
    def calculate_circumference(radius):
        circumference = (radius * 2) * math.pi 
        return circumference
        #(f'Circle area: {round(area,2)}')

