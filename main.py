#Объявление класса student
class Student:
    def __init__(self, name, surname, gender): #Инициализация класса student
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):   #Переопределение магического метода __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.mid_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __eq__(self, other):  #Переопределение метода сравнения __eq__
        return self.mid_grade() == other.mid_grade()

    def __lt__(self, other):  #Переопределение метода сравнения __lt__
        return self.mid_grade() < other.mid_grade()

    def grade_lector(self, lector, course, grade):  #Метод добавляющий возможность оценки лектора за курс
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self):  #Метод возвращающий средний балла студента
        mid = 0.0
        count = 0
        for course in self.grades.values():
            count += len(course)
            for grade in course:
                mid += grade

        if count != 0:
            return mid / count
        else:
            return 0.0

#Объявление родительского класса Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade): #Метод добавляющий возможность выставления оценки студенту
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#Объявление дочернего класса Lecturer класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades={}            #Добавление параметра grades для хранения оценок от студентов

    def __str__(self):       #Переопределение магического метода __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.mid_grade()}\n')

    def __eq__(self, other): #Переопределение метода сравнения __eq__ для сравнения преподавтелей по среднему баллу
        return self.mid_grade() == other.mid_grade()

    def __lt__(self, other):  #Переопределение метода сравнения __lt__ для сравнения преподавтелей по среднему баллу
        return self.mid_grade() < other.mid_grade()

    def mid_grade(self): #Метод возвращающий средний балла лектора
        mid = 0.0
        count = 0

        for course in self.grades.values():
            count += len(course)
            for grade in course:
                mid += grade
        if count != 0:
            return mid / count
        else:
            return 0.0

class Reviewer(Mentor): #Объявление класса Reviewer
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def __str__(self): #Переопределение магического метода __str__
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

#Функция возвращает средний балл лекторов по указанному курсу из списка полученного на вход
def lectors_mid_grade(lectors, course):
    mid = 0.0
    count = 0
    for lector in lectors:
        count += len(lector.grades.get(course))
        for grade in lector.grades.get(course):
            mid += grade

    return mid/count

#Функция возвращает средний балл студентов по указанному курсу из списка полученного на вход
def students_mid_grade(students, course):
    mid = 0.0
    count = 0
    for student in students:
        count += len(student.grades.get(course))
        for grade in student.grades.get(course):
            mid += grade

    return mid/count

#Создаем два экзэмпляра класса student
best_student = Student('Ruoy', 'Eman', 'your_gender')
not_best_student = Student('Roy', 'Harper', 'your_gender')

best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
not_best_student.courses_in_progress += ['Python']

#Создаем два экзэмпляра класса Lecturer
lecturer_1 = Lecturer('Tomas', 'Henderson')
lecturer_2 = Lecturer('James', 'Bold')
#Добавляем активные курсы лекторам 1 и 2
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python']

#Создаем два экзэмпляра класса Reviewer
reviewer_1 = Reviewer('Gignger', 'Bread')
reviewer_2 = Reviewer('Bruce', 'Branner')
#Добавляем активные курсы проверяющим 1 и 2
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

#Проверяющий 1 выставляет оценку студентам по курсу Python
reviewer_1.rate_hw(best_student, 'Python', 10.0)
reviewer_1.rate_hw(best_student, 'Python', 7.0)

reviewer_1.rate_hw(not_best_student, 'Python', 6.0)
reviewer_1.rate_hw(not_best_student, 'Python', 7.0)
#Студенты выставляют оценки лекторам
best_student.grade_lector(lecturer_1, 'Python', 9.0)
not_best_student.grade_lector(lecturer_1, 'Git', 7.0)
not_best_student.grade_lector(lecturer_2, 'Python', 8.4)
#Вывод информации о преподавателях и студентах
print(lecturer_1)
print(lecturer_2)
print(best_student)
print(not_best_student)
print(reviewer_1)
print(reviewer_2)
#Вывод результата сравнения студентов
print(f'Резултат сравнения студентов по среднему баллу (>) {best_student > not_best_student}')
print(f'Резултат сравнения студентов по среднему баллу (<) {best_student < not_best_student}')
print(f'Резултат сравнения студентов по среднему баллу (==) {best_student == not_best_student}')
#Вывод результата сравнения лекторов
print(f'Резултат сравнения студентов по среднему баллу (==) {lecturer_1 == lecturer_2}')
print(f'Резултат сравнения студентов по среднему баллу (>) {lecturer_1 > lecturer_2}')
#Вывод среднего балла преподавателей и студентов по курсу
print('Средняя оценка лекторов по курсу Python: ' + str(lectors_mid_grade([lecturer_1, lecturer_2], 'Python')))
print('Средняя оценка студентов по курсу Python: ' + str(students_mid_grade([best_student, not_best_student], 'Python')))

