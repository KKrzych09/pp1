class Ebook():
    def __init__(self, title, author, pages_amount):
        self.title = title
        self.author = author
        self.pages_amount = pages_amount
        self.is_open = False
        self.page_no = 1
    
    def opened(self):
        self.is_open = True
    
    def closed(self):
        self.is_open = False
    
    def show_status(self):
        if self.is_open:
            print(f'Książka {self.title} autora imieniem {self.author} licząca {self.pages_amount} stron jest otwarta na stronie: {self.page_no}')
        else:
            print('Książka jest zamknięta!')
    def read_page(self):
        if self.is_open:
            self.page_no += 1
        else:
            print('Nie możesz czytać dalej bo książka jest zamknięta!')
    
    def read_ten_pages(self):
        if self.is_open:
            self.page_no += 10
        else:
            print('Nie możesz czytać dalej bo książka jest zamknięta!')
