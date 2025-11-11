#Exercise 1 : Student Grade Summary
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages = {}
for name, grade in student_grades.items():
    average = sum(grade) / len(grade)
    student_averages[name] = average

student_letter_grades = {}    
for name, average in student_averages.items():
    if average >=90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'            
    student_letter_grades[name] = [letter_grade]
#print(student_letter_grades.values())


total_average = sum(student_averages.values())
num_students = len(student_averages)
class_average = total_average / num_students
print(f'Class average: {class_average:.2f}')

# print(student_averages)
# print(student_letter_grades)
# print(class_average)

for name in student_grades:
    print(f'{name}: average: {student_averages[name]:2f}, grade: {student_letter_grades[name]}')


