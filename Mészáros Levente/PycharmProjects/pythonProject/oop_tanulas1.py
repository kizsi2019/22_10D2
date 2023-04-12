kor_01 = {
    'kozeppont': (2, 5),
    'sugar': 5
}

def terulet(kor):
    return kor['sugar'] * pow(3.14, 2)

def kerulet(kor):
    return (kor['sugar'] * 2) * 3.14

print(terulet(kor_01))
print(kerulet(kor_01))
