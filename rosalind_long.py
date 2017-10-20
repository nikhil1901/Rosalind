# -*- coding: utf-8 -*-
import difflib
fileName = 'rosalind_long.txt'
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

count = 0

maxSubsequence = sequences[0]
del sequences[0]

while(len(sequences) > 0):
    for index1, sequence1 in enumerate(sequences):
        minLength = min(len(sequence1), len(maxSubsequence))
        # if(index1 != index2):
        for index in range(minLength, minLength/2, -1):
            if sequence1[0:index+1] == maxSubsequence[-(index+1):]:
                # if(len(maxSubsequence) < (len(sequence1) + len(maxSubsequence) - index)):
                maxSubsequence = str(maxSubsequence) + str(sequence1[index+1:])
                del sequences[index1]
                break
            if maxSubsequence[0:index+1] == sequence1[-(index+1):]:
                # if(len(maxSubsequence) < (len(maxSubsequence) + len(sequence1) - index)):
                maxSubsequence = str(sequence1) + str(maxSubsequence[index+1:])
                del sequences[index1]
                break

print maxSubsequence
