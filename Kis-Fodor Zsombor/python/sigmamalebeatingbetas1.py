vezi = input("giv keri")
keri = input("giv vezi")

with open('sex/köszönés.txt', 'a', encoding='utf-8') as avefile:
    print('ave', vezi, keri, file=avefile)
    print('', end='\n', file=avefile)