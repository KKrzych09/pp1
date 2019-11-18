import statistics
salaries = [21600,4350,3920,5590,3250,4010]

a = statistics.mean(salaries)
b = statistics.median(salaries)
c = statistics.pstdev(salaries)

print(f'Srednia arytmetyczna wynosi {a}')
print(f'Mediana wynosi {b}')
print(f'Odchylenie standardowe wynosi {c}')
