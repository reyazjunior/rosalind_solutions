# Monoisotopic mass table for the standard 20 amino acids
monoisotopic_mass_table = {
    'A': 71.03711,  'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146,  'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333
}

def calculate_protein_mass(protein):
    """
    Calculate the monoisotopic mass of a protein string.
    """
    return sum(monoisotopic_mass_table[aa] for aa in protein)

try:

    # Read the protein string
    with open('bioinformatics_stronghold/rosalind_prtm.txt', 'r') as file:
        protein_string = file.read().strip()

    # Calculate the total mass
    total_mass = calculate_protein_mass(protein_string)

    # Write result to output file with 3 decimal places
    with open('bioinformatics_stronghold/rosalind_prtm_output.txt', 'w') as file:
        file.write(f"{total_mass:.3f}\n")

except Exception as e:
    print(f"An error occurred: {e}")
