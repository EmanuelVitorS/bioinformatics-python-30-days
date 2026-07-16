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

def count_bases(bases):
    count = {}
    for base in bases:
        if base not in count:
            count[base] = 1
        else:
            count[base] += 1
    return count

def build_consensus(sequences):
    consensus = ""
    position_counts = {}
    conserved_positions = []
    for position in range(len(sequences[0])):
        bases = ""
        for sequence in sequences:
            bases += sequence[position]
        counts = count_bases(bases)
        if len(counts) > 1:
            position_counts[position + 1] = counts
        else :
            conserved_positions.append(position + 1)

        most_common = most_frequent_base(bases)
        consensus += most_common
    return consensus, conserved_positions, position_counts

def most_frequent_base(bases):
    base_counts = count_bases(bases)
    highest_count = 0
    most_common = ""

    for base in base_counts:
        if base_counts[base] > highest_count:
            highest_count = base_counts[base]
            most_common = base
    return most_common

def print_consensus_report(consensus,
    sequence_count,
    sequence_length,
    conserved_positions,
    position_counts
):
    print("Consensus sequence:")
    print(consensus)
    print()
    print(f"Number of sequences: {sequence_count}")
    print(f"Sequence length: {sequence_length}")
    print("-" * 50)
    print("Conserved Positions")
    print(conserved_positions)
    print("-" * 50)
    print("Variable positions")
    for position in position_counts:
        print(f"Position {position}")
        for base in position_counts[position]:
            print(f"{base}: {position_counts[position][base]}")

def main():
    file_path = Path(input("Enter the path to your FASTA file:"))
    sequences = read_fasta(file_path)

    if not sequences:
        print("No sequences found.")
        return

    sequence_list = list(sequences.values())
    consensus, conserved_positions, position_counts = build_consensus(sequence_list)
    sequence_count = sequences
    sequence_length = len(sequences)
    print_consensus_report(consensus,
    sequence_count,
    sequence_length,
    conserved_positions,
    position_counts)

if __name__ == "__main__":
    main()
