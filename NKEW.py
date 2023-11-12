import sys
from Bio import Phylo
import io

input_file = 'rosalind_nkew.txt'
output_file = 'output_NKEW.txt'

with open(input_file, 'r') as f:
    Pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]

with open(output_file, 'w') as output:
    for i, line in Pairs:
        X, Y = line.split()
        tree = Phylo.read(io.StringIO(i), 'newick')
        distance = round(tree.distance(X, Y))
        output.write(f'{distance} ')

print(output_file)
