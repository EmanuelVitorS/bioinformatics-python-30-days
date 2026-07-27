from pathlib import Path

from genetic_code import GENETIC_CODE

from amino_acid_classes import AMINO_ACID_CLASSES

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

def count_amino_acid_classes(protein):
    """Count the amino acids belonging to each biochemical class."""

    class_counts = {
        class_name: 0
    for class_name in AMINO_ACID_CLASSES
    }

    for amino_acid in protein:
        for class_name, amino_acids in AMINO_ACID_CLASSES.items():
            if amino_acid in amino_acids:

                if class_name in class_counts:
                    class_counts[class_name] += 1      
                break
                
    return class_counts

def calculate_class_percentages(class_counts):
    """Calculate the percentage represented by each amino acid class."""

    class_percentages = {}

    total_amino_acids = sum(class_counts.values())

    if total_amino_acids == 0:
        for class_name in class_counts:
            class_percentages[class_name] = 0
        return class_percentages

    for class_name, count in class_counts.items():
        percentage = count / total_amino_acids * 100
        class_percentages[class_name] = percentage

    return class_percentages

def print_protein_report(
    sequence_name,
    protein,
    class_counts,
    class_percentages
):
    """Print a report of the amino acid class composition of a protein."""

    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()
    print("Protein:")
    print(protein)
    print()
    print(f"Length: {len(protein)} aa")
    print()
    print("Amino Acid Class Composition:")
    for class_name, count in class_counts.items():
        print(f"{class_name}: {count} ({class_percentages[class_name]:.2f}%)")
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
        class_counts = count_amino_acid_classes(protein)
        class_percentages = calculate_class_percentages(class_counts)

        print_protein_report(
        sequence_name,
        protein,
        class_counts,
        class_percentages
    )

if __name__ == "__main__":
    main()  

