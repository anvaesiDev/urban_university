grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_grades = {}
i = 0

students = list(students)
students.sort()

# решил сделать универсальное решение, не знаю как сделать без цикла
while i < len(students):
    students_grades.update({students[i]: sum(grades[i]) / len(grades[i]) })
    i += 1

print(students_grades)
