def fib(n,k):
    a=1
    b=1
    for i in range(n-2):
        c=b+ k*a
        a=b
        b=c
    return b

try:
    with open('bioinformatics_stronghold/rosalind_fib.txt', 'r') as file:
        line = file.readline().strip()
        n_str, k_str = line.split()
        n_from_file = int(n_str)
        k_from_file = int(k_str)
        file_result = fib(n_from_file, k_from_file)
        print(f"Result from file: {file_result}")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except ValueError:
    print("Error: Invalid data in the file. Please ensure it contains two integers separated by a space.")