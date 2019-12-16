from operator import attrgetter
class Student():
    
    def __init__(self, name, surname, album_nr):
        self.name = name
        self.surname = surname
        self.album_nr = album_nr
    
    def __str__(self):
        return 'Student: ' + self.name + ' ' + self.surname + ', ' + f'{self.album_nr}'
    
    def __eq__(self, other):
        if self.album_nr == other.album_nr:
            return 'Album numbers are the same.'
    
    def __lt__(self, other):
        if self.album_nr > other.album_nr:
            return f'Album number {self.album_nr} is bigger than album number {other.album_nr}'
        elif self.album_nr < other.album_nr:
            return f'Album number {self.album_nr} is smaller than album number {other.album_nr}'

student1 = Student('Anna', 'Tomaszewska', 141820)
student2 = Student('Wojciech', 'Zbych', 201003)
student3 = Student('Maja', 'Kowalska', 153202)
student4 = Student('Marek', 'Migiel', 138600)

students = [student1, student2, student3, student4]

for i in students:
    print(i)

students.sort(key = lambda student: student.album_nr)
print('\nStudents sorted by album number: ')
for j in students:
    print(j)

print(student1 < student2)

