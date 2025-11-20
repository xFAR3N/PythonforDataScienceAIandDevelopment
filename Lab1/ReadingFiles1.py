example1 = "example1.txt"

file1 = open(example1, "r")

print(file1.name)

print(file1.mode)

FileContent = file1.read()
print(FileContent)

file1.close()