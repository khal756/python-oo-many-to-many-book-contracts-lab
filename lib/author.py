class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        from lib.contract import Contract  # deferred import
        return [c for c in Contract.all if c.author == self]

    def books(self):
        from lib.contract import Contract  # deferred import
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from lib.contract import Contract  # deferred import
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())