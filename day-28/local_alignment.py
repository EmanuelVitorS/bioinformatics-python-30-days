from pathlib import Path


MATCH_SCORE = 2
MISMATCH_SCORE = -1
GAP_PENALTY = -2


def read_fasta(file_path):
    """Read a FASTA file and return a dictionary of sequences."""

    sequences = {}
    sequence_name = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                sequence_name = line[1:]
                sequences[sequence_name] = ""
            else:
                sequences[sequence_name] += line.upper()

    return sequences


def find_errors(sequence):
    """Return invalid nucleotide positions and characters."""

    valid_nucleotides = set("ACGT")
    errors = []

    for position, nucleotide in enumerate(sequence, start=1):
        if nucleotide not in valid_nucleotides:
            errors.append((position, nucleotide))

    return errors


def create_score_matrix(sequence_1, sequence_2):
    """Create a score matrix filled with zeros."""

    rows = len(sequence_2) + 1
    columns = len(sequence_1) + 1

    score_matrix = [
        [0 for _ in range(columns)]
        for _ in range(rows)
    ]

    return score_matrix


def fill_score_matrix(
    sequence_1,
    sequence_2,
    score_matrix,
    match_score,
    mismatch_score,
    gap_penalty
):
    """Fill the score matrix using the Smith-Waterman algorithm."""

    highest_score = 0
    highest_row = 0
    highest_column = 0

    for row in range(1, len(score_matrix)):
        for column in range(1, len(score_matrix[0])):
            nucleotide_1 = sequence_1[column - 1]
            nucleotide_2 = sequence_2[row - 1]

            if nucleotide_1 == nucleotide_2:
                diagonal_value = match_score
            else:
                diagonal_value = mismatch_score

            diagonal_score = (
                score_matrix[row - 1][column - 1]
                + diagonal_value
            )

            up_score = (
                score_matrix[row - 1][column]
                + gap_penalty
            )

            left_score = (
                score_matrix[row][column - 1]
                + gap_penalty
            )

            current_score = max(
                0,
                diagonal_score,
                up_score,
                left_score
            )

            score_matrix[row][column] = current_score

            if current_score > highest_score:
                highest_score = current_score
                highest_row = row
                highest_column = column

    return highest_score, highest_row, highest_column


def traceback_local_alignment(
    sequence_1,
    sequence_2,
    score_matrix,
    start_row,
    start_column,
    match_score,
    mismatch_score,
    gap_penalty
):
    """Trace back from the highest score and build the local alignment."""

    aligned_sequence_1 = ""
    aligned_sequence_2 = ""

    row = start_row
    column = start_column

    end_position_1 = column
    end_position_2 = row

    while (
        row > 0
        and column > 0
        and score_matrix[row][column] != 0
    ):
        current_score = score_matrix[row][column]

        nucleotide_1 = sequence_1[column - 1]
        nucleotide_2 = sequence_2[row - 1]

        if nucleotide_1 == nucleotide_2:
            diagonal_value = match_score
        else:
            diagonal_value = mismatch_score

        diagonal_score = (
            score_matrix[row - 1][column - 1]
            + diagonal_value
        )

        up_score = (
            score_matrix[row - 1][column]
            + gap_penalty
        )

        left_score = (
            score_matrix[row][column - 1]
            + gap_penalty
        )

        if current_score == diagonal_score:
            aligned_sequence_1 = (
                nucleotide_1 + aligned_sequence_1
            )

            aligned_sequence_2 = (
                nucleotide_2 + aligned_sequence_2
            )

            row -= 1
            column -= 1

        elif current_score == up_score:
            aligned_sequence_1 = (
                "-" + aligned_sequence_1
            )

            aligned_sequence_2 = (
                nucleotide_2 + aligned_sequence_2
            )

            row -= 1

        elif current_score == left_score:
            aligned_sequence_1 = (
                nucleotide_1 + aligned_sequence_1
            )

            aligned_sequence_2 = (
                "-" + aligned_sequence_2
            )

            column -= 1

        else:
            break

    start_position_1 = column + 1
    start_position_2 = row + 1

    return (
        aligned_sequence_1,
        aligned_sequence_2,
        start_position_1,
        end_position_1,
        start_position_2,
        end_position_2
    )


def create_match_line(
    aligned_sequence_1,
    aligned_sequence_2
):
    """Create a visual line showing matches, mismatches, and gaps."""

    match_line = ""

    for nucleotide_1, nucleotide_2 in zip(
        aligned_sequence_1,
        aligned_sequence_2
    ):
        if nucleotide_1 == nucleotide_2:
            match_line += "|"
        elif nucleotide_1 == "-" or nucleotide_2 == "-":
            match_line += " "
        else:
            match_line += "."

    return match_line


def calculate_identity(
    aligned_sequence_1,
    aligned_sequence_2
):
    """Calculate the identity percentage of a local alignment."""

    if not aligned_sequence_1:
        return 0.0

    matches = 0

    for nucleotide_1, nucleotide_2 in zip(
        aligned_sequence_1,
        aligned_sequence_2
    ):
        if nucleotide_1 == nucleotide_2:
            matches += 1

    identity = (
        matches / len(aligned_sequence_1)
    ) * 100

    return identity


