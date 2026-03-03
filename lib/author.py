class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        self.name = name
        Author.all.append(self)

    def contracts(self):
        from contract import Contract
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from contract import Contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())