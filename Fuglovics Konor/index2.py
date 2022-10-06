months = ['January', 'February', 'March', 'April', 'May', 'June']
'''
for month in months:
    month = month.upper()
    print(month)
print(months)
'''
for index in range(len(months)):
    months[index] = months[index].upper()
print(months)