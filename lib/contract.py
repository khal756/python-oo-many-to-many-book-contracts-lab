class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        from author import Author
        from book import Book

        if not isinstance(author, Author):
            raise TypeError("author must be Author instance")
        if not isinstance(book, Book):
            raise TypeError("book must be Book instance")
        if not isinstance(date, str):
            raise TypeError("date must be string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]