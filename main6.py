# 1. Створити ієрархію класів для опису академії.
#
#    Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
#    Продумати архітектуру: реалізувати принципи ООП


# v1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Teacher(Person):
#     def __init__(self, name, age, expertise):
#         super().__init__(name, age)
#         self.expertise = expertise
#
# class Student(Person):
#     def __init__(self, name, age, courses):
#         super().__init__(name, age)
#         self.courses = courses
#
# class Subject:
#     def __init__(self, name, teacher, students):
#         self.name = name
#         self.teacher = teacher
#         self.students = students
#
# class Academy:
#     def __init__(self, name, subjects):
#         self.name = name
#         self.subjects = subjects


# v2

class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

    def display_info(self):
        print(f"Name: {self._name}, Surname: {self._surname}, Age: {self._age}")


class Teacher(Person):
    def __init__(self, name, surname, age, subjects_taught):
        super().__init__(name, surname, age)
        self._subjects_taught = subjects_taught

    def display_info(self):
        super().display_info()
        print(f"Subjects Taught: {', '.join(self._subjects_taught)}")

    def conduct_lesson(self):
        print(f"Teacher {self._name} is conducting a lesson.")


class Student(Person):
    def __init__(self, name, surname, age, course, group):
        super().__init__(name, surname, age)
        self._course = course
        self._group = group

    def display_info(self):
        super().display_info()
        print(f"Course: {self._course}, Group: {self._group}")

    def do_homework(self):
        print(f"Student {self._name} is doing homework.")


class Subject:
    def __init__(self, name, description, teacher, students):
        self._name = name
        self._description = description
        self._teacher = teacher
        self._students = students

    def display_info(self):
        print(f"Subject: {self._name}, Description: {self._description}")
        print("Teacher:")
        self._teacher.display_info()
        print("Students:")
        for student in self._students:
            student.display_info()


class Academy:
    def __init__(self):
        self._teachers = []
        self._students = []
        self._subjects = []

    def add_teacher(self, teacher):
        self._teachers.append(teacher)

    def add_student(self, student):
        self._students.append(student)

    def add_subject(self, subject):
        self._subjects.append(subject)

    def display_statistics(self):
        print(f"Number of Teachers: {len(self._teachers)}")
        print(f"Number of Students: {len(self._students)}")
        print(f"Number of Subjects: {len(self._subjects)}")


# Тестування
teacher1 = Teacher("John", "Doe", 35, ["Math", "Physics"])
student1 = Student("Alice", "Smith", 20, 2, "A")
subject1 = Subject("Mathematics", "Advanced Calculus", teacher1, [student1])

academy = Academy()
academy.add_teacher(teacher1)
academy.add_student(student1)
academy.add_subject(subject1)

teacher1.conduct_lesson()
student1.do_homework()
subject1.display_info()

academy.display_statistics()