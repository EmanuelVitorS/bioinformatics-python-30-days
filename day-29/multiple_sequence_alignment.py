from pathlib import Path


MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_PENALTY = -2


def read_fasta(file_path):
    """Read a FASTA file and return a dictionary of sequences."""

    sequences = {}
    sequence_name = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                sequence_name = line[1:].strip()

                if not sequence_name:
                    raise ValueError(
                        "FASTA headers cannot be empty."
                    )

                sequences[sequence_name] = ""

            else:
                if not sequence_name:
                    raise ValueError(
                        "A sequence was found before a FASTA header."
                    )

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
    """Create a Needleman-Wunsch score matrix."""

    rows = len(sequence_2) + 1
    columns = len(sequence_1) + 1

    score_matrix = [
        [0 for _ in range(columns)]
        for _ in range(rows)
    ]

    return score_matrix


def initialize_score_matrix(score_matrix, gap_penalty):
    """Initialize the first row and column with gap penalties."""

    for column in range(1, len(score_matrix[0])):
        score_matrix[0][column] = (
            score_matrix[0][column - 1]
            + gap_penalty
        )

    for row in range(1, len(score_matrix)):
        score_matrix[row][0] = (
            score_matrix[row - 1][0]
            + gap_penalty
        )


def fill_score_matrix(
    sequence_1,
    sequence_2,
    score_matrix,
    match_score,
    mismatch_score,
    gap_penalty
):
    """Fill a global alignment score matrix."""

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

            score_matrix[row][column] = max(
                diagonal_score,
                up_score,
                left_score
            )


def traceback_global_alignment(
    sequence_1,
    sequence_2,
    score_matrix,
    match_score,
    mismatch_score,
    gap_penalty
):
    """Build a global alignment by tracing through the score matrix."""

    aligned_sequence_1 = ""
    aligned_sequence_2 = ""

    row = len(sequence_2)
    column = len(sequence_1)

    while row > 0 or column > 0:
        current_score = score_matrix[row][column]

        if row > 0 and column > 0:
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

            if current_score == diagonal_score:
                aligned_sequence_1 = (
                    nucleotide_1 + aligned_sequence_1
                )

                aligned_sequence_2 = (
                    nucleotide_2 + aligned_sequence_2
                )

                row -= 1
                column -= 1
                continue

        if row > 0:
            up_score = (
                score_matrix[row - 1][column]
                + gap_penalty
            )

            if current_score == up_score:
                aligned_sequence_1 = (
                    "-" + aligned_sequence_1
                )

                aligned_sequence_2 = (
                    sequence_2[row - 1]
                    + aligned_sequence_2
                )

                row -= 1
                continue

        if column > 0:
            aligned_sequence_1 = (
                sequence_1[column - 1]
                + aligned_sequence_1
            )

            aligned_sequence_2 = (
                "-" + aligned_sequence_2
            )

            column -= 1

    return aligned_sequence_1, aligned_sequence_2


def global_pairwise_alignment(sequence_1, sequence_2):
    """Perform a Needleman-Wunsch global alignment."""

    score_matrix = create_score_matrix(
        sequence_1,
        sequence_2
    )

    initialize_score_matrix(
        score_matrix,
        GAP_PENALTY
    )

    fill_score_matrix(
        sequence_1,
        sequence_2,
        score_matrix,
        MATCH_SCORE,
        MISMATCH_SCORE,
        GAP_PENALTY
    )

    aligned_sequence_1, aligned_sequence_2 = (
        traceback_global_alignment(
            sequence_1,
            sequence_2,
            score_matrix,
            MATCH_SCORE,
            MISMATCH_SCORE,
            GAP_PENALTY
        )
    )

    final_score = score_matrix[-1][-1]

    return (
        aligned_sequence_1,
        aligned_sequence_2,
        final_score
    )


