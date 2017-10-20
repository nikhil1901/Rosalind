# -*- coding: utf-8 -*-
fileName = 'rosalind_grph.txt'
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
            # print temp
            # print prevSequence
            # print len(sequences) - 1
            # print ""
            prevSequence = prevSequence + temp
            # print prevSequence
            # print prevSequence
            # print len(sequences) - 1
            # print ""
            sequences[len(sequences) - 1] = prevSequence
        else:
            temp = line[:]
            temp = temp.translate(None, '\n')
            sequences.append(temp)
            sequenceCount += 1
            nameFlag = False

# print len(stringNames)
# print sequences[0]
# print len(stringSet)
count = 0

for index1, sequence1 in enumerate(sequences):
    for index2 in range(index1+1, len(sequences)):
    # for index2, sequence2 in enumerate(sequences):
    #     if(index1 != index2):
            # print stringNames[1], stringNames[2]
        count += 1
        if(sequence1[-3:] == sequences[index2][:3]):
            # print "sequence: "
            # print stringNames[index1], sequence1[-3:], sequence1
            # print stringNames[index2], sequence2[:3], sequence2
            # graphElement = ''.join([str(stringNames[index1]), "\t", str(stringNames[index2])])
            graphElements.append(str(stringNames[index1]))
            graphElements.append(str(stringNames[index2]))
        if (sequences[index2][-3:] == sequence1[:3]):
            # print "sequence: "
            # print stringNames[index1], sequence1[-3:], sequence1
            # print stringNames[index2], sequence2[:3], sequence2
            # graphElement = ''.join([str(stringNames[index2]), "\t", str(stringNames[index1])])
            graphElements.append(str(stringNames[index2]))
            graphElements.append(str(stringNames[index1]))

# print len(graphElement)
for index in xrange(0, len(graphElements), 2):
    print graphElements[index], graphElements[index+1]
