def dna_to_rna(dna):
    rna=dna.replace('T','U')
    return rna

try:
    with open('bioinformatics_stronghold/rosalind_rna.txt', 'r') as file:
        lines = file.readlines()
        s_from_file = lines[0].strip()
        rna=dna_to_rna(s_from_file)
        with open('bioinformatics_stronghold/rosalind_rna_output.txt','w') as file:
            file.write(f"{rna}")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except IndexError:
    print("Error: File does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse data from the input file. Please check the format.")