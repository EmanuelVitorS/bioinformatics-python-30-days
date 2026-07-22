from pathlib import Path

from restriction_enzyme import RESTRICTION_ENZYMES

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

def find_restriction_sites(sequence):
    sites_found = {}

    for enzyme_name, recognition_sequence in RESTRICTION_ENZYMES.items():
        positions = []

        for position in range(len(sequence) - len(recognition_sequence) + 1):
            if sequence[position:position + len(recognition_sequence)] == recognition_sequence:
                positions.append(position + 1)

        sites_found[enzyme_name] = positions

    return sites_found


def print_restriction_report(sequence_name, restriction_sites):
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print()

    for enzyme_name, recognition_sequence in RESTRICTION_ENZYMES.items():

        positions = restriction_sites[enzyme_name]
        print(f"{enzyme_name}")
        print(f"Recognition sequence: {recognition_sequence}")

        if positions:
            formatted_positions = ", ".join(str(position) for position in positions)
            print(f"Sites found: {len(positions)}")
            print(f"Positions: {formatted_positions}")

        else:
            print("No restriction sites found.")

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

        restriction_sites = find_restriction_sites(sequence)

        print_restriction_report(sequence_name, restriction_sites)        

if __name__ == "__main__":
    main()       