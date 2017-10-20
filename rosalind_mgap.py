# -*- coding: utf-8 -*-


def editDistance(string1, string2):
    m = len(string1) + 1
    n = len(string2) + 1
    gap = 1
    a = [[0 for x in range(n)] for y in range(m)]
    b = [[0 for x in range(n)] for y in range(m)]
    for index in range(1, m):
        a[index][0] = -index * gap
        b[index][0] = index
    for index in range(1, n):
        a[0][index] = -index * gap
        b[0][index] = index

    # b[0][0] = gap


    for i in range(1, m):
        for j in range(1, n):
            if(string1[i - 1] == string2[j - 1]):
                cost = gap
            else:
                cost = (-150000 * gap)
            a[i][j] = max(
                cost + a[i - 1][j - 1],
                a[i - 1][j] - gap,
                a[i][j - 1] - gap
            )

            if a[i][j] == (cost + a[i - 1][j - 1]):
                b[i][j] = b[i - 1][j - 1]
            elif a[i][j] == (a[i - 1][j] - gap):
                b[i][j] = b[i - 1][j] + 1
            elif a[i][j] == (a[i][j - 1] - gap):
                b[i][j] = b[i][j - 1] + 1

    return a, b


fileName = 'rosalind_mgap.txt'
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

print (countMatrix[-1][-1])
