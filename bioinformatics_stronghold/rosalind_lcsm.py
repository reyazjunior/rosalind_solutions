def find_lcsm(sequences):
    if not sequences:
        return ""
    shortest=min(sequences,key=len)
    max_len = len(shortest)
    for length in range(max_len,0,-1):
        for start in range(max_len-length+1):
            motif=shortest[start:start+length]
            if all(motif in seq for seq in sequences):
                return motif
    return ""

try:
    sequences=[]
    with open('bioinformatics_stronghold/rosalind_lcsm.txt', 'r') as file:
        current_sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ''
            else:
                current_sequence += line
        if current_sequence:
            sequences.append(current_sequence)
    print("Sequences loaded successfully.")
    result=find_lcsm(sequences)
    print(f"Longest common shared motif = {result}\n")
except FileNotFoundError:
    print("Error: File not found. Please create the file.")
except Exception as e:
    print(f"Error while reading the file: {e}")