def osszegzo(x, *args):
   osszesen = 1
   for szam in args:
       osszesen = osszesen + szam
   return osszesen

print(osszegzo(1,5,5))
