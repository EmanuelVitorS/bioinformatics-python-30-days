from pathlib import Path


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

                if sequence_name in sequences:
                    raise ValueError(
                        f"Duplicate FASTA header: {sequence_name}"
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


def validate_sequence_lengths(sequences):
    """Return True if all sequences have the same length."""

    sequence_lengths = {
        len(sequence)
        for sequence in sequences.values()
    }

    return len(sequence_lengths) == 1


def calculate_sequence_distance(sequence_1, sequence_2):
    """
    Calculate the normalized Hamming distance between two sequences.

    Distance is the number of mismatches divided by sequence length.
    """

    if len(sequence_1) != len(sequence_2):
        raise ValueError(
            "Sequences must have the same length."
        )

    if not sequence_1:
        return 0.0

    mismatches = 0

    for nucleotide_1, nucleotide_2 in zip(
        sequence_1,
        sequence_2
    ):
        if nucleotide_1 != nucleotide_2:
            mismatches += 1

    distance = mismatches / len(sequence_1)

    return distance


def build_distance_matrix(sequences):
    """Build a pairwise distance matrix for all sequences."""

    sequence_names = list(sequences.keys())
    distance_matrix = {}

    for first_name in sequence_names:
        distance_matrix[first_name] = {}

        for second_name in sequence_names:
            if first_name == second_name:
                distance = 0.0
            else:
                distance = calculate_sequence_distance(
                    sequences[first_name],
                    sequences[second_name]
                )

            distance_matrix[first_name][second_name] = distance

    return distance_matrix


def find_closest_clusters(distance_matrix):
    """Return the two clusters with the smallest distance."""

    cluster_names = list(distance_matrix.keys())

    closest_cluster_1 = None
    closest_cluster_2 = None
    smallest_distance = float("inf")

    for first_index in range(len(cluster_names)):
        for second_index in range(
            first_index + 1,
            len(cluster_names)
        ):
            first_cluster = cluster_names[first_index]
            second_cluster = cluster_names[second_index]

            distance = distance_matrix[
                first_cluster
            ][second_cluster]

            if distance < smallest_distance:
                smallest_distance = distance
                closest_cluster_1 = first_cluster
                closest_cluster_2 = second_cluster

    return (
        closest_cluster_1,
        closest_cluster_2,
        smallest_distance
    )


def format_branch_length(branch_length):
    """Format a branch length for Newick output."""

    return f"{branch_length:.4f}".rstrip("0").rstrip(".")


def create_new_cluster(
    cluster_1,
    cluster_2,
    distance,
    clusters
):
    """Create a new UPGMA cluster from two existing clusters."""

    cluster_data_1 = clusters[cluster_1]
    cluster_data_2 = clusters[cluster_2]

    new_height = distance / 2

    branch_length_1 = (
        new_height - cluster_data_1["height"]
    )

    branch_length_2 = (
        new_height - cluster_data_2["height"]
    )

    newick = (
        f"({cluster_data_1['newick']}:"
        f"{format_branch_length(branch_length_1)},"
        f"{cluster_data_2['newick']}:"
        f"{format_branch_length(branch_length_2)})"
    )

    new_cluster_name = f"({cluster_1}+{cluster_2})"

    new_cluster_data = {
        "newick": newick,
        "size": (
            cluster_data_1["size"]
            + cluster_data_2["size"]
        ),
        "height": new_height
    }

    return new_cluster_name, new_cluster_data


def calculate_new_cluster_distance(
    cluster_1,
    cluster_2,
    other_cluster,
    distance_matrix,
    clusters
):
    """
    Calculate the weighted average distance from a new cluster
    to another cluster.
    """

    size_1 = clusters[cluster_1]["size"]
    size_2 = clusters[cluster_2]["size"]

    distance_1 = distance_matrix[
        cluster_1
    ][other_cluster]

    distance_2 = distance_matrix[
        cluster_2
    ][other_cluster]

    new_distance = (
        distance_1 * size_1
        + distance_2 * size_2
    ) / (size_1 + size_2)

    return new_distance


def update_distance_matrix(
    distance_matrix,
    cluster_1,
    cluster_2,
    new_cluster_name,
    clusters
):
    """Update the distance matrix after merging two clusters."""

    remaining_clusters = [
        cluster_name
        for cluster_name in distance_matrix
        if cluster_name not in {cluster_1, cluster_2}
    ]

    new_distances = {}

    for other_cluster in remaining_clusters:
        new_distance = calculate_new_cluster_distance(
            cluster_1,
            cluster_2,
            other_cluster,
            distance_matrix,
            clusters
        )

        new_distances[other_cluster] = new_distance

    distance_matrix.pop(cluster_1)
    distance_matrix.pop(cluster_2)

    for cluster_name in distance_matrix:
        distance_matrix[cluster_name].pop(
            cluster_1,
            None
        )

        distance_matrix[cluster_name].pop(
            cluster_2,
            None
        )

    distance_matrix[new_cluster_name] = {
        new_cluster_name: 0.0
    }

    for other_cluster, distance in new_distances.items():
        distance_matrix[
            new_cluster_name
        ][other_cluster] = distance

        distance_matrix[
            other_cluster
        ][new_cluster_name] = distance


def build_upgma_tree(sequences):
    """Build a UPGMA phylogenetic tree."""

    distance_matrix = build_distance_matrix(
        sequences
    )

    original_distance_matrix = {
        row_name: row.copy()
        for row_name, row in distance_matrix.items()
    }

    clusters = {
        sequence_name: {
            "newick": sequence_name,
            "size": 1,
            "height": 0.0
        }
        for sequence_name in sequences
    }

    clustering_steps = []
    step_number = 1

    while len(distance_matrix) > 1:
        (
            cluster_1,
            cluster_2,
            distance
        ) = find_closest_clusters(
            distance_matrix
        )

        (
            new_cluster_name,
            new_cluster_data
        ) = create_new_cluster(
            cluster_1,
            cluster_2,
            distance,
            clusters
        )

        clustering_steps.append({
            "step": step_number,
            "cluster_1": cluster_1,
            "cluster_2": cluster_2,
            "distance": distance,
            "new_cluster": new_cluster_name,
            "height": new_cluster_data["height"]
        })

        update_distance_matrix(
            distance_matrix,
            cluster_1,
            cluster_2,
            new_cluster_name,
            clusters
        )

        clusters[new_cluster_name] = new_cluster_data

        del clusters[cluster_1]
        del clusters[cluster_2]

        step_number += 1

    final_cluster_name = next(iter(clusters))
    newick_tree = (
        clusters[final_cluster_name]["newick"]
        + ";"
    )

    return (
        newick_tree,
        original_distance_matrix,
        clustering_steps
    )


def print_distance_matrix(
    sequence_names,
    distance_matrix
):
    """Print a formatted pairwise distance matrix."""

    print("\nPairwise distance matrix:\n")

    name_width = max(
        14,
        max(len(name) for name in sequence_names) + 2
    )

    print(" " * name_width, end="")

    for sequence_name in sequence_names:
        print(f"{sequence_name:>14}", end="")

    print()

    for first_name in sequence_names:
        print(
            f"{first_name:<{name_width}}",
            end=""
        )

        for second_name in sequence_names:
            distance = distance_matrix[
                first_name
            ][second_name]

            print(f"{distance:14.4f}", end="")

        print()


def print_clustering_steps(clustering_steps):
    """Print the steps used to build the UPGMA tree."""

    print("\nClustering steps:\n")

    for step_data in clustering_steps:
        print(f"Step {step_data['step']}:")

        print(
            f"  Merge: {step_data['cluster_1']} "
            f"and {step_data['cluster_2']}"
        )

        print(
            f"  Distance: "
            f"{step_data['distance']:.4f}"
        )

        print(
            f"  Cluster height: "
            f"{step_data['height']:.4f}"
        )

        print(
            f"  New cluster: "
            f"{step_data['new_cluster']}"
        )

        print()


def print_phylogenetic_report(
    sequences,
    newick_tree,
    distance_matrix,
    clustering_steps
):
    """Print the UPGMA phylogenetic analysis report."""

    sequence_names = list(sequences.keys())

    print("\n" + "-" * 70)
    print("UPGMA Phylogenetic Tree")
    print("-" * 70)

    print(
        f"Number of sequences: "
        f"{len(sequence_names)}"
    )

    print(
        f"Sequence length: "
        f"{len(next(iter(sequences.values())))} bp"
    )

    print_distance_matrix(
        sequence_names,
        distance_matrix
    )

    print_clustering_steps(
        clustering_steps
    )

    print("Newick tree:\n")
    print(newick_tree)

    print("\nDistance method:")
    print("Normalized Hamming distance")

    print("\nClustering method:")
    print(
        "UPGMA - Unweighted Pair Group "
        "Method with Arithmetic Mean"
    )


def save_newick_tree(newick_tree, output_path):
    """Save a Newick tree to a file."""

    with open(output_path, "w") as file:
        file.write(newick_tree)
        file.write("\n")


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
        if not sequence:
            invalid_sequences_found = True

            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Invalid ❌")
            print("The sequence is empty.")
            print()

            continue

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

    if not validate_sequence_lengths(sequences):
        print(
            "Error: all sequences must have "
            "the same length."
        )

        print()

        for sequence_name, sequence in sequences.items():
            print(
                f"{sequence_name}: "
                f"{len(sequence)} bases"
            )

        return

    (
        newick_tree,
        distance_matrix,
        clustering_steps
    ) = build_upgma_tree(
        sequences
    )

    print_phylogenetic_report(
        sequences,
        newick_tree,
        distance_matrix,
        clustering_steps
    )

    output_path = file_path.with_name(
        "upgma_tree.newick"
    )

    save_newick_tree(
        newick_tree,
        output_path
    )

    print(
        f"\nNewick tree saved to: "
        f"{output_path}"
    )


if __name__ == "__main__":
    main()