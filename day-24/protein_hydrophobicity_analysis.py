from pathlib import Path

from genetic_code import GENETIC_CODE

from amino_acid_hydrophobicity import AMINO_ACID_HYDROPHOBICITY

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

def calculate_average_hydrophobicity(protein):
    """Calculate the average hydrophobicity of a protein sequence."""

    if not protein:
        return 0
    
    total_hydrophobicity = 0

    for amino_acid in protein:
        total_hydrophobicity += AMINO_ACID_HYDROPHOBICITY[amino_acid]

    average_hydrophobicity = total_hydrophobicity / len(protein)

    return average_hydrophobicity

def classify_hydrophobicity(average_hydrophobicity):
    """Return the hydrophobicity classification of a protein."""
    
    if average_hydrophobicity > 1:
        return "Hydrophobic"

    elif average_hydrophobicity >= -1:
        return "Moderately hydrophobic"

    else:
        return "Hydrophilic"

def print_protein_report(
    sequence_name,
    protein,
    average_hydrophobicity,
    classification
):
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()

    print("Protein:")
    print(protein)
    print()

    print("Length:")
    print(f"{len(protein)} aa")
    print()

    print("Average Hydrophobicity:")
    print(f"{average_hydrophobicity:.2f}")
    print()

    print("Classification:")
    print(classification)
    print()

def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    sequences = read_fasta(file_path)

    if not sequences:
        print("No sequences found.")
        return

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
        average_hydrophobicity = calculate_average_hydrophobicity(protein)

        classification = classify_hydrophobicity(average_hydrophobicity) 
        print_protein_report(
        sequence_name,
        protein,
        average_hydrophobicity,
        classification
)


if __name__ == "__main__":
    main()  
