from pathlib import Path

def read_fasta(file_path):
    """Read a FASTA file and return a dictionary of sequences."""

    sequences = {}
    name = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line

    return sequences

genetic_code = {
    # Phenylalanine
    "TTT": "F", "TTC": "F",

    # Leucine
    "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L",
    "CTA": "L", "CTG": "L",

    # Isoleucine
    "ATT": "I", "ATC": "I", "ATA": "I",

    # Methionine (Start)
    "ATG": "M",

    # Valine
    "GTT": "V", "GTC": "V",
    "GTA": "V", "GTG": "V",

    # Serine
    "TCT": "S", "TCC": "S",
    "TCA": "S", "TCG": "S",
    "AGT": "S", "AGC": "S",

    # Proline
    "CCT": "P", "CCC": "P",
    "CCA": "P", "CCG": "P",

    # Threonine
    "ACT": "T", "ACC": "T",
    "ACA": "T", "ACG": "T",

    # Alanine
    "GCT": "A", "GCC": "A",
    "GCA": "A", "GCG": "A",

    # Tyrosine
    "TAT": "Y", "TAC": "Y",

    # Histidine
    "CAT": "H", "CAC": "H",

    # Glutamine
    "CAA": "Q", "CAG": "Q",

    # Asparagine
    "AAT": "N", "AAC": "N",

    # Lysine
    "AAA": "K", "AAG": "K",

    # Aspartic Acid
    "GAT": "D", "GAC": "D",

    # Glutamic Acid
    "GAA": "E", "GAG": "E",

    # Cysteine
    "TGT": "C", "TGC": "C",

    # Tryptophan
    "TGG": "W",

    # Arginine
    "CGT": "R", "CGC": "R",
    "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    # Glycine
    "GGT": "G", "GGC": "G",
    "GGA": "G", "GGG": "G",

    # Stop codons
    "TAA": "*",
    "TAG": "*",
    "TGA": "*"
}

def translate_dna(sequence):
    """Translate a DNA sequence into a protein sequence using the genetic code."""
    
    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]

        if len(codon) < 3:
            break  

        if genetic_code.get(codon) == "*":
            break

        protein_sequence += genetic_code.get(codon, "?")

    return protein_sequence

def find_errors(sequence):
    """Count the number of invalid nucleotide characters in the sequence."""
    
    valid_nucleotides = set("ACGT")
    errors = []
    for position, nucleotide in enumerate(sequence, start=1):
        if nucleotide not in valid_nucleotides:
            errors.append((position, nucleotide))
    return errors

def main():
    file_path = Path(r"Enter the path to your FASTA file here")
    sequences = read_fasta(file_path)

    for name, sequence in sequences.items():
        errors = find_errors(sequence)
        print("-" * 50)
        print(f"Sequence: {name}")

        if not errors:
            protein = translate_dna(sequence)

            print("Status: Valid ✅")
            print()

            print("DNA:")
            print(sequence)
            print()

            print("Protein:")
            print(protein)

        else:
            print("Status: Invalid ❌")
            print(f"Errors Found: {len(errors)}")

            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")

if __name__ == "__main__":
    main()
