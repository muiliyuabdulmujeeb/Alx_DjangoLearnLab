python command:
```
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book)
print(book.title)
print(book.author)
print(book.publication_year)
```

comment: Used the dot notation to get each column of the table

response:
```
Book object (2)
1984
George Orwell
1949
```
