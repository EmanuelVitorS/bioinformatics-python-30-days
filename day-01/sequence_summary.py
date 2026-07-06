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


def calculate_gc(sequence):
    """Return sequence length and GC percentage."""

    length = len(sequence)

    if length == 0:
        return 0, 0

    count_g = sequence.count("G")
    count_c = sequence.count("C")

    gc_content = ((count_g + count_c) / length) * 100

    return length, gc_content


def main():
    file_path = Path(r"Enter the FASTA file path: ")

    sequences = read_fasta(file_path)

    for name, sequence in sequences.items():
        length, gc = calculate_gc(sequence)
        print(f"\nSequence: {name}")
        print(f"Length: {length} bp")
        print(f"GC Content: {gc:.2f}%")


if __name__ == "__main__":
    main()