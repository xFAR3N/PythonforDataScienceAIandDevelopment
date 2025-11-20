example = 'Example2.txt'

with open(example, 'w') as writefile:
    writefile.write('This is line A')

with open(example, 'w') as writefile:
    writefile.write('This is line A\n')
    writefile.write('This is line B\n')

with open(example, 'r') as file:
    print(file.read())

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open(example, 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open(example, 'r') as writefile:
    print(writefile.read())

with open(example, 'a') as writefile:
    writefile.write("This is line C\n")
    writefile.write("This is line D\n")
    writefile.write("This is line E\n")

with open(example, 'a+') as writefile:
    writefile.write("This is line E\n")
    print(writefile.read())

with open(example, 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))