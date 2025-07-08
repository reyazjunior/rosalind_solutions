def rna_to_protein(rna_sequence):
    codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",

    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", # AUG is also the start codon
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    """
    Translates an RNA sequence into a protein sequence using the global codon_table.

    The translation starts at the beginning of the RNA sequence and continues
    until a "Stop" codon is encountered or the end of the sequence is reached.
    If the RNA sequence length is not a multiple of 3, any remaining nucleotides
    at the end will be ignored.

    Args:
        rna_sequence (str): A string representing the RNA sequence.
                            Should contain only 'U', 'C', 'A', 'G'.

    Returns:
        str: The translated protein sequence (single-letter amino acid codes)
             or an error message if an invalid codon is found.
    """
    protein_sequence = []
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence) - len(rna_sequence) % 3, 3):
        codon = rna_sequence[i:i+3]

        if codon not in codon_table:
            return f"Error: Invalid codon '{codon}' found in sequence."

        amino_acid = codon_table[codon]

        if amino_acid == "Stop":
            break
        else:
            protein_sequence.append(amino_acid)

    return "".join(protein_sequence)

try:
    with open('bioinformatics_stronghold/rosalind_prot.txt','r') as file:
        lines = file.readlines()
        s_from_file = lines[0].strip()
        protein=rna_to_protein(s_from_file)
        with open('bioinformatics_stronghold/rosalind_prot_output.txt','w') as file:
            file.write(f"{protein}")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except IndexError:
    print("Error: File does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse data from the input file. Please check the format.")