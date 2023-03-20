class School:

    def __init__(self, subjects):
        self.subjects = subjects



class Student:

    def __init__(self, name, shclass):
        self.name = name
        self.shclass = shclass


class Teacher(School):

    def __init__(self, name):
        self.name = name
        super()

