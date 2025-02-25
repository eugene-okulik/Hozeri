class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, book_name, author, pages_amount):
        self.book_name = book_name
        self.author = author
        self.pages_amount = pages_amount
        self.ISBN = None
        self.is_reserved = False

    def format_book_details(self):
        details = (f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_amount}, '
                   f'материал: {self.page_material}')
        return f'{details}, зарезервирована' if self.is_reserved else details


books = [
    Book('Война и мир', 'Лев Толстой', 2144),
    Book('Анна Каренина', 'Лев Толстой', 864),
    Book('Детство', 'Лев Толстой', 254),
    Book('Кавказский пленник', 'Лев Толстой', 500),
    Book('Отрочество', 'Лев Толстой', 600)
]

books[1].ISBN = 9783127123207
books[1].is_reserved = True

for book in books:
    print(book.format_book_details())


class SchoolBook(Book):
    def __init__(self, book_name, author, pages_amount, subject, group):
        super().__init__(book_name, author, pages_amount)
        self.subject = subject
        self.group = group
        self.is_workbook = False

    def format_book_details(self):
        details = (f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_amount}, '
                   f'предмет: {self.subject}, класс: {self.group}')
        return f'{details}, зарезервирована' if self.is_reserved else details


school_books = [
    SchoolBook('Геометрия', 'Геометриев Лев', 570, 'Геометрия', '8A'),
    SchoolBook('Алгебра', 'Алегебров Никита', 400, 'Алгебра', '7Б'),
    SchoolBook('Биология', 'Биологов Олег', 800, 'Биология', '10В')
]

school_books[1].is_reserved = True
school_books[1].is_workbook = True

for school_book in school_books:
    print(school_book.format_book_details())
