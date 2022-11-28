Y = "Y"
Liszt = []

Leghoszabb = 0
Legrövidebb = 9999

while Y != "":
  Y =  input("Agy meg egy szót")
  Liszt.append(Y)
szav = Liszt[0]
szak = Liszt[0]

for szo in Liszt:

      if len(szo) > Leghoszabb:
       szav = szo
       Leghoszabb = len(szo)
      else:
        if len(szo) != 0:
          if len(szo) < Legrövidebb:
            szak = szo
            Legrövidebb = len(szo) 
print("A lista elemei:",Liszt)       
print("A leghoszabb szó:",szav)       
print("Hosza:", Leghoszabb)
print("Legrövidebb szó:",szak)
print("Hosza:",Legrövidebb)