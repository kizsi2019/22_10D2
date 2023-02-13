'''
polc = []

polc.append({
    'szerzo': 'William Golding',
    'cim': 'A legyek ura'
})

polc.append({
    'szerzo': 'Ottlik Géza',
    'cim': 'Iskola a határon'
})

print(polc)
'''

'''
Halmaz (set):
- rendezetlen (elemeknek nincs indexe)
- egy elem csak egyszer szerepelhet
- többféle típust tárolhat egyszerre is
- a halmaz eleme maga nem változtatható meg
'''

'''
reggeli = {'tea', 'vaj', 'piritós'}
ebed = set(['halászlé', 'kenyér', True])
reggeli.add('lekvár')
reggeli.remove('sajt')
reggeli.discard('sajt')
'''
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

# metszet
print(reggeli & ebed)
# unio
print(reggeli | ebed)
# különbség
print(reggeli - ebed)
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)
'''
    Tuple:
    - rendezett (elemeknek indexe van)
    - egy elem többször szerepelhet
    - többféle típust tárolhat egyszerre is
    - NEM megváltoztatható adattípus
      (NEM lehet az elemeket módosítani, elemek sorrnedjét, számát változtatni)
    '''
'''
# tuple létrehozása
kozeppont = (0, 5)

# de ez is tuple-t eredmenyez
kozeppont = 0, 5

# hivatkozás a tuple egy elemére
print(kozeppont[1])  # 5

# tuple "kicsomagolása"
x, y = kozeppont  # x értéke: 0, y értéke: 5
print(x)
'''
'''
import  random
valasz = set()
lotto = set()
for i in range(5):
    rand = random.randint(0, 10)
    lotto.add(rand)
for sz in range(5):
    val = int(input("tipp?"))
    valasz.add(val)
print(valasz & lotto)
'''
R = int(input("R"))
G = int(input("G"))
B = int(input("B"))
legnagy = 0
szin = R, G, B
aszam = 0
a_szam = 0
if szin[1] > 0:
    print("van zöld")
for sz in szin:
    aszam = aszam + 1
    if sz > legnagy:
        legnagy =  sz
        a_szam = aszam
if a_szam == 1:
    legnagyobbszin = "Red"
elif a_szam == 2:
    legnagyobbszin = "Green"
else:
    legnagyobbszin = "blue"

print(legnagyobbszin)
legkissebb = 99999999999999999
eszam = 0
e_szam = 0
for ssz in szin:
    eszam = eszam + 1
    if ssz < legkissebb:
        legkissebb = ssz
        e_szam = eszam
if e_szam == 1:
    legkisebbszin = "RED"
elif e_szam == 2:
    legkisebbszin = "Green"
else:
    legkisebbszin = "Blue"
print(legkisebbszin)

