fileName = 'rosalind_ba9k.txt'
with open(fileName) as file:
    content = file.readlines()

transform = content[0]
index = int(content[1])

character = transform[index]

occurenceNumber = 0

for i in range(0, index + 1):
    if transform[i] == character:
        occurenceNumber += 1

fList = ''.join(sorted(transform)[1:])

searchNumber = 0
for i in range(0, len(fList)):
    if fList[i] == character:
        searchNumber += 1
        if searchNumber == occurenceNumber:
            print i
            break
