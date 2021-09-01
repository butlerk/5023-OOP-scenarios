class Student:
    english_mark:int
    science_mark:int
    mathematics_mark:int
    completed_assessments:bool
    name:str
    average_mark: float
    average:float
    total_mark:int

    def __init__(self, name, english_mark, science_mark, mathematics_mark, completed_assessments):
        self.name = name
        self.english_mark = english_mark
        self.science_mark = science_mark
        self.mathematics_mark = mathematics_mark
        self.completed_assessments = completed_assessments        

    def calc_average(a, b, c):
        total_mark = a + b + c
        average = round(total_mark/3)
        return(average)

        







