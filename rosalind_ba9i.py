def rotations(sequence):
    superSequence = sequence * 2
    allRotations = []
    for index in range(0, len(sequence)):
        allRotations.append(superSequence[index:index+len(sequence)])
    return allRotations




fileName = 'rosalind_ba9i.txt'
with open(fileName) as file:
    content = file.readlines()

sequence = ""
for line in content:
    temp = line[:]
    temp = temp.translate(None, '\n')
    sequence = sequence + temp

allRotations = sorted(rotations(sequence))
lastSequences = ''.join(map(lambda x:x[-1], allRotations))
print lastSequences
# print sequence
