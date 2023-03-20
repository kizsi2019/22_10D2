import datetime


class Student:

    def __init__(self, name, shclass, age):
        self.name = name
        self.shclass = shclass
        self.age = age


    def bage(self):
        return datetime.datetime.now().year - self.age

    def intro(self):
        print(f'Szia, a nevem {self.name}, {self.age} éves vagyok, a {self.shclass} osztályba járok')

stud = Student()


