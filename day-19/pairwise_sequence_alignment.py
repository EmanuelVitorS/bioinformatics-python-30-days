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

def calculate_alignment_score(
    sequence1,
    sequence2,
    match_score=1,
    mismatch_score=-1
):
    score = 0

    for base1, base2 in zip(sequence1, sequence2):
        if base1 == base2:
            score += match_score
        else:
            score += mismatch_score

    return score


def align_sequences(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        return []

    matches = 0
    mismatches = 0
    alignment = ""

    for sequence1_base, sequence2_base in zip(sequence1, sequence2):
        if sequence1_base == sequence2_base:
            matches += 1
            alignment += "|"
        else:
            mismatches += 1
            alignment += " "

    identity = (matches / len(sequence1)) * 100
    score = calculate_alignment_score(sequence1, sequence2)

    return {
        "matches": matches,
        "mismatches": mismatches,
        "identity": identity,
        "alignment": alignment,
        "score": score
    }

def print_alignment_report(
    sequence1_name,
    sequence2_name,
    sequence1,
    sequence2,
    alignment_data
):
    print("-" * 50)

    print(f"Sequence 1: {sequence1_name}")
    print(f"Sequence 2: {sequence2_name}")
    print()

    print(sequence1)
    print(alignment_data["alignment"])
    print(sequence2)
    print()

    print(f"Matches: {alignment_data['matches']}")
    print(f"Mismatches: {alignment_data['mismatches']}")
    print(f"Identity: {alignment_data['identity']:.2f}%")
    print(f"Alignment Score: {alignment_data['score']}")

def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    sequences = read_fasta(file_path)

    sequence_items = list(sequences.items())

    if len(sequence_items) < 2:
        print("The FASTA file must contain at least two sequences.")
        return

    sequence_name1, sequence1 = sequence_items[0]
    sequence_name2, sequence2 = sequence_items[1]

    errors1 = find_errors(sequence1)
    errors2 = find_errors(sequence2)

    if errors1:
        print("-" * 50)
        print(f"Sequence: {sequence_name1}")
        print("Status: Invalid")
        print(f"Errors found: {len(errors1)}")

        for position, nucleotide in errors1:
            print(f"Position {position}: {nucleotide}")

        print()

    if errors2:
        print("-" * 50)
        print(f"Sequence: {sequence_name2}")
        print("Status: Invalid")
        print(f"Errors found: {len(errors2)}")

        for position, nucleotide in errors2:
            print(f"Position {position}: {nucleotide}")

        print()

    if errors1 or errors2:
        return

    alignment_data = align_sequences(sequence1, sequence2)

    if alignment_data is None:
        print("The sequences must have the same length.")
        return

    print_alignment_report(
        sequence_name1,
        sequence_name2,
        sequence1,
        sequence2,
        alignment_data
    )

if __name__ == "__main__":
    main()       