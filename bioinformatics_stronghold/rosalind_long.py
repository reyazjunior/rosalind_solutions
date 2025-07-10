from Bio import SeqIO

def _get_overlap_strings(s1, s2):
    """
    Return a pair (merged_string, overlap_substring) for maximal suffix–prefix overlap
    between s1 and s2. Checks both directions.
    """
    candidates = []
    overlaps = []

    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1) - i]:
            overlaps.append(s1[i:])
            candidates.append(s1 + s2[len(s1) - i:])
            break

    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2) - i]:
            overlaps.append(s2[i:])
            candidates.append(s2 + s1[len(s2) - i:])
            break

    if not overlaps:
        return "", ""

    # Choose the merge that results in the shortest total string
    merged = min(candidates, key=len)
    # Choose the overlap with the greatest length
    overlap = max(overlaps, key=len)
    return merged, overlap


def find_superstring(reads):
    """
    Greedily merge reads by picking the pair with the longest overlap
    until only one string remains.
    """
    seqs = reads[:]
    while len(seqs) > 1:
        best_merge = None
        best_overlap = ""
        pair_to_merge = (None, None)

        for i in range(len(seqs) - 1):
            for j in range(i + 1, len(seqs)):
                merged, overlap = _get_overlap_strings(seqs[i], seqs[j])
                if len(overlap) > len(best_overlap):
                    best_overlap = overlap
                    best_merge = merged
                    pair_to_merge = (i, j)

        if best_merge is None:
            raise ValueError("No valid overlap found — check input data")

        i, j = pair_to_merge
        a, b = seqs[i], seqs[j]
        new_seqs = [seq for idx, seq in enumerate(seqs) if idx not in {i, j}]
        new_seqs.append(best_merge)
        seqs = new_seqs

    return seqs[0]



try:
    with open("bioinformatics_stronghold/rosalind_long.txt", "r") as infile:
        reads = [str(rec.seq) for rec in SeqIO.parse(infile, "fasta")]

    result = find_superstring(reads)

    with open("bioinformatics_stronghold/rosalind_long_output.txt", "w") as outfile:
        outfile.write(result + "\n")

except Exception as error:
    print("An error occurred:", error)
