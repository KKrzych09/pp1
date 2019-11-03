with open('students.txt') as file:
    file.readline()
    for line in file:
        x = line.split(",")
        if int(x[2]) < 30:
            print(f"{x[0]:<8} {x[1]:<8} {x[4]}", end='')