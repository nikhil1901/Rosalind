# -*- coding: utf-8 -*-
rna_codon_table = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"
}
output = ""


fileName = 'rosalind_splc.txt'
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
rna_sequence = ""
rna_sequence = sequences[0][:]
del sequences[0]


rna_sequence = rna_sequence.replace("T", "U")
# print rna_sequence

for sequence in sequences:
    sequence = sequence.replace("T", "U")
    rna_sequence = rna_sequence.replace(sequence, "")

# print rna_sequence


# print rna_sequence
for index in range(0, len(rna_sequence), 3):
    rna = rna_sequence[index:index+3]
    rna_convert = rna_codon_table[rna]
    if(rna_convert == "Stop"):
        break
    output = output + rna_convert
    # print "rna_convert:", rna_convert

print output