def merge_reference_alignments(
    multiple_alignment,
    new_aligned_reference,
    new_aligned_sequence
):
    """
    Merge a new pairwise alignment into an existing multiple alignment.

    The first sequence in multiple_alignment is the current gapped
    reference sequence.
    """

    current_reference = multiple_alignment[0]

    merged_existing_sequences = [
        ""
        for _ in multiple_alignment
    ]

    merged_new_sequence = ""

    current_position = 0
    new_position = 0

    while (
        current_position < len(current_reference)
        or new_position < len(new_aligned_reference)
    ):
        if current_position >= len(current_reference):
            for index in range(len(multiple_alignment)):
                merged_existing_sequences[index] += "-"

            merged_new_sequence += (
                new_aligned_sequence[new_position]
            )

            new_position += 1
            continue

        if new_position >= len(new_aligned_reference):
            for index, aligned_sequence in enumerate(
                multiple_alignment
            ):
                merged_existing_sequences[index] += (
                    aligned_sequence[current_position]
                )

            merged_new_sequence += "-"
            current_position += 1
            continue

        current_character = current_reference[
            current_position
        ]

        new_character = new_aligned_reference[
            new_position
        ]

        if (
            current_character == new_character
            and current_character != "-"
        ):
            for index, aligned_sequence in enumerate(
                multiple_alignment
            ):
                merged_existing_sequences[index] += (
                    aligned_sequence[current_position]
                )

            merged_new_sequence += (
                new_aligned_sequence[new_position]
            )

            current_position += 1
            new_position += 1

        elif (
            current_character == "-"
            and new_character == "-"
        ):
            for index, aligned_sequence in enumerate(
                multiple_alignment
            ):
                merged_existing_sequences[index] += (
                    aligned_sequence[current_position]
                )

            merged_new_sequence += (
                new_aligned_sequence[new_position]
            )

            current_position += 1
            new_position += 1

        elif current_character == "-":
            for index, aligned_sequence in enumerate(
                multiple_alignment
            ):
                merged_existing_sequences[index] += (
                    aligned_sequence[current_position]
                )

            merged_new_sequence += "-"
            current_position += 1

        elif new_character == "-":
            for index in range(len(multiple_alignment)):
                merged_existing_sequences[index] += "-"

            merged_new_sequence += (
                new_aligned_sequence[new_position]
            )

            new_position += 1

        else:
            raise ValueError(
                "Reference alignments could not be merged."
            )

    merged_existing_sequences.append(
        merged_new_sequence
    )

    return merged_existing_sequences


def build_multiple_alignment(sequences):
    """
    Build a simplified progressive multiple sequence alignment.

    The first sequence is used as the reference sequence.
    """

    sequence_items = list(sequences.items())

    reference_name, reference_sequence = sequence_items[0]

    aligned_names = [reference_name]
    multiple_alignment = [reference_sequence]

    pairwise_scores = {}

    for sequence_name, sequence in sequence_items[1:]:
        (
            aligned_reference,
            aligned_sequence,
            alignment_score
        ) = global_pairwise_alignment(
            reference_sequence,
            sequence
        )

        multiple_alignment = merge_reference_alignments(
            multiple_alignment,
            aligned_reference,
            aligned_sequence
        )

        aligned_names.append(sequence_name)

        pairwise_scores[sequence_name] = alignment_score

    return (
        aligned_names,
        multiple_alignment,
        pairwise_scores
    )


def count_column_bases(column):
    """Count nucleotides in one alignment column."""

    base_counts = {}

    for nucleotide in column:
        if nucleotide == "-":
            continue

        if nucleotide not in base_counts:
            base_counts[nucleotide] = 1
        else:
            base_counts[nucleotide] += 1

    return base_counts


def find_most_frequent_base(base_counts):
    """Return the most frequent nucleotide in a column."""

    if not base_counts:
        return "-"

    highest_count = max(base_counts.values())

    tied_bases = [
        base
        for base, count in base_counts.items()
        if count == highest_count
    ]

    return sorted(tied_bases)[0]


def build_consensus(multiple_alignment):
    """Build a consensus sequence from a multiple alignment."""

    if not multiple_alignment:
        return ""

    consensus = ""
    alignment_length = len(multiple_alignment[0])

    for position in range(alignment_length):
        column = [
            sequence[position]
            for sequence in multiple_alignment
        ]

        base_counts = count_column_bases(column)

        most_frequent_base = find_most_frequent_base(
            base_counts
        )

        consensus += most_frequent_base

    return consensus


def calculate_conservation(multiple_alignment):
    """Calculate the conservation percentage of each column."""

    conservation_percentages = []

    if not multiple_alignment:
        return conservation_percentages

    sequence_count = len(multiple_alignment)
    alignment_length = len(multiple_alignment[0])

    for position in range(alignment_length):
        column = [
            sequence[position]
            for sequence in multiple_alignment
        ]

        base_counts = count_column_bases(column)

        if not base_counts:
            conservation = 0.0
        else:
            highest_count = max(base_counts.values())

            conservation = (
                highest_count / sequence_count
            ) * 100

        conservation_percentages.append(
            conservation
        )

    return conservation_percentages


def create_conservation_line(conservation_percentages):
    """Create symbols representing alignment conservation."""

    conservation_line = ""

    for conservation in conservation_percentages:
        if conservation == 100:
            conservation_line += "*"
        elif conservation >= 75:
            conservation_line += ":"
        elif conservation >= 50:
            conservation_line += "."
        else:
            conservation_line += " "

    return conservation_line


