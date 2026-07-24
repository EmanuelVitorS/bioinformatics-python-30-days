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

def count_amino_acids(protein):
    """Count the occurrence of each amino acid in a protein sequence."""
    amino_acid_counts = {}

    for amino_acid in protein:
        if amino_acid not in amino_acid_counts:
            amino_acid_counts[amino_acid] = 1
        else:
            amino_acid_counts[amino_acid] += 1
    return amino_acid_counts


def calculate_frequencies(amino_acid_counts):
    """Calculate the percentage frequency of each amino acid."""
    frequencies = {}
    total = sum(amino_acid_counts.values())

    for amino_acid, count in amino_acid_counts.items():
        frequency = (count / total) * 100
        frequencies[amino_acid] = round(frequency, 2)

    return frequencies
    


def print_amino_acid_report(sequence_name, protein, amino_acid_counts, frequencies):
    """Print an amino acid composition report."""
    
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()

    print("Protein:")
    print(protein)
    print()

    for amino_acid, count in amino_acid_counts.items():
        frequency = frequencies[amino_acid]

        print(f"Amino Acid: {amino_acid}")
        print(f"Count: {count}")
        print(f"Frequency: {frequency:.2f}%")
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

        amino_acid_counts = count_amino_acids(protein)
        frequencies = calculate_frequencies(amino_acid_counts)
        print_amino_acid_report(sequence_name, protein, amino_acid_counts, frequencies)

if __name__ == "__main__":
    main()  
