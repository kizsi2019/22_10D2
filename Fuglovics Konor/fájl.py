source = open('car_list.csv')
source.readline()
source.readlines()
source.read()
for line in source:
    print(line)
source.close()
