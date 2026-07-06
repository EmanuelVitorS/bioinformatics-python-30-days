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

def transcribe_dna(sequence): 
    """Transcribe a DNA sequence into RNA.""" 
    return sequence.replace("T", "U") 

def main(): 
    file_path = Path(r"E:\bioinformatics-python-30-days\teste_100.fasta.txt") 
    sequences = read_fasta(file_path) 
    for name, sequence in sequences.items(): 
        errors = find_errors(sequence) 
        if not errors:
            print("-" * 50)
            print(f"Sequence: {name}")
            print("Status: Valid ✅")
            print()
            print("DNA:")
            print(sequence)
            print()
            print("RNA:")
            print(transcribe_dna(sequence))

        else:
            print("-" * 50)
            print(f"Sequence: {name}")
            print("Status: Invalid ❌")
            print()
            print(f"Errors Found: {len(errors)}")

        for position, nucleotide in errors:
            print(f"Position {position}: {nucleotide}")

if __name__ == "__main__":
    main()
