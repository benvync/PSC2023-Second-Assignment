from Bio import SeqIO
from Bio.Seq import Seq

def splice_introns(DNA, Introns):
    for Intron in Introns:
        DNA = DNA.replace(Intron, '')
    return DNA

def translate_dna(DNA):
    coding_DNA = Seq(DNA)
    protein = coding_DNA.translate()
    return protein

def main(): #FASTA file insertion
    with open('rosalind_splc.txt', 'r') as file:
        records = list(SeqIO.parse(file, 'fasta'))

    DNA = str(records[0].seq)
    introns = [str(record.seq) for record in records[1:]]
    exons_DNA = splice_introns(DNA, introns) #actual splicing process
    protein = translate_dna(exons_DNA)
    with open('output_SPLC.txt', 'w') as output_file:
        output_file.write(str(protein))

if __name__ == "__main__":
    main()

