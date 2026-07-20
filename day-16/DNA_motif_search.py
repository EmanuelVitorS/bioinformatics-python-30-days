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

def find_motif(sequence, motif):
    positions = []

    for position in range(len(sequence) - len(motif) + 1):
        fragment = sequence[position:position + len(motif)]

        if fragment == motif:
            positions.append(position + 1)

    return positions
    
def print_motif_report(sequence_name, motif, positions):
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print(f"Motif: {motif}")
    print()

    if positions:
        print(f"Matches found: {len(positions)}")
        print("Positions:")

        for position in positions:
            print(position)
    else:
        print("Matches found: 0")
        print("Motif not found.")


def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    motif = input("Enter the motif to search: ").strip().upper()

    if not motif:
        print("The motif cannot be empty.")
        return

    if find_errors(motif):
        print("Invalid motif. Use only A, C, G and T.")
        return
    sequences = read_fasta(file_path)

    for sequence_name, sequence in sequences.items():
        errors = find_errors(sequence)

        if errors:
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Invalid")
            print(f"Errors found: {len(errors)}")

            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")

            continue

        positions = find_motif(sequence, motif)
        print_motif_report(sequence_name, motif, positions)
    
if __name__ == "__main__":
    main()    
