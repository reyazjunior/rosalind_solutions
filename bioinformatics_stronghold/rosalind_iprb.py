def prob(k,m,n):
    total=k+m+n
    return (
        (k / total) * ((k - 1) / (total - 1)) +
        2 * (k / total) * (m / (total - 1)) +
        2 * (k / total) * (n / (total - 1)) +
        (m / total) * ((m - 1) / (total - 1)) * 0.75 +
        2 * (m / total) * (n / (total - 1)) * 0.5
    )

try:
    with open('bioinformatics_stronghold/rosalind_iprb.txt', 'r') as file:
        line = file.readline().strip()
        k_str, m_str, n_str = line.split()
        k = int(k_str)
        m = int(m_str)
        n = int(n_str)
        file_result = prob(k,m,n)
        print(f"Result from file: {file_result}")
except FileNotFoundError:
    print("Error: 'rosalind_iprb.txt' not found. Please create the file with the leg lengths.")
except ValueError:
    print("Error: Invalid data in 'rosalind_iprb'. Please ensure it contains two integers separated by a space.")