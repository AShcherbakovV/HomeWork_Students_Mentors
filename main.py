class Student:
    def __init__(self, name, surname, gender):


        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades={}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student_2 = Student('Ruoy', 'Eman', 'your_gender')
best_student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Tomas', 'Henderson')
lecturer_2 = Lecturer('James', 'Bold')
lecturer_1.courses_attached += ['Python']

best_student.grade_lector(lecturer_1, 'Python', 9.0)
best_student_2.grade_lector(lecturer_1, 'Python', 7.0)

print(lecturer_1.grades)
print(best_student.grades)
