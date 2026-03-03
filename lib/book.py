class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        from lib.contract import Contract
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]