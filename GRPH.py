
from Bio import SeqIO

def read_fasta(filename):
    Sequence = {}
    for record in SeqIO.parse(filename, "fasta"):
        Sequence[record.id] = str(record.seq)
    return Sequence

def find_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def create_overlap_graph(fasta_file, k):
    Sequence = read_fasta(fasta_file)
    adjacency_list = []

    for label1, seq1 in Sequence.items():
        for label2, seq2 in Sequence.items():
            if label1 != label2 and find_overlap(seq1, seq2, k):
                adjacency_list.append((label1, label2))

    return adjacency_list

def write_adjacency_list_to_file(adjacency_list, output_file):
    with open(output_file, 'w') as file:
        for edge in adjacency_list:
            file.write(f"{edge[0]} {edge[1]}\n")

fasta_file = "rosalind_grph.txt"
k = 3
output_file = "output_GRPH.txt"

adjacency_list = create_overlap_graph(fasta_file, k)
write_adjacency_list_to_file(adjacency_list, output_file) #write the list in the output






















