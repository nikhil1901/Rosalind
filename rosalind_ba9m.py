def betterBWMatching(lastColumn, pattern, firstIndex):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if pattern != "":
            symbol = pattern[-1]
            # print symbol
            pattern = pattern[:-1]
            if symbol in lastColumn:
                topIndex = -1
                # bottomIndex = -1
                symbolCountTop = 0
                symbolCountBottom = 0
                # for i in range(0, top):
                #     if lastColumn[i] == symbol:
                #         symbolCountTop += 1
                        # if topIndex == -1:
                        #     topIndex = i
                        # bottomIndex = i

                for i in range(0, bottom + 1):
                    # print lastColumn[i]
                    if lastColumn[i] == symbol:
                        if (i < top):
                            symbolCountTop += 1
                        symbolCountBottom += 1
                        # if i >= top:
                        if topIndex == -1:
                            topIndex = i
                            # bottomIndex = i
                # print "topIndex", topIndex
                # symbolCountTop += symbolCountBottom
                # print symbolCountTop, symbolCountBottom
                if topIndex == -1:
                    return 0
                # print "firstIndex", firstIndex[symbol]
                top = firstIndex[symbol] + symbolCountTop
                bottom = firstIndex[symbol] + symbolCountBottom - 1
                # print "top, bottom", top, bottom
            else:
                 return 0
        else:
            return bottom - top + 1
    return bottom - top + 1



fileName = 'rosalind_ba9m.txt'
with open(fileName) as file:
    content = file.readlines()


# print lastToFirst('T$GACCA', 3)


lastColumn = content[0][:-1]
# print lastColumn
# firstIndices = [0, 0, 0, 0]
firstIndices = list()
firstIndices.append(0)
firstIndices.append(1)
fList = ''.join(sorted(lastColumn))
# print fList
for i in range(1, len(fList) - 1):
    if fList[i] != fList[i + 1]:
        firstIndices.append(i + 1)

firstIndex = {
    "$" : firstIndices[0],
    "A" : firstIndices[1],
    "C" : firstIndices[2],
    "G" : firstIndices[3],
    "T" : firstIndices[4]
}
patterns = content[1].split()
output = list()
for index in range(0, len(patterns)):
    # print patterns[index]
    # print betterBWMatching(lastColumn, patterns[index], firstIndex)
    output.append(betterBWMatching(lastColumn, patterns[index], firstIndex))

# print "".join(output)
print(" ".join(map(str,output)))
