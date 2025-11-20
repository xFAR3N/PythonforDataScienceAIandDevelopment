from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

def cleanFiles(currentMem, exMem):
    with open(currentMem,'r+') as writefile:
        with open(exMem,'a+') as appendfile:
            writefile.seek(0)
            members = writefile.readlines()
            header = members[0]
            members.pop(0)
            inactive = [member for member in members if ('no' in member)]
            writefile.seek(0)
            writefile.write(header)
            for member in members:
                if member in inactive:
                    appendfile.write(member)
                else:
                    writefile.write(member)
            writefile.truncate()


cleanFiles(memReg,exReg)

headers = "Membership No  Date Joined  Active  \n"

with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())