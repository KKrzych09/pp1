import csv
import statistics

with open('employees.csv', newline = '') as file:
    reader = csv.reader(file)
    i = 0
    lista = []
    for row in reader:
        if i > 0:
            lista.append(int(row[2])) #dodaje elementy row[2] czyli 'age' do pustej listy zeby móc użyć modułu statistics
        i += 1
    print(f'Srednia arytmetyczna wieku pracowników: {statistics.mean(lista)}')
    print(f'Mediana wieku pracowników: {statistics.median(lista)}')
    print(f'Odchylenie standardowe wieku pracowników: {statistics.pstdev(lista)}')
        