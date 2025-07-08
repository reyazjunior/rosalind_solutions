def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

try:
    with open('bioinformatics_stronghold/rosalind_hamm.txt', 'r') as file:
        lines = file.read().strip().splitlines()
        if len(lines) < 2:
            raise ValueError("File must contain exactly two lines with DNA strings.")
        s1, s2 = lines[0].strip(), lines[1].strip()
        result = hamming_distance(s1, s2)
        print(f"Hamming distance: {result}")

except FileNotFoundError:
    print("Error: File 'rosalind_hamming.txt' not found.")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")