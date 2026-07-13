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

def find_orfs(sequence):
    """Find all open reading frames (ORFs) in the sequence."""
    
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []

    for frame in range(3):
        for i in range(frame, len(sequence) - 2, 3):
            codon = sequence[i:i + 3]
            if codon == start_codon:
                for j in range(i + 3, len(sequence) - 2, 3):
                    stop_codon = sequence[j:j + 3]
                    if stop_codon in stop_codons:
                        orf_sequence = sequence[i:j+3]

                        orfs.append(
                            (i + 1, j + 3, orf_sequence)
                        )

                        break
    return orfs

def main():
    file_path = Path(r"Enter the path to your FASTA file here")
    sequences = read_fasta(file_path)

    for name, sequence in sequences.items():
        errors = find_errors(sequence)
        print("-" * 50)
        print(f"Sequence: {name}")

        if not errors:
            print("Status: Valid ✅")
            print()

            orfs = find_orfs(sequence)

            if orfs:
                print("ORFs:")
                for index, (start, end, orf_seq) in enumerate(orfs, start=1):
                    print(f"ORF {index}")
                    print(f"Position {start}-{end}: {orf_seq}")
            else:
                print("No ORFs found.")
        else:
            print("Status: Invalid ❌")
            print(f"Errors Found: {len(errors)}")
            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")
if __name__ == "__main__":
    main()
