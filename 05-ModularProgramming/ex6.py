import csv
with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    headline = csv.reader(f)
    i = 1
    print('#', 'NAME','SURNAME','AGE','EMAIL')
    print('=================================')
    for row in reader:
        print(i, row['name'].upper(), row['surname'], row['age'], row['email'])
        i += 1