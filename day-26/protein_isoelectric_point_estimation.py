from pathlib import Path

from genetic_code import GENETIC_CODE

from amino_acid_pka import (
    AMINO_ACID_PKA,
    N_TERMINUS_PKA,
    C_TERMINUS_PKA
)

from amino_acid_names import AMINO_ACID_NAMES
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

def count_ionizable_amino_acids(protein):
    ionizable_counts = {
    amino_acid: 0
    for amino_acid in AMINO_ACID_PKA
}

    for amino_acid in protein:
        if amino_acid in AMINO_ACID_PKA:
            if amino_acid in ionizable_counts:
                ionizable_counts[amino_acid] += 1

    return ionizable_counts

def calculate_net_charge(ionizable_counts, ph):
    positive_charge = 0
    negative_charge = 0

    positive_amino_acids = {"K", "R", "H"}
    negative_amino_acids = {"D", "E", "C", "Y"}

    n_terminal_charge = 1 / (
        1 + 10 ** (ph - N_TERMINUS_PKA)
    )

    c_terminal_charge = 1 / (
        1 + 10 ** (C_TERMINUS_PKA - ph)
    )

    positive_charge += n_terminal_charge
    negative_charge += c_terminal_charge

    for amino_acid, count in ionizable_counts.items():
        pka = AMINO_ACID_PKA[amino_acid]

        if amino_acid in positive_amino_acids:
            charge = count / (1 + 10 ** (ph - pka))
            positive_charge += charge

        elif amino_acid in negative_amino_acids:
            charge = count / (1 + 10 ** (pka - ph))
            negative_charge += charge

    net_charge = positive_charge - negative_charge

    return net_charge

def estimate_isoelectric_point(ionizable_counts):
    best_ph = 0
    smallest_charge = float("inf")

    ph = 0.0

    while ph <= 14.0:
        net_charge = calculate_net_charge(
            ionizable_counts,
            ph
        )

        absolute_charge = abs(net_charge)

        if absolute_charge < smallest_charge:
            smallest_charge = absolute_charge
            best_ph = ph

        ph += 0.01

    return round(best_ph, 2)

def print_protein_report(
    sequence_name,
    protein,
    ionizable_counts,
    isoelectric_point
):
    print(f"\nSequence: {sequence_name}")
    print(f"Protein: {protein}")
    print(f"Protein length: {len(protein)}")
    print("Ionizable amino acids:")

    if ionizable_counts:
        for amino_acid, count in ionizable_counts.items():
            amino_acid_name = AMINO_ACID_NAMES[amino_acid]

            print(f"{amino_acid} - {amino_acid_name}: {count}")       
    else:
        print("None found")

    print(f"Estimated isoelectric point: {isoelectric_point:.2f}")

def main():
    file_path = Path(input("Enter the path to your FASTA file: "))
    sequences = read_fasta(file_path)

    for sequence_name, sequence in sequences.items():
        errors = find_errors(sequence)
    
        if errors:
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Invalid ❌")
            print(f"Errors found: {len(errors)}")
    
            for position, nucleotide in errors:
                print(f"Position {position}: {nucleotide}")
    
            print()
            continue

        protein = translate_dna(sequence)
        if not protein:
            print("-" * 50)
            print(f"Sequence: {sequence_name}")
            print("Status: Valid ✅")
            print()
            print("Protein:")
            print("No amino acids were translated.")
            print()
            continue
        ionizable_counts = count_ionizable_amino_acids(protein)
        isoeletric_point = estimate_isoelectric_point(ionizable_counts)
        print_protein_report(sequence_name, 
                            protein,
                            ionizable_counts,
                            isoeletric_point )

if __name__ == "__main__":
    main()  