def mortal_fib(n, m):
    age = [0] * m
    age[0] = 1

    for month in range(1, n):
        new_borns = sum(age[1:])
        age = [new_borns] + age[:-1]

    return sum(age)

try:
    with open('bioinformatics_stronghold/rosalind_fibd.txt', 'r') as file:
        line = file.readline().strip()
        n, m = map(int, line.split())
        result = mortal_fib(n, m)
        print(f"Result from file: {result}")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except ValueError:
    print("Error: Invalid data in the file. Please ensure it contains two integers separated by a space.")
