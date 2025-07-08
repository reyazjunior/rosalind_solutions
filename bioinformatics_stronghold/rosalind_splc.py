from Bio.Seq import Seq

def spliced_translation(dna_seq, introns):
    # Remove introns
    for intron in introns:
        dna_seq = dna_seq.replace(intron, '')

    # Transcribe to RNA
    rna_seq = Seq(dna_seq).transcribe()

    # Translate to protein
    protein = rna_seq.translate(to_stop=True)

    return str(protein)


# I/O handling in try block
try:
    from Bio import SeqIO

    with open("bioinformatics_stronghold/rosalind_splc.txt", "r") as file:
        records = list(SeqIO.parse(file, "fasta"))
        dna_seq = str(records[0].seq)
        introns = [str(record.seq) for record in records[1:]]

    # Call the function with variables
    protein = spliced_translation(dna_seq, introns)

    # Write output to file
    with open("bioinformatics_stronghold/rosalind_splc_output.txt", "w") as out_file:
        out_file.write(protein)

except Exception as e:
    print("An error occurred:", e)
