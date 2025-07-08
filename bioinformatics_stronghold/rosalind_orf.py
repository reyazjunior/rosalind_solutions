# Codon to amino acid mapping
CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# Reverse complement
def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement[base] for base in reversed(seq))

# Translate DNA sequence into amino acids
def translate(seq):
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in CODON_TABLE:
            protein += CODON_TABLE[codon]
        else:
            protein += 'X'  # unknown codon
    return protein

# Extract all valid protein strings from ORFs
def find_candidate_proteins(dna_seq):
    proteins = set()

    for strand in [dna_seq, reverse_complement(dna_seq)]:
        for frame in range(3):
            subseq = strand[frame:]
            trimmed = subseq[:len(subseq) - len(subseq) % 3]
            amino_seq = translate(trimmed)

            # Extract ORFs starting with 'M' and ending at '*'
            for i in range(len(amino_seq)):
                if amino_seq[i] == 'M':
                    protein = ''
                    for j in range(i, len(amino_seq)):
                        if amino_seq[j] == '*':
                            proteins.add(protein)
                            break
                        protein += amino_seq[j]

    return proteins

try:
    with open("bioinformatics_stronghold/rosalind_orf.txt", "r") as f:
        lines = f.readlines()
        dna_seq = ''.join(line.strip() for line in lines if not line.startswith('>'))

    result = find_candidate_proteins(dna_seq)

    with open("bioinformatics_stronghold/rosalind_orf_output.txt", "w") as out:
        for protein in result:
            out.write(protein + "\n")

except Exception as e:
    print("Error:", e)
