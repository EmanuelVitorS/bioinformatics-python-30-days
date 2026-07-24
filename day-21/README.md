# Day 21 - Codon Usage Analysis

# Overview

Codons are groups of three nucleotides that specify amino acids during protein synthesis. Although multiple codons can encode the same amino acid, organisms often show preferences for particular codons, a phenomenon known as **codon usage bias**. Codon usage analysis is widely used in bioinformatics, molecular evolution, comparative genomics, and gene expression optimization.

This project reads DNA sequences from a FASTA file, validates the nucleotide composition, counts the occurrence of each codon, identifies the corresponding amino acid using the genetic code, and generates a codon usage report for each sequence.

---

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Count the occurrence of each codon
* Identify the amino acid encoded by each codon
* Generate a codon usage report
* Analyze multiple DNA sequences

---

# Example Input

fasta
>seq1
ATGGCTGCTGCTTTTAAA

---

# Example Output

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Codon: ATG
Amino Acid: M
Count: 1

Codon: GCT
Amino Acid: A
Count: 3

Codon: TTT
Amino Acid: F
Count: 1

Codon: AAA
Amino Acid: K
Count: 1

---

# Project Structure

day-21/
│
├── codon_usage.py
├── genetic_code.py
├── test_sequences.fasta
└── README.md

---

# Concepts Learned

* Genetic code
* Codons
* Protein synthesis
* Codon usage bias
* DNA sequence analysis
* FASTA processing

---

# Python Concepts Practiced

* Dictionaries
* Dictionary lookups
* Counting occurrences
* Loops
* Conditional statements
* Functions
* File handling
* Modular programming
* Python 3
* FASTA format

---

# What I Learned

During this project I learned how codons determine amino acids during protein synthesis and how codon usage can be analyzed computationally. I reinforced my understanding of dictionaries by implementing a codon counting algorithm and integrated the genetic code into a complete sequence analysis workflow.

---

# Future Improvements

* Calculate codon frequencies (%)
* Sort codons by frequency
* Display complete amino acid names
* Compare codon usage between sequences
* Export reports to CSV
* Generate codon usage charts