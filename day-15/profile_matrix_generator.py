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

def count_bases(bases):

    base_counts = {}
    for base in bases:
        if base not in base_counts:
            base_counts[base] = 1
        else:
            base_counts[base] += 1
    return base_counts

def most_frequent_base(base_counts):
    highest_count = 0
    most_common = ""

    for base in base_counts:
        if base_counts[base] > highest_count:
            highest_count = base_counts[base]
            most_common = base
    return most_common

def build_profile_matrix(sequences):
    """Build a profile matrix for multiple DNA sequences."""
    profile = {"A": [], "C": [], "G": [], "T": []}

    for position in range(len(sequences[0])):
        bases = ""
        for sequence in sequences:
            bases += sequence[position]
        base_counts = count_bases(bases)
        for nucleotide in profile:
            profile[nucleotide].append(base_counts.get(nucleotide, 0))
    return profile

def build_consensus(profile):
    consensus = ""

    for position in range(len(profile["A"])):
        base_counts = {}
        for nucleotide in profile:
            base_counts[nucleotide] = profile[nucleotide][position]
        most_common = most_frequent_base(base_counts)
        consensus += most_common
    return consensus

def analyze_profile_positions(profile):
    conserved_positions = []
    variable_positions = {}

    for position in range(len(profile["A"])):
        base_counts = {}
        for nucleotide in profile:
            count = profile[nucleotide][position]
            if count > 0:
                base_counts[nucleotide] = count
        if len(base_counts) == 1:
            conserved_positions.append(position + 1)
        else:
            variable_positions[position + 1] = base_counts

    return conserved_positions, variable_positions

def print_profile_report(
    consensus,
    profile,
    conserved_positions,
    variable_positions
):
    print("Consensus sequence:")
    print(consensus)
    print()

    print("Profile Matrix")
    print("     ", end="")
    for position in range(len(profile["A"])):
        print(position + 1, end=" ")
    print()
    for nucleotide in profile:
        print(f"{nucleotide}: ", end="")
        for count in profile[nucleotide]:
            print(count, end=" ")
        print()
    print("-" * 50)
    print("Conserved Positions")
    print(conserved_positions)
    print("-" * 50)
    print("Variable Positions")

    for position in variable_positions:
        print(f"\nPosition {position}")
        for nucleotide in variable_positions[position]:
            print(f"{nucleotide}: {variable_positions[position][nucleotide]}")

def main():
    file_path = Path(input("Enter the path to your FASTA file:"))
    sequences = read_fasta(file_path)
    sequence_list = list(sequences.values())
    profile = build_profile_matrix(sequence_list)
    conserved_positions, variable_positions = analyze_profile_positions(profile)
    consensus = build_consensus(profile)
    print_profile_report(
    consensus,
    profile,
    conserved_positions,
    variable_positions
)
        
if __name__ == "__main__":
    main()