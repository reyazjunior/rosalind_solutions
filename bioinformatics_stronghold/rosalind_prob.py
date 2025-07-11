import math

def log_probability_array(dna, gc_contents):
    at_count = sum(1 for base in dna if base in 'AT')
    gc_count = len(dna) - at_count

    results = []
    for gc in gc_contents:
        p_gc = gc / 2
        p_at = (1 - gc) / 2
        log_prob = gc_count * math.log10(p_gc) + at_count * math.log10(p_at)
        results.append(round(log_prob, 3))
    return results

# File I/O in try-block
try:
    with open("bioinformatics_stronghold/rosalind_prob.txt", "r") as file:
        lines = file.read().strip().splitlines()
        dna = lines[0].strip()
        gc_array = list(map(float, lines[1].strip().split()))

    output = log_probability_array(dna, gc_array)

    with open("bioinformatics_stronghold/rosalind_prob_output.txt", "w") as out:
        out.write(' '.join(map(str, output)) + '\n')

except Exception as e:
    print("An error occurred:", e)
