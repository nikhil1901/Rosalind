def lastToFirst(lastColumn, index):
    transform = lastColumn

    character = transform[index]
    # print "character", character
    occurenceNumber = 0

    for i in range(0, index + 1):
        if transform[i] == character:
            occurenceNumber += 1

    fList = ''.join(sorted(transform))
    # print "transform", len(transform)
    # print "fList", len(fList)

    searchNumber = 0
    for i in range(0, len(fList)):
        if fList[i] == character:
            searchNumber += 1
            if searchNumber == occurenceNumber:
                return i
                break
    return 0

def bwMatching(lastColumn, pattern):
    top = 0
    bottom = len(lastColumn) - 1
    # print "bottom", bottom
    while top <= bottom:
        if pattern != "":
            symbol = pattern[-1]
            pattern = pattern[:-1]
            # print "symbol", symbol
            if symbol in lastColumn:
                topIndex = -1
                bottomIndex = -1
                for i  in range(top, bottom + 1):
                    if lastColumn[i] == symbol:
                        if topIndex == -1:
                            topIndex = i
                        bottomIndex = i
                # print "topIndex", topIndex, bottomIndex
                if topIndex == -1:
                    return 0
                # print topIndex, bottomIndex
                top = lastToFirst(lastColumn, topIndex)
                bottom = lastToFirst(lastColumn, bottomIndex)
                # print top, bottom
            else:
                return 0
        else:
            return bottom - top + 1




fileName = 'rosalind_ba9l.txt'
with open(fileName) as file:
    content = file.readlines()


# print lastToFirst('T$GACCA', 3)


lastColumn = content[0][:-1]
patterns = content[1].split()
output = list()
for index in range(0, len(patterns)):
    # print patterns[index]
    output.append(bwMatching(lastColumn, patterns[index]))

# print "".join(output)
print(" ".join(map(str,output)))
