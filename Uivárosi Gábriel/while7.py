

import random
f = 20
d = 0
while f != 0:
  random_szam = random.randint(1,12)
f -= 1

if random_szam % 3 == 0:
     print(random_szam)
     d += 1