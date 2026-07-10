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

def calculate_gc(sequence):
    """Return sequence length and GC percentage."""

    length = len(sequence)

    if length == 0:
        return 0, 0

    count_g = sequence.count("G")
    count_c = sequence.count("C")

    gc_content = ((count_g + count_c) / length) * 100

    return length, gc_content

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

def calculate_tm(sequence):
    bases = count_bases(sequence)
    tm = 2 * (bases["A"] + bases["T"]) + 4 * (bases["G"] + bases["C"])    
    return tm

def main():
    file_path = Path(r"E:\bioinformatics-python-30-days\teste_100.fasta.txt")
    sequences = read_fasta(file_path)
    
    for name, sequence in sequences.items():
        errors = find_errors(sequence)
        length, gc = calculate_gc(sequence)
        bases = count_bases(sequence)
        tm = calculate_tm(sequence)

        if not errors:
            print("-" * 50)
            print(f"Sequence: {name}")
            print("Status: Valid ✅")
            print()
            print(f"Length: {length} bp")
            print(f"Tm: {tm} °C") 
            print(f"GC Content: {gc:.2f}%")
            for base, count in bases.items():
                print(f"  {base}: {count}")           
        else:
            print("Status: Invalid ❌")
            print(f"Errors Found: {len(errors)}")

            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")

if __name__ == "__main__":                
    main()