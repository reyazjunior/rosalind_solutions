def build_overlap_graph(dna_dict, k=3):
    edges=[]
    for id1, seq1 in dna_dict.items():
        suffix=seq1[-k:]
        for id2, seq2 in dna_dict.items():
            if id1 != id2 and seq2.startswith(suffix):
                edges.append((id1, id2))
    return edges


dna_dict = {}
try:
    with open("bioinformatics_stronghold/rosalind_grph.txt", "r") as f:
        current_id = ""
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    dna_dict[current_id] = ''.join(current_seq)
                current_id = line[1:]  # remove '>'
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            dna_dict[current_id] = ''.join(current_seq)

        edges = build_overlap_graph(dna_dict)
    with open("bioinformatics_stronghold/rosalind_grph_output.txt", "w") as out:
        for edge in edges:
            out.write(f"{edge[0]} {edge[1]}\n")
except Exception as e:
    print(f"Error reading file: {e}")
