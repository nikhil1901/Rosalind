# -*- coding: utf-8 -*-


def editDistance(string1, string2):
    m = len(string1) + 1
    n = len(string2) + 1
    gap = 3
    a = [[0 for x in range(n)] for y in range(m)]
    b = [[0 for x in range(n)] for y in range(m)]
    for index in range(1, m):
        a[index][0] = index * gap
        b[index][0] = gap
    for index in range(1, n):
        a[0][index] = index * gap
        b[0][index] = gap

    b[0][0] = gap


    for i in range(1, m):
        for j in range(1, n):
            if(string1[i - 1] == string2[j - 1]):
                cost = 0
            else:
                cost = 3
            a[i][j] = min(
                cost + a[i - 1][j - 1],
                gap + a[i - 1][j],
                gap + a[i][j - 1]
            )

            if a[i][j] == (cost + a[i - 1][j - 1]):
                b[i][j] += b[i - 1][j - 1]
            if a[i][j] == (gap + a[i - 1][j]):
                b[i][j] += b[i - 1][j]
            if a[i][j] == (gap + a[i][j - 1]):
                b[i][j] += b[i][j - 1]

            b[i][j] %= 134217727

    return a, b


fileName = 'rosalind_ctea.txt'
with open(fileName) as file:
    content = file.readlines()

gap = 3
stringNames = list()    #contain names of strings
sequences = list()   #contain the actual string sequences
graphElements = list()
nameFlag = False
stringSet = set()
sequenceCount = 0
for line in content:
    if(line.startswith('>')):
        temp = line[:]
        temp = temp.translate(None, '>')
        temp = temp.translate(None, '\n')
        stringNames.append(temp)
        stringSet.add(temp)
        nameFlag = True
    else:
        if(not nameFlag):
            temp = line[:]
            temp = temp.translate(None, '\n')
            prevSequence = str(sequences[len(sequences) - 1][:])
            prevSequence = prevSequence + temp
            sequences[len(sequences) - 1] = prevSequence
        else:
            temp = line[:]
            temp = temp.translate(None, '\n')
            sequences.append(temp)
            sequenceCount += 1
            nameFlag = False

string1 = sequences[0]
string2 = sequences[1]

editDistanceMatrix, countMatrix = editDistance(string1, string2)

# print "\n".join(map(str, reversed(editDistanceMatrix)))
print (countMatrix[-1][-1] / gap)

m = len(string1)
n = len(string2)
index1 = m
index2 = n
outputString1 = ""
outputString2 = ""
editDistanceCount = 0
gapCount = 0

while index1 != 0 or index2 != 0:
    minimum = min(
        editDistanceMatrix[index1 - 1][index2 - 1],
        editDistanceMatrix[index1][index2 - 1],
        editDistanceMatrix[index1 - 1][index2]
    )

    if minimum == editDistanceMatrix[index1 - 1][index2 - 1]:
        attachString = string2[index2 - 1][:]
        outputString2 += attachString
        attachString = string1[index1 - 1][:]
        outputString1 += attachString
        index1 -= 1
        index2 -= 1
        if string1[index1] != string2[index2]:
            editDistanceCount += 1
    elif minimum == editDistanceMatrix[index1][index2 - 1]:
        attachString = string2[index2 - 1][:]
        outputString2 += attachString
        outputString1 += "-"
        index2 -= 1
        editDistanceCount += 1
    else:
        attachString = string1[index1 - 1][:]
        outputString2 += "-"
        outputString1 += attachString
        index1 -= 1
        editDistanceCount += 1
