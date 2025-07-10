def longest_subsequence(seq, increasing=True):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if (increasing and seq[j] < seq[i]) or (not increasing and seq[j] > seq[i]):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_idx = max(range(n), key=lambda i: dp[i])

    
    result = []
    while max_idx != -1:
        result.append(seq[max_idx])
        max_idx = prev[max_idx]

    return result[::-1]  # reverse to correct order


try:
    with open("bioinformatics_stronghold/rosalind_lgis.txt", "r") as f:
        lines = f.read().strip().splitlines()
        n = int(lines[0])
        seq = list(map(int, lines[1].split()))

    lis = longest_subsequence(seq, increasing=True)
    lds = longest_subsequence(seq, increasing=False)

    with open("bioinformatics_stronghold/rosalind_lgis_output.txt", "w") as out:
        out.write(" ".join(map(str, lis)) + "\n")
        out.write(" ".join(map(str, lds)) + "\n")

except Exception as e:
    print("An error occurred:", e)
