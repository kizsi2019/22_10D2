with open('text2.txt', 'w', encoding='utf-8') as file:
    file.write('apple, pear, strawberry')
    file.writelines(['apple\n', 'pear\n', 'strawberry\n'])