storage = {}
print(storage)

student = {
    'first_name': 'Kiss',
    'last_name': 'Péter',
    'age': 17,
    'menza': True
}
print(student['age'])
print(student.get('kollegista', 'nem'))
print('last_name' in student)

for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.itens():
    print(key, value)