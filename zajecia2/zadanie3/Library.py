class Library:
    def __init__(self, books=None):
        if books:
            self.books = books
        else:
            self.books = dict({})

    def find_book(self, isbn : str) -> str | None:
        try:
            return self.books[isbn]
        except:
            return None
