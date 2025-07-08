def gc_content(s):
    gc_count=s.count('G')+s.count('C')
    return (gc_count/len(s)) *100

try:
    dna_dict = {}
    with open('bioinformatics_stronghold/rosalind_gc.txt', 'r') as file:
        current_label = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_label = line[1:]
                dna_dict[current_label] = ''
            elif current_label:
                dna_dict[current_label] += line
    print("DNA dictionary loaded successfully.")
    max_label=None
    max_gc=-1
    for label, sequence in dna_dict.items():
        gc=gc_content(sequence)
        if gc>max_gc:
            max_gc=gc
            max_label=label
    with open('bioinformatics_stronghold/rosalind_gc_output.txt', 'w') as out_file:
        out_file.write(f"{max_label}\n{max_gc:.6f}\n")
    print(f"Highest GC content result written to rosalind_gc_output.txt")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except Exception as e:
    print(f"Error while reading the file: {e}")
