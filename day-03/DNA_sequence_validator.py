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

def find_errors(sequence):
    """Count the number of invalid nucleotide characters in the sequence."""
    valid_nucleotides = set("ACGT")
    errors = []
    for position, nucleotide in enumerate(sequence, start=1):
        if nucleotide not in valid_nucleotides:
            errors.append((position, nucleotide))
    return errors

def main():
    file_path = Path(r"Enter the FASTA file path: ")
    sequences = read_fasta(file_path)

    for name, sequence in sequences.items():
        errors = find_errors(sequence)

        if not errors:
            print(f"Sequence: {name}")
            print("Status: Valid ✅")
        else:
            print(f"Sequence: {name}")
            print("Status: Invalid ❌")
            print(f"Errors Found: {len(errors)}")

        for position, nucleotide in errors:
            print(f"Position {position}: {nucleotide}")

if __name__ == "__main__":
    main()