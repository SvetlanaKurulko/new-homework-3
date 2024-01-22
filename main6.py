# 1. Створити ієрархію класів для опису академії.
#
#    Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
#    Продумати архітектуру: реалізувати принципи ООП



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, expertise):
        super().__init__(name, age)
        self.expertise = expertise

class Student(Person):
    def __init__(self, name, age, courses):
        super().__init__(name, age)
        self.courses = courses

class Subject:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

class Academy:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects