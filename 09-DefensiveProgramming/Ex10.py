try:
    with open('NoEducation.txt') as file:
        read_file = file.read()
        print(read_file)
except:
    print("There's no such file or directory")