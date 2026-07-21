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

def translate_reading_frames(sequence):
    """Translate a DNA sequence in the three forward reading frames."""
    proteins = {}

    for frame in range(3):
        frame_sequence = sequence[frame:]
        proteins[frame + 1] = translate_dna(frame_sequence)

    return proteins

def print_translation_report(sequence_name, sequence, proteins):
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print("Status: Valid ✅")
    print()
    print("DNA:")
    print(sequence)
    print()
    for frame, protein in proteins.items():
        print(f"Frame {frame}:")
        print(f"Length: {len(protein)} amino acids")
        if protein:
            print(protein)
        else:
            print("No protein translated.")
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

        proteins = translate_reading_frames(sequence)

        print_translation_report(
            sequence_name,
            sequence,
            proteins
        )

if __name__ == "__main__":
    main()  