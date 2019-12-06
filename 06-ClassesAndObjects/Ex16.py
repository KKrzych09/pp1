import ebook_class


book = ebook_class.Ebook('Dawaj na ring', 'Mariusz Pudzianowski', 150)
book.opened()
book.show_status()
book.read_page()
book.show_status()
book.read_ten_pages()
book.show_status()
book.closed()
book.show_status()
book.read_page()
