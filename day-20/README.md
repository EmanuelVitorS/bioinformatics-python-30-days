# Day 20 - Restriction Enzyme Analysis

# Overview

This project introduces restriction enzyme analysis, one of the most common techniques in molecular biology and DNA cloning.

It reads DNA sequences from a FASTA file, validates the nucleotide composition, identifies restriction enzyme recognition sites, and reports all positions where each enzyme can cut the DNA.

---

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Search for restriction enzyme recognition sites
* Report all matching positions for each enzyme
* Handle multiple occurrences of the same restriction site
* Support analysis of multiple DNA sequences

---

# Restriction Enzymes

| Enzyme | Recognition Sequence |
|--------|-----------------------|
| EcoRI | GAATTC |
| BamHI | GGATCC |
| HindIII | AAGCTT |

---

# Example Input

fasta
>seq1
ATGGAATTCGGATCCAAGCTTATGCGT

>seq2
ATGCGTATGCGTATGCGT

---

# Example Output

--------------------------------------------------
Sequence: seq1

EcoRI
Recognition sequence: GAATTC
Sites found: 1
Positions: 4

BamHI
Recognition sequence: GGATCC
Sites found: 1
Positions: 10

HindIII
Recognition sequence: AAGCTT
Sites found: 1
Positions: 16

---

# Project Structure

day-20/
│
├── restriction_enzyme.py
├── restriction_enzyme_analysis.py
├── test_sequences.fasta
└── README.md


---

# Concepts Learned

* Restriction enzymes
* Recognition sequences
* DNA sequence pattern matching
* Sequence validation
* Biological sequence analysis

---

# Python Concepts Practiced

* Dictionaries
* Lists
* Nested loops
* String slicing
* Conditional statements
* Functions
* File handling
* Modular programming
* Python 3
* FASTA format

---

## Technologies

* Python 3
* FASTA format

---

# What I Learned

During this project I learned how restriction enzymes recognize specific DNA sequences and why they are fundamental tools in molecular biology. I also improved my understanding of pattern matching algorithms, string slicing, dictionaries, loops, modular programming, and sequence validation while working with biological data.

---

# Future Improvements

* Support additional restriction enzymes
* Import enzyme databases automatically
* Display cut positions separately from recognition sites
* Simulate DNA digestion and fragment sizes
* Generate graphical restriction maps