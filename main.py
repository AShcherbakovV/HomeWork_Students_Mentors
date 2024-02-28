class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.mid_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    
    def grade_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self):
        mid = 0.0
        count = 0

        for course in self.grades.values():
            count += len(course)
            for grade in course:
                mid += grade

        return mid / count


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

    def __str__(self):
        mid = 0.0
        count = 0

        for course in self.grades.values():
            count += len(course)
            for grade in course:
                mid += grade

        mid = mid/count

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {mid}\n')



class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student_2 = Student('Ruoy', 'Eman', 'your_gender')
best_student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Tomas', 'Henderson')
lecturer_2 = Lecturer('James', 'Bold')
lecturer_1.courses_attached += ['Python']

lecturer_1.rate_hw(best_student, 'Python', 10.0)
lecturer_2.rate_hw(best_student, 'Python', 7.0)

best_student.grade_lector(lecturer_1, 'Python', 9.0)
best_student_2.grade_lector(lecturer_1, 'Python', 7.0)

print(lecturer_1)
print(best_student)
