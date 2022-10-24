languages = ['Python', 'C', 'C++', 'Java']

languages.append('python')
print(languages)

languages_forwebsite = ['HTML', 'CSS', 'JavaScript']
languages.extend(languages_forwebsite)
print(languages)

languages.insert(1, 'Go')
print(languages)


