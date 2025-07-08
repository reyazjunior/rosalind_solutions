def find_reverse_palindromes(dna):
    def reverse_complement(s):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement[base] for base in reversed(s))
    
    result = []
    n = len(dna)
    for i in range(n):
        for length in range(4, 13):  # inclusive of 12
            if i + length > n:
                continue
            sub = dna[i:i+length]
            if sub == reverse_complement(sub):
                result.append((i+1, length))  # positions are 1-based
    return result

# I/O Handling
try:
    with open("bioinformatics_stronghold/rosalind_revp.txt", "r") as file:
        lines = file.readlines()
        dna = ''.join(line.strip() for line in lines if not line.startswith('>'))

    palindromes = find_reverse_palindromes(dna)

    with open("bioinformatics_stronghold/rosalind_revp_output.txt", "w") as out:
        for pos, length in palindromes:
            out.write(f"{pos} {length}\n")

except Exception as e:
    print("An error occurred:", e)