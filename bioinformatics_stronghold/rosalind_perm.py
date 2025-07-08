from itertools import permutations
import os

def generate_permutations(n):
    """
    Generate all permutations of numbers 1 through n.
    Returns a list of lists, each inner list being a permutation.
    """
    nums = list(range(1, n + 1))
    return list(permutations(nums))

try:
    # Read input
    with open('bioinformatics_stronghold/rosalind_perm.txt', 'r') as file:
        n = int(file.read().strip())

    # Generate permutations
    perms = generate_permutations(n)

    # Prepare output lines
    output_lines = [str(len(perms))]
    output_lines += [' '.join(map(str, perm)) for perm in perms]

    # Write output
    with open('bioinformatics_stronghold/rosalind_perm_output.txt', 'w') as file:
        file.write('\n'.join(output_lines))

except Exception as e:
    print(f"An error occurred: {e}")
