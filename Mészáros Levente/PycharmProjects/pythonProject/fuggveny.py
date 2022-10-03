intervallum = ['-3', '-2', '-1', '0', '1', '2', '3', '4']

ertekkeszlet_elemek = []


x = 0
x_r = []
y_r = []
y = (2 * x - 5)

for i in range(4):
        if x <= 4:
            x_r.append(x)
            x += 1
            y += 2
            print(y)
            print(x)
            y_r.append(y)

print('ez az értékkészlet' ,y_r)
print('ez az értelmezési tartomány' ,x_r)























# y = 2x-3