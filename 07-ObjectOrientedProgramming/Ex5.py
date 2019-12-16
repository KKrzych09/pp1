class Songs():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f'{"Wykonawca:":<11}' + self.artist + '\n' + f'{"Utwór:":<11}' + self.title + '\n' + f'{"Album:":<11}' + self.album + '\n' + f'{"Rok:":<11}' + self.year + "\n"

utwor1 = Songs('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(utwor1)

utwor2 = Songs('Krzysztof Krawczyk', 'Mój przyjacielu', 'The Very Best Of..', '1999')
print(utwor2)

utwor3 = Songs('Kombi', 'Nasze pokolenie', 'c.d.', '2004')
print(utwor3)