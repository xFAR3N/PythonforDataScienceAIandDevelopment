example = 'example1.txt'
with open(example, 'r') as myfile:
    FileContent=myfile.read()
    print(FileContent)

with open(example, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

with open(example, "r") as file1:
    print("first line: " + file1.readline())

with open(example, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

with open(example, "r") as file1:
    FileasList = file1.readlines()
    print(FileasList[0])
    print(FileasList[1])
    print(FileasList[2])