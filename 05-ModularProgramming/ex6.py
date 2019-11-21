import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    age_count = 0
    for row in reader:
        if i == 0:
            print(f"{'#':<5} {row[0].upper():<15} {row[1].upper():<12} {row[2].upper():<6} {row[3].upper()}")
            print('=' * 60)
        else:
            print(f"{i:<5} {row[0].upper():<15} {row[1]:<12} {row[2]:<6} {row[3]}")
            age_count += int(row[2])
        i += 1
    print(f"\nŚrednia arytmetyczna wieku pracowników wynosi: {age_count / (i - 1)}")