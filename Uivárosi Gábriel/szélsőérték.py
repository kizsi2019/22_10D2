'''
LISZT = [12, 5, 4, 8, 9, 11, 10, 12, 6]
min = LISZT[0]
Max = LISZT[0]
for szam in LISZT:
    if szam < min:
        min = szam
    if szam > Max:
        Max = szam
print("Legkisebb",min)
print("Legnagyobb",Max)
'''
LISZT = []
yup = 0
yup2 = "?"
while yup2 != "":
    yup = int(input("AGYÁL SZÁMOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))
    yup2 = input("?")
    LISZT.append(yup)
min = LISZT[0]
Max = LISZT[0]
for szam in LISZT:
    if szam < min:
        min = szam
    if szam > Max:
        Max = szam
print("Legkisebb",min)
print("Legnagyobb",Max)