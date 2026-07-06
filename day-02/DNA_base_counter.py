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

def calculate_at(sequence):
    """Return sequence length and AT percentage."""

    length = len(sequence)

    if length == 0:
        return 0, 0

    count_a = sequence.count("A")
    count_t = sequence.count("T")

    at_content = ((count_a + count_t) / length) * 100

    return length, at_content   


def count_bases(sequence):
    """Count the occurrences of each DNA base in the sequence."""
    quantity_a = sequence.count("A")
    quantity_t = sequence.count("T")
    quantity_g = sequence.count("G")
    quantity_c = sequence.count("C")

    return {
    "A": quantity_a,
    "T": quantity_t,
    "G": quantity_g,
    "C": quantity_c,
}

def main():
    file_path = Path(r"E:\bioinformatics-python-30-days\teste_100.fasta.txt")
    sequences = read_fasta(file_path)
    

    for name, sequence in sequences.items():
        length, gc = calculate_gc(sequence)
        length, at = calculate_at(sequence)
        bases = count_bases(sequence)

        print(f"\nSequence: {name}")
        print(f"Length: {length} bp")
        print("Base Counts:")
        for base, count in bases.items():
            print(f"  {base}: {count}")
        print(f"GC Content: {gc:.2f}%")
        print(f"AT Content: {at:.2f}%")

if __name__ == "__main__":
    main()