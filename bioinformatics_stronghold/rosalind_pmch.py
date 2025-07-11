from math import factorial
from Bio import SeqIO

def count_perfect_matchings(rna_seq):
    a = rna_seq.count('A')
    u = rna_seq.count('U')
    c = rna_seq.count('C')
    g = rna_seq.count('G')
    if a != u or c != g:
        raise ValueError("RNA string doesn't have equal A-U or C-G counts")
    return factorial(a) * factorial(c)

# I/O Handling
try:
    with open("bioinformatics_stronghold/rosalind_pmch.txt", "r") as file:
        records = list(SeqIO.parse(file, "fasta"))
        rna_string = str(records[0].seq)

    result = count_perfect_matchings(rna_string)

    with open("bioinformatics_stronghold/rosalind_pmch_output.txt", "w") as out:
        out.write(str(result) + "\n")

except Exception as e:
    print("An error occurred:", e)
