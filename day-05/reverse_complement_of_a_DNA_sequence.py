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

def complement_dna(sequence):
    """Return the complementary DNA sequence."""
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join(complement[nuc] for nuc in sequence)

def reverse_sequence(sequence):
    """Return the reverse of the sequence."""
    return sequence[::-1]

def reverse_complement(sequence):
    """Return the reverse complement of the DNA sequence."""
    return reverse_sequence(complement_dna(sequence))

def main():
    file_path = Path(r"Enter the path to your FASTA file here")
    sequences = read_fasta(file_path)

    for name, sequence in sequences.items():
        errors = find_errors(sequence)

        if not errors:
            complement = complement_dna(sequence)
            reverse = reverse_sequence(sequence)
            reverse_comp = reverse_complement(sequence)
            print("-" * 50)
            print(f"Sequence: {name}")
            print("Status: Valid ✅")
            print()

            print("Original:")
            print(sequence)
            print()

            print("Complement:")
            print(complement)
            print()

            print("Reverse:")
            print(reverse)
            print()

            print("Reverse Complement:")
            print(reverse_comp)
        else:
            print("-" * 50)
            print(f"Sequence: {name}")
            print("Status: Invalid ❌")
            print()
            print(f"Errors Found: {len(errors)}")

            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")

if __name__ == "__main__":
    main()