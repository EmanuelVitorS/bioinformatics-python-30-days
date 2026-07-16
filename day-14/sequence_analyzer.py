from pathlib import Path

from genetic_code import GENETIC_CODE

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

def calculate_at_gc(sequence):
    """Return sequence length and GC percentage."""

    length = len(sequence)

    if length == 0:
        return {
            "length": 0,
            "GC": 0,
            "AT": 0
        }
    count_g = sequence.count("G")
    count_c = sequence.count("C")
    count_a = sequence.count("A")
    count_t = sequence.count("T")

    gc_content = ((count_g + count_c) / length) * 100
    at_content = ((count_a + count_t) / length) * 100
    return {
        "length": length,
        "GC": gc_content,
        "AT": at_content
    }


def transcribe_dna(sequence): 
    """Transcribe a DNA sequence into RNA.""" 
    return sequence.replace("T", "U")

def translate_dna(sequence):
    """Translate a DNA sequence into a protein sequence using the genetic code."""
    
    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]

        if len(codon) < 3:
            break  
        amino_acid = GENETIC_CODE.get(codon, "?")
        if amino_acid == "*":
            break

        protein_sequence += amino_acid

    return protein_sequence

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

def analyze_sequence(sequence):

    stats = calculate_at_gc(sequence)

    result = {
        "length": stats["length"],
        "GC": stats["GC"],
        "AT": stats["AT"],
        "errors": find_errors(sequence),
        "rna": transcribe_dna(sequence),
        "protein": translate_dna(sequence),
        "orfs": find_orfs(sequence)
    }

    return result

def print_report(name, result):
    print("=" * 50)
    print(f"Sequence: {name}")
    if result["errors"]:
        print("Status: Invalid ❌")
    else:
        print("Status: Valid ✅")
    print()
    print(f"Length: {result['length']} bp")
    print(f"GC: {result['GC']:.2f}%")
    print(f"AT: {result['AT']:.2f}%")

    print()
    print("RNA:")
    print(result["rna"])

    print()
    print("Protein:")
    print(result["protein"])

    print()
    if result["orfs"]:
        print(f"ORFs found: {len(result['orfs'])}")

        for number, (start, end, orf) in enumerate(result["orfs"], start=1):
            print(f"ORF {number}: {start}-{end}")
            print(orf)
    else:
        print("ORFs found: None")

def main():
    file_path = Path(input("Enter the path to your FASTA file:"))
    sequences = read_fasta(file_path)
    for name, sequence in sequences.items():
        result = analyze_sequence(sequence)
        print_report(name, result)
        
if __name__ == "__main__":
    main()