def calculate_pairwise_identity(
    aligned_sequence_1,
    aligned_sequence_2
):
    """Calculate identity between two aligned sequences."""

    if len(aligned_sequence_1) != len(aligned_sequence_2):
        raise ValueError(
            "Aligned sequences must have the same length."
        )

    compared_positions = 0
    matches = 0

    for nucleotide_1, nucleotide_2 in zip(
        aligned_sequence_1,
        aligned_sequence_2
    ):
        if nucleotide_1 == "-" and nucleotide_2 == "-":
            continue

        compared_positions += 1

        if (
            nucleotide_1 == nucleotide_2
            and nucleotide_1 != "-"
        ):
            matches += 1

    if compared_positions == 0:
        return 0.0

    return (
        matches / compared_positions
    ) * 100


def calculate_identity_matrix(
    aligned_names,
    multiple_alignment
):
    """Calculate pairwise identities for all aligned sequences."""

    identity_matrix = {}

    for first_index in range(len(multiple_alignment)):
        first_name = aligned_names[first_index]

        identity_matrix[first_name] = {}

        for second_index in range(len(multiple_alignment)):
            second_name = aligned_names[second_index]

            identity = calculate_pairwise_identity(
                multiple_alignment[first_index],
                multiple_alignment[second_index]
            )

            identity_matrix[first_name][second_name] = (
                identity
            )

    return identity_matrix


def print_identity_matrix(
    aligned_names,
    identity_matrix
):
    """Print the pairwise identity matrix."""

    print("\nPairwise identity matrix (%):\n")

    name_width = max(
        12,
        max(len(name) for name in aligned_names) + 2
    )

    print(" " * name_width, end="")

    for name in aligned_names:
        print(f"{name:>12}", end="")

    print()

    for first_name in aligned_names:
        print(f"{first_name:<{name_width}}", end="")

        for second_name in aligned_names:
            identity = identity_matrix[
                first_name
            ][second_name]

            print(f"{identity:12.2f}", end="")

        print()


def print_conservation_report(
    conservation_percentages
):
    """Print conservation percentages for alignment columns."""

    print("\nConservation by position:\n")

    for position, conservation in enumerate(
        conservation_percentages,
        start=1
    ):
        print(
            f"Position {position}: "
            f"{conservation:.2f}%"
        )


def print_alignment_report(
    aligned_names,
    multiple_alignment,
    consensus,
    conservation_percentages,
    pairwise_scores
):
    """Print the multiple sequence alignment report."""

    conservation_line = create_conservation_line(
        conservation_percentages
    )

    print("\n" + "-" * 70)
    print("Progressive Multiple Sequence Alignment")
    print("-" * 70)

    print(f"Number of sequences: {len(aligned_names)}")
    print(
        f"Alignment length: "
        f"{len(multiple_alignment[0])}"
    )

    print("\nMultiple alignment:\n")

    name_width = max(
        len(name)
        for name in aligned_names
    ) + 2

    for sequence_name, aligned_sequence in zip(
        aligned_names,
        multiple_alignment
    ):
        print(
            f"{sequence_name:<{name_width}}"
            f"{aligned_sequence}"
        )

    print(
        f"{'Conservation':<{name_width}}"
        f"{conservation_line}"
    )

    print(
        f"{'Consensus':<{name_width}}"
        f"{consensus}"
    )

    print("\nConservation symbols:")
    print("* = 100% conserved")
    print(": = at least 75% conserved")
    print(". = at least 50% conserved")
    print("  = less than 50% conserved")

    if pairwise_scores:
        print("\nReference pairwise scores:")

        reference_name = aligned_names[0]
        print(f"Reference sequence: {reference_name}")

        for sequence_name, score in pairwise_scores.items():
            print(f"{sequence_name}: {score}")


def main():
    file_path = Path(
        input("Enter the path to your FASTA file: ")
    )

    try:
        sequences = read_fasta(file_path)

    except FileNotFoundError:
        print("Error: FASTA file not found.")
        return

    except ValueError as error:
        print(f"Error: {error}")
        return

    if len(sequences) < 2:
        print(
            "Error: the FASTA file must contain "
            "at least two sequences."
        )
        return

    invalid_sequences_found = False

    for sequence_name, sequence in sequences.items():
        errors = find_errors(sequence)

        if errors:
            invalid_sequences_found = True

            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Invalid ❌")
            print(f"Errors found: {len(errors)}")

            for position, nucleotide in errors:
                print(
                    f"Position {position}: "
                    f"{nucleotide}"
                )

            print()

    if invalid_sequences_found:
        return

    (
        aligned_names,
        multiple_alignment,
        pairwise_scores
    ) = build_multiple_alignment(sequences)

    consensus = build_consensus(
        multiple_alignment
    )

    conservation_percentages = calculate_conservation(
        multiple_alignment
    )

    identity_matrix = calculate_identity_matrix(
        aligned_names,
        multiple_alignment
    )

    print_alignment_report(
        aligned_names,
        multiple_alignment,
        consensus,
        conservation_percentages,
        pairwise_scores
    )

    print_identity_matrix(
        aligned_names,
        identity_matrix
    )

    print_conservation_report(
        conservation_percentages
    )

if __name__ == "__main__":
    main()