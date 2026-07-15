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

def build_consensus(sequences):
    consensus = ""
    for position in range(len(sequences[0])):
        bases = ""
        for sequence in sequences:
            bases += sequence[position]
        most_common = most_frequent_base(bases)
        consensus += most_common
    return consensus    

def most_frequent_base(bases):
    base_counts = {}

    for base in bases:
        if base not in base_counts:
            base_counts[base] = 1
        else:
            base_counts[base] += 1

    highest_count = 0
    most_common = ""

    for base in base_counts:
        if base_counts[base] > highest_count:
            highest_count = base_counts[base]
            most_common = base
    return most_common

def main():
    file_path = Path(input("Enter the path to your FASTA file:"))
    sequences = read_fasta(file_path)

    if not sequences:
        print("No sequences found.")
        return

    sequence_list = list(sequences.values())
    consensus = build_consensus(sequence_list)
    print("Consensus sequence:")
    print(consensus)
    print()
    print(f"Number of sequences: {len(sequence_list)}")
    print(f"Sequence length: {len(sequence_list[0])}")

if __name__ == "__main__":
    main()