
raktar = {}
print(raktar)

diak = {
	      'vezeteknev': 'Kiss',
	      'keresztnev': 'Péter',
	      'eletkor': 17,
	      'menza': True
    }
    
print(diak['eletkor'])
print(diak.get('eletkor'))

print(diak.get('kollegista', 'nem'))

print('keresztnev' in diak)
  
for kulcs in diak:
	 print(kulcs, diak[kulcs])
for ertek in diak.values():
        print(ertek)
for kulcs, ertek in diak.items():
        print(kulcs, ertek)