def calculate_alignment_statistics(
    aligned_sequence_1,
    aligned_sequence_2
):
    """Count matches, mismatches, and gaps."""

    matches = 0
    mismatches = 0
    gaps = 0

    for nucleotide_1, nucleotide_2 in zip(
        aligned_sequence_1,
        aligned_sequence_2
    ):
        if nucleotide_1 == "-" or nucleotide_2 == "-":
            gaps += 1
        elif nucleotide_1 == nucleotide_2:
            matches += 1
        else:
            mismatches += 1

    return matches, mismatches, gaps


def print_score_matrix(
    sequence_1,
    sequence_2,
    score_matrix
):
    """Print the Smith-Waterman score matrix."""

    print("\nScore matrix:\n")

    print("      -", end="")

    for nucleotide in sequence_1:
        print(f"{nucleotide:5}", end="")

    print()

    for row, values in enumerate(score_matrix):
        if row == 0:
            row_name = "-"
        else:
            row_name = sequence_2[row - 1]

        print(f"{row_name:5}", end="")

        for value in values:
            print(f"{value:5}", end="")

        print()


def print_alignment_report(
    sequence_name_1,
    sequence_name_2,
    aligned_sequence_1,
    aligned_sequence_2,
    start_position_1,
    end_position_1,
    start_position_2,
    end_position_2,
    highest_score,
    identity,
    matches,
    mismatches,
    gaps
):
    """Print the local sequence alignment report."""

    match_line = create_match_line(
        aligned_sequence_1,
        aligned_sequence_2
    )

    print("\n" + "-" * 60)
    print("Smith-Waterman Local Alignment")
    print("-" * 60)

    print(f"Sequence 1: {sequence_name_1}")
    print(f"Sequence 2: {sequence_name_2}")

    print("\nBest local alignment:\n")

    print(aligned_sequence_1)
    print(match_line)
    print(aligned_sequence_2)

    print("\nAlignment positions:")
    print(
        f"{sequence_name_1}: "
        f"{start_position_1}-{end_position_1}"
    )
    print(
        f"{sequence_name_2}: "
        f"{start_position_2}-{end_position_2}"
    )

    print("\nAlignment statistics:")
    print(f"Alignment length: {len(aligned_sequence_1)}")
    print(f"Matches: {matches}")
    print(f"Mismatches: {mismatches}")
    print(f"Gaps: {gaps}")
    print(f"Identity: {identity:.2f}%")
    print(f"Highest local alignment score: {highest_score}")

    print("\nScoring system:")
    print(f"Match: {MATCH_SCORE}")
    print(f"Mismatch: {MISMATCH_SCORE}")
    print(f"Gap: {GAP_PENALTY}")


def main():
    file_path = Path(
        input("Enter the path to your FASTA file: ")
    )

    try:
        sequences = read_fasta(file_path)
    except FileNotFoundError:
        print("Error: FASTA file not found.")
        return

    if len(sequences) != 2:
        print(
            "Error: the FASTA file must contain "
            "exactly two sequences."
        )
        return

    sequence_items = list(sequences.items())

    sequence_name_1, sequence_1 = sequence_items[0]
    sequence_name_2, sequence_2 = sequence_items[1]

    errors_1 = find_errors(sequence_1)
    errors_2 = find_errors(sequence_2)

    if errors_1:
        print(f"\nSequence: {sequence_name_1}")
        print("Status: Invalid ❌")

        for position, nucleotide in errors_1:
            print(f"Position {position}: {nucleotide}")

    if errors_2:
        print(f"\nSequence: {sequence_name_2}")
        print("Status: Invalid ❌")

        for position, nucleotide in errors_2:
            print(f"Position {position}: {nucleotide}")

    if errors_1 or errors_2:
        return

    score_matrix = create_score_matrix(
        sequence_1,
        sequence_2
    )

    (
        highest_score,
        highest_row,
        highest_column
    ) = fill_score_matrix(
        sequence_1,
        sequence_2,
        score_matrix,
        MATCH_SCORE,
        MISMATCH_SCORE,
        GAP_PENALTY
    )

    if highest_score == 0:
        print(
            "No local alignment with a positive score "
            "was found."
        )
        return

    (
        aligned_sequence_1,
        aligned_sequence_2,
        start_position_1,
        end_position_1,
        start_position_2,
        end_position_2
    ) = traceback_local_alignment(
        sequence_1,
        sequence_2,
        score_matrix,
        highest_row,
        highest_column,
        MATCH_SCORE,
        MISMATCH_SCORE,
        GAP_PENALTY
    )

    identity = calculate_identity(
        aligned_sequence_1,
        aligned_sequence_2
    )

    matches, mismatches, gaps = (
        calculate_alignment_statistics(
            aligned_sequence_1,
            aligned_sequence_2
        )
    )

    print_score_matrix(
        sequence_1,
        sequence_2,
        score_matrix
    )

    print_alignment_report(
        sequence_name_1,
        sequence_name_2,
        aligned_sequence_1,
        aligned_sequence_2,
        start_position_1,
        end_position_1,
        start_position_2,
        end_position_2,
        highest_score,
        identity,
        matches,
        mismatches,
        gaps
    )


if __name__ == "__main__":
    main()