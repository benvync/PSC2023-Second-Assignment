def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def find_corrections(reads):
    Correction = []
    seen = set()
    for read in reads:
        reverse_complement = read[::-1].translate(str.maketrans("ACGT", "TGCA"))
        if read in seen:
            Correction.append(f"{read}->{reverse_complement}")
        else:
            for seen_read in seen:
                if hamming_distance(read, seen_read) == 1:
                    Correction.append(f"{read}->{seen_read}")
                    break
                elif hamming_distance(reverse_complement, seen_read) == 1:
                    Correction.append(f"{reverse_complement}->{seen_read}")
                    break
        seen.add(read)
    return Correction

def main():
    with open('rosalind_corr.txt', 'r') as file:
        records = list(file.read().strip().split('>'))
        reads = [record.split('\n', 1)[1].replace('\n', '') for record in records if record]

    Correction = find_corrections(reads)
    with open('output_corr.txt', 'w') as output_file:
        for correction in Correction:
            output_file.write(correction + '\n')

if __name__ == "__main__":
    main()
