import math

a = int(input('Add meg az egyik befogót!'))
b = int(input('Add meg a másik befogót!'))
c = math.pow(a, 2)+math.pow(b, 2)
print('A befogók négyzetének összege:', c, 'cm')
print('Az eredmény:', round(math.sqrt(c)), 'cm')