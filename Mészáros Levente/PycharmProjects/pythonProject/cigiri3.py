def paros_e(x, *lista):

   for szam in lista:
       if szam % 2 == 0:
         ok = True
       else:
          ok = False

   return ok


print(paros_e(5,3))