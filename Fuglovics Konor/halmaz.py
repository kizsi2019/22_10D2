breakfast = {'tea', 'butter', 'bread'}

lunch = set()
lunch = set(['halászlé', 'kenyér', True])

breakfast.add('jam')
breakfast.pop()
#breakfast.remove('cheese') <-- Nem működik
breakfast.discard('cheese')

print(breakfast)
print(lunch)

print(breakfast & lunch)
print(breakfast | lunch)
print(breakfast - lunch)
print(breakfast ^ lunch)