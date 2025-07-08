def create_profile_matrix(sequences):
    n=len(sequences[0])
    profile_matrix={
        'A': [0]*n,
        'C': [0]*n,
        'G': [0]*n,
        'T': [0]*n
    }
    for dna in sequences:
        for position, nucleotide in enumerate(dna):
            profile_matrix[nucleotide][position]+=1
    return profile_matrix

def make_consensus_sequence(profile_matrix):
    result=[]
    for position in range(len(profile_matrix['A'])):
        max_count=0
        max_nucleotide=None
        for nucleotide in ['A','C','G','T']:
            count=profile_matrix[nucleotide][position]
            if count>max_count:
                max_count=count
                max_nucleotide=nucleotide
        result.append(max_nucleotide)
    consensus=''.join(result)
    return consensus

try:
    sequences=[]
    with open('bioinformatics_stronghold/rosalind_cons.txt', 'r') as file:
        current_sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ''
            else:
                current_sequence += line
        if current_sequence:
            sequences.append(current_sequence)
    print("Sequences loaded successfully.")
    profile_matrix= create_profile_matrix(sequences)
    consensus= make_consensus_sequence(profile_matrix)
    with open('bioinformatics_stronghold/rosalind_cons_output.txt', 'w') as out_file:
        out_file.write(f"{consensus}\n")
        for nucleotide in ['A', 'C', 'G', 'T']:
            out_file.write(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}\n")
    print(f"Output written successfully.")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except Exception as e:
    print(f"Error while reading the file: {e}")