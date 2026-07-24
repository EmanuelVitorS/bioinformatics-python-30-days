from pathlib import Path

from genetic_code import GENETIC_CODE

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
                sequences[name] += line.upper()

    return sequences

def find_errors(sequence):
    """Count the number of invalid nucleotide characters in the sequence."""
    valid_nucleotides = set("ACGT")
    errors = []
    for position, nucleotide in enumerate(sequence, start=1):
        if nucleotide not in valid_nucleotides:
            errors.append((position, nucleotide))
    return errors

def count_codons(sequence):
    """Count complete codons in a DNA sequence."""
    codons_counts = {}

    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]

        if len(codon) < 3:
            break
        
        if codon not in codons_counts:
            codons_counts[codon] = 1

        else:
            codons_counts[codon] += 1

    return codons_counts

def print_count_codons_report(sequence_name, count_codons):
    """Print a codon usage report for a DNA sequence."""

    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()

    for codon, count in count_codons.items():

        amino_acid = GENETIC_CODE.get(codon)

        print(f"Codon: {codon}")
        print(f"Amino acid: {amino_acid}")
        print(f"Count: {count}")
        print()



def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    sequences = read_fasta(file_path)

    for sequence_name, sequence in sequences.items():
        errors = find_errors(sequence)
    
        if errors:
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Invalid ❌")
            print(f"Errors found: {len(errors)}")
    
            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")
    
            print()
            continue

        codons_count = count_codons(sequence)
        print_count_codons_report(sequence_name, codons_count)

if __name__ == "__main__":
    main()  