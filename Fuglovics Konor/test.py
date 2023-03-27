class Student:

    def __init__(self, name, shclass):
        self.name = name
        self.shclass = shclass
    def info(self):
        print(f'Szia, a nevem {self.name}, {self.shclass} osztályba járok.')


class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def info(self):
        print(f'Szia, a nevem {self.name}, {self.subject}-t tanítok.')

stud = Student('Konor', '10D')
teach_1 = Teacher('Kiss Zsigmond', 'Informatika')
teach_2 = Teacher('Kósa Csilla', 'Angol')

stud.info()
teach_1.info()
teach_2.info()
print(teach_2.name)
print(stud.shclass)

with open('school.txt', 'w', encoding='utf-8') as file:
    file.write(stud.name)
    file.write(teach_1.name)
    file.write(teach_2.name)