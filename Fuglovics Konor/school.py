class School:
    def __init__(self, boys, girls):
        self.boys = boys
        self.girls = girls


scho = School('200', '400')


with open('numbers.txt', 'w', encoding='utf-8') as file:
    file.write(f'There are {scho.boys} boys and {scho.girls} girls in the school.')