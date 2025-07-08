def expected_dominant_offspring(couples):
    # Probabilities of dominant phenotype for each couple type
    probs = [1, 1, 1, 0.75, 0.5, 0]
    expected = 0
    for count, prob in zip(couples, probs):
        expected += count * 2 * prob  # 2 offspring per couple
    return expected



data = []
try:
    with open("bioinformatics_stronghold/rosalind_iev.txt", "r") as f:
        line = f.readline().strip()
        data = list(map(int, line.split()))
        result = expected_dominant_offspring(data)
        print(result)
except Exception as e:
    print(f"Error reading file: {e}")
