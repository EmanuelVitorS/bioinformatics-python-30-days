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

def count_kmers(sequence, k):
    kmer_counts = {}

    for position in range(len(sequence) - k + 1):
        kmer = sequence[position:position + k]

        if kmer not in kmer_counts:
            kmer_counts[kmer] = 1
        else:
            kmer_counts[kmer] += 1

    return kmer_counts

def print_kmer_report(sequence_name, k, kmer_counts):
    print("-" * 50)
    print(f"Sequence: {sequence_name}")
    print(f"k = {k}")
    print()

    print(f"Unique k-mers: {len(kmer_counts)}")
    print()

    print("K-mer Frequencies")

    for kmer in kmer_counts:
        print(f"{kmer}: {kmer_counts[kmer]}")

    print()

def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    try:
        k = int(input("Enter the value of k: "))
    except ValueError:
        print("Invalid value. Please enter an integer.")
        return
    if k <= 0:
        print("k must be greater than 0.")
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

        if k > len(sequence):
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print(f"k = {k}")
            print("k cannot be greater than the sequence length.")
            continue

        kmer_counts = count_kmers(sequence, k)

        print_kmer_report(
            sequence_name,
            k,
            kmer_counts
        )

if __name__ == "__main__":
    main()  

    