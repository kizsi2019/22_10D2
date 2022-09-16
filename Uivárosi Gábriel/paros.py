szam =  int(input("adjon meg egy páros számot!"))
f = False
if szam % 2 == 0:
     print("köszönöm")

else:
     while f == False:
         szam = int(input("kérem adjon meg egy PÁROS számot!"))
         if szam %2 == 0:
             f = True

print("köszönöm")