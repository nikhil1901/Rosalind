# -*- coding: utf-8 -*-

def editDistance(string1, string2):
    m = len(string1) + 1
    n = len(string2) + 1
    gap = 3
    a = [[0 for x in range(n)] for y in range(m)]
    b = [[0 for x in range(n)] for y in range(m)]
    for index in range(1, m):
        a[index][0] = index * gap
    for index in range(1, n):
        a[0][index] = index * gap


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
            # if a[i][j] == (cost + a[i - 1][j - 1]):
            #     newString1.join(string1[i])
            #     newString2.join(string2[j])
            # elif a[i][j] == (gap + a[i - 1][j]):
            #     newString1.join(string1[i])
            #     newString2.join("-")
            # else:
            #     newString1.join("-")
            #     newString2.join(string2[j])

    return a


fileName = 'rosalind_edta.txt'
with open(fileName) as file:
    content = file.readlines()

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

# print sequences

# inverted = False
# if len(sequences[0]) >= len(sequences[1]):
#     string1 = sequences[0]
#     string2 = sequences[1]
# else:
#     string1 = sequences[1]
#     string2 = sequences[0]
#     inverted = True

string1 = sequences[0]
string2 = sequences[1]

editDistanceMatrix = editDistance(string1, string2)


m = len(string1)
n = len(string2)
index1 = m
index2 = n
outputString1 = ""
outputString2 = ""
editDistanceCount = 0

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
    # elif minimum == editDistanceMatrix[index1 - 1][index2 - 1]:
    #     attachString = string2[index2 - 1][:]
    #     outputString2 += attachString
    #     attachString = string1[index1 - 1][:]
    #     outputString1 += attachString
    #     index1 -= 1
    #     index2 -= 1
    #     if string1[index1] != string2[index2]:
    #         editDistanceCount += 1
    else:
        attachString = string1[index1 - 1][:]
        outputString2 += "-"
        outputString1 += attachString
        index1 -= 1
        editDistanceCount += 1


print editDistanceCount
# if inverted:
#     print outputString2[::-1]
#     print outputString1[::-1]
# else:
#     print outputString1[::-1]
#     print outputString2[::-1]
print outputString1[::-1]
print outputString2[::-1]
