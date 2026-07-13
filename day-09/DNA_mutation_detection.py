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

def find_mutations(reference, sample):
    if len(reference) != len(sample):
        return []
    mutations = []
    for position, (reference_base, sample_base) in enumerate(zip(reference, sample), start=1):
        if reference_base != sample_base:
            mutations.append((position, reference_base, sample_base))
    return mutations

def main():
    file_path = Path(r"E:\bioinformatics-python-30-days\teste_100.fasta.txt")
    sequences = read_fasta(file_path)
    items = list(sequences.items())

    for i in range(0, len(items), 2):
        name1, sequence1 = items[i]
        name2, sequence2 = items[i + 1]
        errors1 = find_errors(sequence1)
        errors2 = find_errors(sequence2)

        if i + 1 >= len(items):
            print("The last sequence has no pair for comparison.")
            break

        if len(sequence1) != len(sequence2):
            print("-" * 50)
            print("Status: Cannot compare")
            print()
            print(f"Reference: {name1}")
            print(f"Sample: {name2}")
            print("Sequences have different lengths.")
            continue

        if not errors1 and not errors2:
            mutations = find_mutations(sequence1, sequence2)
            print("-" * 50)
            print("Status: Valid ✅")
            print()
            print(f"Comparing:")
            print(f"Reference: {name1}")
            print(f"Sample: {name2}")
            for (position, reference_base, sample_base) in mutations:
                print(f"Base {position}: {reference_base} -> {sample_base}")
            if not mutations:
                print("No mutations found.")

        else:
            print("-" * 50)
            print(f"Comparing: {name1} and {name2}")
            print("Status: Invalid ❌")
            print()
            print("Reference:")
            for position, nucleotide in errors1:
                print(f"Position {position}: {nucleotide}")
            print()
            print("Sample:")
            for position, nucleotide in errors2:
                print(f"Position {position}: {nucleotide}")
if __name__ == "__main__":
    main()