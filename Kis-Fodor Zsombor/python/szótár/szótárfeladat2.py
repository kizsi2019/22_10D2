szisza = {
    'Neve': 'Garfield',
    'Életkora':'1'
}

print(szisza)

wannachange = input('melyik adatot akarod megváltoztatni? (név,kor)')

if wannachange == 'név':
    szisza['Neve'] = input('Új név')
else:
    szisza['Életkora'] = input('Új kor')

print(szisza)