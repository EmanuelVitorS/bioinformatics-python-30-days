# Day 13 - DNA Consensus Sequence and Variable Position Analysis

# Overview

This project reads multiple DNA sequences from a FASTA file and generates a **consensus sequence** by selecting the most frequent nucleotide at each position. In addition, it identifies **conserved positions**, detects **variable positions**, and reports the nucleotide distribution for every variable site.

The program is designed for multiple sequence analysis and demonstrates how consensus sequences can summarize genetic information from a group of DNA sequences.

---

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Build a DNA consensus sequence
* Count nucleotide frequencies at every position
* Identify conserved positions
* Identify variable positions
* Display nucleotide counts for each variable position
* Generate a formatted consensus report
* Modular program structure using reusable functions

---

Example Input:

fasta
>seq1
ATGCGTACGA

>seq2
ATGCGTTCGA

>seq3
ATGCGTACGA

>seq4
ATGCGTACGG

>seq5
ATGCGTACGA

>seq6
ATGCGCACGA


Example Output:

Consensus sequence:
ATGCGTACGA

Number of sequences: 6
Sequence length: 10

--------------------------------------------------
Conserved Positions

[1, 2, 3, 4, 5, 6, 8, 9]

--------------------------------------------------
Variable Positions

Position 7
A: 5
T: 1

Position 10
A: 5
G: 1

---

Project Structure:

read_fasta()
│
├── Reads sequences from a FASTA file
│
find_errors()
│
├── Detects invalid nucleotide characters
│
count_bases()
│
├── Counts nucleotide frequencies
│
most_frequent_base()
│
├── Finds the most frequent nucleotide
│
build_consensus()
│
├── Builds the consensus sequence
├── Identifies conserved positions
└── Collects nucleotide counts for variable positions
│
print_consensus_report()
│
└── Displays the final analysis report
│
main()
└── Coordinates the complete workflow


---

Concepts Learned:

* Consensus sequence generation
* Multiple sequence comparison
* Conserved and variable site analysis
* Dictionary-based frequency counting
* Function decomposition
* Modular program organization
* Returning multiple values from functions

---

Python Concepts Practiced:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Nested loops
* Function reuse
* Multiple return values
* FASTA parsing
* File handling
* String manipulation
* enumerate()
* pathlib

---

Technologies:

* Python 3
* pathlib

---

# Future Improvements

* Validate that all sequences have the same length
* Ignore or handle ambiguous nucleotides (N)
* Export reports to a text file
* Support FASTA files containing hundreds or thousands of sequences
* Handle ties between equally frequent nucleotides
* Calculate nucleotide frequencies as percentages
