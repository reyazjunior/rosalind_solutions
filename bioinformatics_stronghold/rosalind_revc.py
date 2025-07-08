def complement(dna):
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    complemented_list = []
    for nucleotide in dna:
        complemented_list.append(complement_map[nucleotide])
    complemented_string = "".join(complemented_list)
    reverse_complemented_string = complemented_string[::-1]
    return reverse_complemented_string

try:
    with open('bioinformatics_stronghold/rosalind_revc.txt', 'r') as file:
        lines = file.readlines()
        s_from_file = lines[0].strip()
        rna=complement(s_from_file)
        with open('bioinformatics_stronghold/rosalind_revc_output.txt','w') as file:
            file.write(f"{rna}")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except IndexError:
    print("Error: File does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse data from the input file. Please check the format.")