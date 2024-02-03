def reverse_complement(dna_strand):
    atcg = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(atcg[base] for base in reversed(dna_strand))

def find_reverse_complements(dna_list):
    indices_with_reverse_complements = set()

    for i, (_, dna_strand) in enumerate(dna_list, start=1):
        complement = reverse_complement(dna_strand)

        found_complement = any(complement == other_strand for j, (_, other_strand) in enumerate(dna_list, start=1) if i != j)

        if found_complement or complement == dna_strand:
            indices_with_reverse_complements.add(i)

    return indices_with_reverse_complements

def main():
    def get_dna_strand():
        length, strand = input().split()
        return int(length), strand.upper()

    n = int(input())
    dna_list = [get_dna_strand() for _ in range(n)]

    result_indices = find_reverse_complements(dna_list)

    if result_indices:
        print(' '.join(map(str, sorted(result_indices))))
    else:
        print('RACOON ROLL')

if __name__ == '__main__':
    main()
