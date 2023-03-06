books = []

while True:
    author = input("Mi a könyv szerzője? ")
    if not author:
        break
    title = input("Mi a könyv címe? ")
    book = {
        "author": author,
        "title": title
    }
    books.append(book)

print("A bevitt könyvek:")
for book in books:
    print("Szerző: " + book["author"] + ", Cím: " + book["title"])
