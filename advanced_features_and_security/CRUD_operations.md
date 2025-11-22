Query1:
```
from bookshelf.models import Book
new_book = Book(title= "1984", author= "George Orwell", publication_year= 1949)
new_book.save()
```

Response1:
Null

Query2:
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book)
print(book.title)
print(book.author)
print(book.publication_year)
```

Response2:
```
Book object (2)
1984
George Orwell
1949
```

Query3:
```
from bookshelf.models import Book

book = Book.objects.get(id= 2)
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
```

Response3:
Nineteen Eighty-Four

Query4:
```
from bookshelf.models import Book

book = Book.objects.get(id= 2)
book.delete()

print(book)
```

Response4:
```
(1, {'bookshelf.Book': 1})
Book object (None)
```