# -*- coding: utf-8 -*-
import math
fileName = 'rosalind_prob.txt'
with open(fileName) as file:
    content = file.readlines()

stringNames = list()    #contain names of strings
sequences = list()   #contain the actual string sequences
probabilityElements = list()
lineCount = 0
dna = ""

for line in content:
    if(lineCount == 0):
        temp = line[:]
        temp = temp.translate(None, '\n')
        dna = "".join(temp)
        lineCount += 1
    else:
        temp = line[:]
        temp = temp.translate(None, '\n')
        probabilityElements = map(float, temp.split())

a_t_count = dna.count('A') + dna.count('T')
g_c_count = dna.count('G') + dna.count('C')

output = list()

for probabilityElement in probabilityElements:
    outputProbability = a_t_count*math.log((1-probabilityElement)/2, 10) + g_c_count*math.log(probabilityElement/2, 10)
    outputProbabilityString = str("%.3f" % outputProbability)
    output.append(outputProbabilityString)

print ' '.join(output)
