from math import comb

def prob_at_least_N_AaBb(k, N):
    n = 2 ** k  # total individuals in generation k
    p = 0.25    # probability of Aa Bb
    prob = 0
    for i in range(N, n+1):
        prob += comb(n, i) * (p**i) * ((1 - p)**(n - i))
    return round(prob, 3)


try:
    with open('bioinformatics_stronghold/rosalind_lia.txt', 'r') as file:
        line = file.readline().strip()
        k_str, N_str = line.split()
        k_from_file = int(k_str)
        N_from_file = int(N_str)
        file_result = prob_at_least_N_AaBb(k_from_file, N_from_file)
        print(f"Result from file: {file_result}")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except ValueError:
    print("Error: Invalid data in the file. Please ensure it contains two integers separated by a space.")