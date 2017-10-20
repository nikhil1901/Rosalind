# -*- coding: utf-8 -*-
file = open('rosalind_dna.txt', 'r')
dna_sequence = file.read()
a_count = dna_sequence.count('A')
c_count = dna_sequence.count('C')
g_count = dna_sequence.count('G')
t_count = dna_sequence.count('T')
print a_count, '\t', c_count, '\t', g_count, '\t', t_count
