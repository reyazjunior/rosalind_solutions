def partial_permutations(n, k, mod=10**6):
    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % mod
    return result

# File I/O in try block
try:
    with open("bioinformatics_stronghold/rosalind_pper.txt", "r") as file:
        n, k = map(int, file.read().strip().split())

    result = partial_permutations(n, k)

    with open("bioinformatics_stronghold/rosalind_pper_output.txt", "w") as out:
        out.write(str(result) + "\n")

except Exception as e:
    print("An error occurred:", e)
