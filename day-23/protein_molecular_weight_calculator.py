from pathlib import Path

from genetic_code import GENETIC_CODE

from amino_acid_weight import AMINO_ACID_WEIGHTS

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

def translate_dna(sequence):
    """Translate a DNA sequence into a protein sequence using the genetic code."""
    
    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]

        if len(codon) < 3:
            break  
        amino_acid = GENETIC_CODE.get(codon, "?")
        if amino_acid == "*":
            break

        protein_sequence += amino_acid

    return protein_sequence

def calculate_molecular_weight(protein):
    """Calculate the molecular weight of a protein sequence."""
    total_weight = 0

    for amino_acid in protein:
        total_weight += AMINO_ACID_WEIGHTS[amino_acid]

    return total_weight

def print_protein_report(sequence_name, protein, molecular_weight):
    """Print a molecular weight report for a protein sequence."""
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()
    
    print("Protein:")
    print(protein)
    print()

    print("Length")
    print(f"{len(protein)} aa")
    print()

    print("Molecular Weight:")
    print(f"{molecular_weight:.2f} Da")
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
        protein = translate_dna(sequence)
        if not protein:
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Valid ✅")
            print()
            print("Protein:")
            print("No amino acids were translated.")
            print()
            continue
        molecular_weight = calculate_molecular_weight(protein)
        print_protein_report(sequence_name, protein, molecular_weight)

if __name__ == "__main__":
    main()  