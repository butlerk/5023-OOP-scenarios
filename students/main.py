from grades import Student

students = []
student1 = Student('Michael', 80, 70, 70, True)
students.append(student1)

student2 = Student('Angela', 60, 65, 75, True)
students.append(student2)

student3 = Student('Natalie', 60, 65, 100, False)
students.append(student3)

# Print the names and marks for each of the students
print('\nStudents:\n')
# TODO: Change code in loop to access Student objects' attributes, rather than dictionary
for student in students:
    print('---')
    print(f"Name: { student.name }")
    print(f"English: { student.english_mark }")
    print(f"Science: { student.science_mark }")
    print(f"Mathematics: { student.mathematics_mark }")
    average = Student.calc_average(student.english_mark, student.science_mark, student.mathematics_mark)
    print(f"Average mark: {average}")
    if student.completed_assessments == True:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print('---\n')








