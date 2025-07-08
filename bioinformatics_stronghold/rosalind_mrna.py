def count_rna_translations(protein):
    codon_counts = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,
        'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
        'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
        'E': 2, 'G': 4, '*': 3  # * is the stop codon
    }

    MOD = 1_000_000
    total = 1

    for aa in protein:
        total = (total * codon_counts[aa]) % MOD

    # Multiply by the number of stop codons
    total = (total * codon_counts['*']) % MOD

    return total


try:
    with open("bioinformatics_stronghold/rosalind_mrna.txt") as f:
        protein_string = f.read().strip()
    print(count_rna_translations(protein_string))
except FileNotFoundError:
    print("Input file not found.")
