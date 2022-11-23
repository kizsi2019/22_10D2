Y = "Y"
Liszt = []
szav = ''
Leghoszabb = 0
while Y != "":
  Y =  input("Agy meg egy szót")
  Liszt.append(Y)
for szo in Liszt:

     if len(szo) > Leghoszabb:
       szav = szo
       Leghoszabb = len(szo)
       
print("A leghoszabb szó:",szav)       
print("Hosza:", Leghoszabb)