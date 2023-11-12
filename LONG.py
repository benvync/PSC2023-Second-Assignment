def merge_strings(s1, s2):
    maximum_overlap = 0
    merged_strings = ""
    for i in range(1, len(s1)):
        if s2.startswith(s1[i:]):
            if len(s1[i:]) > maximum_overlap:
                maximum_overlap = len(s1[i:])
                merged_strings = s1 + s2[maximum_overlap:]
    if maximum_overlap == 0:
        merged_strings = s1 + s2
    return merged_strings

def find_shortest_superstring(strings):
    while len(strings) > 1:
        maximum_overlap = 0
        merge_candidates = None
        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    merged = merge_strings(strings[i], strings[j])
                    overlap = len(strings[i]) + len(strings[j]) - len(merged)
                    if overlap > maximum_overlap:
                        maximum_overlap = overlap
                        merge_candidates = (i, j)
        if merge_candidates:
            i, j = merge_candidates
            merged_string = merge_strings(strings[i], strings[j])
            strings.pop(max(i, j))
            strings.pop(min(i, j))
            strings.append(merged_string)
    return strings[0]

def main():
    with open('rosalind_long.txt', 'r') as file:
        records = list(file.read().strip().split('>'))
        DNA_string = [record.split('\n', 1)[1].replace('\n', '') for record in records if record]

    shortest_string = find_shortest_superstring(DNA_string)
    with open('output_LONG.txt', 'w') as output_file:
        output_file.write(shortest_string)

if __name__ == "__main__":
    main()
