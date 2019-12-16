class Book():
    
    def __init__(self, pages, file):
        self.pages = pages
        self.file = file
        

class Electronic_book(Book):
    
    def __init__(self, file):
        super().__init__(file, file)
    
    def in_file(self):
        print(f'Your book is in {self.file} file.')
    
    
class Paper_book(Book):
    
    def __init__(self, pages):
        super().__init__(pages, pages)
    
    def pages_amount(self):
        print(f'Your book has {self.pages} pages.')
    
book1 = Electronic_book("'my book'")
book2 = Paper_book(330)

book1.in_file()
book2.pages_amount()