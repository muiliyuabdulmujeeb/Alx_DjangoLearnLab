python command:
```
from bookshelf.models import Book

book = Book.objects.get(id= 2)
book.delete()

print(book)
```

response: 
```
(1, {'bookshelf.Book': 1})
Book object (None)
```

comment: book was successfully deleted