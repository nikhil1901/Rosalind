# -*- coding: utf-8 -*-
fileName = 'rosalind_fibd.txt'
file = open(fileName, 'r')
content = file.read()

months, lifespan = map(int, content.split())

mature = [0] * (lifespan - 1)

immature = 1


for month in range(0, months - 1):
    to_immature = 0
    for index in range(lifespan - 2, -1, -1):
        to_immature += mature[index]
        mature[index] = 0
        if(index != 0):
            mature[index] = mature[index - 1]
    mature[0] = immature
    immature = to_immature
    # print "month = ", month
    # print mature
    # print immature

sum = sum(mature) + immature


print sum
