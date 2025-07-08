def count_dna_nucleotides(s):
    a,c,g,t=0,0,0,0
    for i in s:
        if i=='A':
            a+=1
        elif i=='C':
            c+=1
        elif i=='G':
            g+=1
        elif i=='T':
            t+=1
    return a,c,g,t

try:
    with open('bioinformatics_stronghold/rosalind_dna.txt', 'r') as file:
        lines = file.readlines()
        s_from_file = lines[0].strip()
        a,c,g,t=count_dna_nucleotides(s_from_file)
        print(f"{a} {c} {g} {t}")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except IndexError:
    print("Error: File does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse data from the input file. Please check the format.")