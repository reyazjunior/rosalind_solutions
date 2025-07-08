import requests
import re

def fetch_fasta_sequence(uniprot_id):
    """Fetches and returns the protein sequence from UniProt FASTA."""
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    response.raise_for_status()

    lines = response.text.splitlines()
    return ''.join(lines[1:])  # Remove header and join sequence lines


def find_ngly_motifs(sequence):
    """
    Returns 1-based positions of all N-glycosylation motifs (including overlaps).
    Motif: N{P}[ST]{P}
    """
    positions = []
    for i in range(len(sequence) - 3):
        if (
            sequence[i] == 'N' and
            sequence[i + 1] != 'P' and
            sequence[i + 2] in {'S', 'T'} and
            sequence[i + 3] != 'P'
        ):
            positions.append(i + 1)  # 1-based indexing
    return positions



# MAIN
try:
    with open("bioinformatics_stronghold/rosalind_mprt.txt") as f:
        ids = [line.strip() for line in f if line.strip()]

    with open("bioinformatics_stronghold/rosalind_mprt_output.txt", "w") as out:
        for full_id in ids:
            base_id = full_id.split('_')[0]  # Keep only part before "_"
            try:
                sequence = fetch_fasta_sequence(base_id)
                positions = find_ngly_motifs(sequence)
                if positions:
                    out.write(f"{full_id}\n")
                    out.write('\t'.join(map(str, positions)) + '\n')
            except requests.HTTPError:
                out.write(f"Failed to fetch: {full_id}\n")

except FileNotFoundError:
    print("Input file not found.")
