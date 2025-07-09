from itertools import product

def generate_lexicographic_strings(alphabet, n):
    # Sort alphabet in standard English lex order
    sorted_alphabet = sorted(alphabet)
    
    # Generate all combinations using Cartesian product
    all_combinations = product(sorted_alphabet, repeat=n)
    
    # Join tuples into strings
    return [''.join(p) for p in all_combinations]

# File handling
try:
    with open("bioinformatics_stronghold/rosalind_lexf.txt", "r") as file:
        lines = file.read().strip().splitlines()
        alphabet = lines[0].split()
        n = int(lines[1].strip())

    results = generate_lexicographic_strings(alphabet, n)

    with open("bioinformatics_stronghold/rosalind_lexf_output.txt", "w") as out:
        for string in results:
            out.write(string + '\n')

except Exception as e:
    print("An error occurred:", e)
