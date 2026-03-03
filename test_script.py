from lib.author import Author
from lib.book import Book
from lib.contract import Contract

# Create authors and books
a1 = Author("Alice")
a2 = Author("Bob")
b1 = Book("Python Mastery")
b2 = Book("Advanced Python")

# Sign contracts
a1.sign_contract(b1, "2026-03-03", 1000)
a1.sign_contract(b2, "2026-03-03", 1500)
a2.sign_contract(b1, "2026-03-03", 2000)

# Print checks
print(a1.books())           # [b1, b2]
print(b1.authors())         # [a1, a2]
print(a1.total_royalties()) # 2500
print(Contract.contracts_by_date("2026-03-03"))  # all 3 contracts