# Day 22 - Amino Acid Composition Analysis

# Overview

This project translates DNA sequences into proteins and performs an amino acid composition analysis. It validates DNA sequences, counts the occurrence of each amino acid in the translated protein, calculates their relative frequencies, and generates a detailed report for each sequence.

---

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Translate DNA into protein sequences
* Count amino acid occurrences
* Calculate amino acid frequencies
* Generate an amino acid composition report

---

# Project Structure

day-22/
├── amino_acid_composition.py
├── genetic_code.py
├── test_sequences.fasta
└── README.md

---

# Example Output

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Protein:
MAAFKG

Amino Acid: M
Count: 1
Frequency: 16.67%

Amino Acid: A
Count: 2
Frequency: 33.33%

Amino Acid: F
Count: 1
Frequency: 16.67%

Amino Acid: K
Count: 1
Frequency: 16.67%

Amino Acid: G
Count: 1
Frequency: 16.67%

---

# Skills Practiced

* FASTA file parsing
* DNA sequence validation
* DNA to protein translation
* Dictionary manipulation
* Frequency calculation
* Report generation
* Modular programming

---

# What I Learned

* How to count amino acid occurrences using Python dictionaries
* How to calculate frequency percentages from biological data
* How to organize bioinformatics workflows into reusable functions
* How to generate structured reports for protein sequence analysis

---

# Next Steps

In the next project, the analysis will move beyond amino acid composition toward more advanced protein sequence analysis and bioinformatics techniques.