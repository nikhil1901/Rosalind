# -*- coding: utf-8 -*-
"""
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset

>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT


Sample Output

MVYIADKQHVASREAYGHMFKVCA
"""

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

# open input file
fileName = 'rosalind_splc.txt'
with open(fileName) as file:
    content = file.readlines()

stringNames = list()    #contain names of strings
sequences = list()   #contain the actual string sequences
graphElements = list()
nameFlag = False
stringSet = set()
sequenceCount = 0

# take input lines from the file given in FASTA format
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

rna_sequence = ""
rna_sequence = sequences[0][:]
del sequences[0]

# replace T with U, since in RNA, Thymine gets replaced by Uracil
rna_sequence = rna_sequence.replace("T", "U")

for sequence in sequences:
    sequence = sequence.replace("T", "U")
    rna_sequence = rna_sequence.replace(sequence, "")

# convert until we get Stop sequence
for index in range(0, len(rna_sequence), 3):
    rna = rna_sequence[index:index+3]
    rna_convert = rna_codon_table[rna]
    if(rna_convert == "Stop"):
        break
    output = output + rna_convert

# print the output
print output
