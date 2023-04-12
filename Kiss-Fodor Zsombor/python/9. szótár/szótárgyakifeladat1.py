polc = []

író = None
Mű = None


while író != 'ENTER':
    író = input("könyv írója")
    Mű = input("könyv műve")
    if író != 'ENTER':
        polc.append({
            'Író:':író,
            'Mű címe:':Mű
        })

print(polc)