books = []
while True:
    author = input("Adja meg a könyv szerzőjét (ha befejezte, nyomja meg az ENTER-t): ")
    if not author:
        break
    title = input("Adja meg a könyv címét: ")
    book = {
        "szerző": author,
        "cím": title
    }
    books.append(book)

print("\nA bevitt könyvek adatai:")
for i, book in enumerate(books):
    print(f"{i + 1}. szerző: {book['szerző']} / cím: {book['cím']}")
