class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def get_avg_hw_grade(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res = sum(avg)/len(avg)
        return round(res, 2)

    def __str__(self):
        print()
        print('Студент:')
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
                        f'Средняя оценка за домашние задания: {self.get_avg_hw_grade()}\n'\
                        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        print()
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.get_avg_hw_grade() < other.get_avg_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_lc_grade(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res = sum(avg)/len(avg)
        return round(res, 2)

    def __str__(self):
        print()
        print('Лектор:')
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_lc_grade()}'
        print()
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.get_avg_lc_grade() < other.get_avg_lc_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        print()
        print('Проверяющий:')
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        print()
        return some_reviewer


def get_avg_all_hw_grade(students, course):
    sum_grades = []
    for student in students:
        if (isinstance(student, Student) and course in student.grades):
            sum_grades.extend(student.grades[course])
        else:
            print('Error. Try again.')
            return
    return round(sum(sum_grades) / len(sum_grades), 2)

def get_avg_all_lc_grade(lecturers, course):
    sum_grades = []
    for lecturer in lecturers:
        if (isinstance(lecturer, Lecturer) and course in lecturer.grades):
            sum_grades.extend(lecturer.grades[course])
        else:
            print('Error. Try again.')
            return
    return round(sum(sum_grades) / len(sum_grades), 2)


# Создаем 2 экземпляра класса Student
first_student = Student('Ivan', 'Ivanov', 'male')
first_student.courses_in_progress += ['Python', 'JavaScript']
first_student.finished_courses += ['EnglishDom', 'Git']

second_student = Student('Danil', 'Danilov', 'male')
second_student.courses_in_progress += ['Python', 'Java']
second_student.finished_courses += ['EnglishDom']


# Создаем 2 экземпляра класса Lecturer
first_mentor = Lecturer('Roman', 'Romanov')
first_mentor.courses_attached += ['Python', 'JavaScript']

second_mentor = Lecturer('Ilya', 'Ilyin')
second_mentor.courses_attached += ['Python','Java']


# Создаем 2 экземпляра класса Reviewer
first_reviewer = Reviewer('Alexander','Alexandrov')
first_reviewer.courses_attached += ['Python', 'JavaScript']

second_reviewer = Reviewer('Peter','Petrov')
second_reviewer.courses_attached += ['Python', 'JavaScript']


# Ревьюер оценивает ДЗ студента
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 6)

second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 4)


# Студент оценивает преподавателя
first_student.rate_lc(first_mentor, 'Python', 6)
first_student.rate_lc(first_mentor, 'Python', 7)
first_student.rate_lc(first_mentor, 'Python', 8)

second_student.rate_lc(second_mentor, 'Python', 8)
second_student.rate_lc(second_mentor, 'Python', 9)
second_student.rate_lc(second_mentor, 'Python', 10)


student_list = [first_student, second_student]
lecturer_list = [first_mentor, second_mentor]


print(first_student)
print(second_student)

print(first_mentor)
print(second_mentor)

print(first_reviewer)
print(second_reviewer)

print(get_avg_all_hw_grade(student_list, 'Python'))
print(get_avg_all_lc_grade(lecturer_list, 'Python'))

print(first_student > second_student)
print(first_mentor < second_mentor)