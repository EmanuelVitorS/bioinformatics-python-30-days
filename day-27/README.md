# Day 27 - Needleman-Wunsch Global Sequence Alignment

# Overview

This project implements the Needleman-Wunsch algorithm for global DNA sequence alignment.

The program reads two DNA sequences from a FASTA file, validates the nucleotide sequences, constructs a scoring matrix, performs traceback to obtain the optimal global alignment, calculates alignment statistics, and generates a detailed alignment report.

---

# Features

* Read DNA sequences from FASTA files
* Validate DNA sequences
* Build a scoring matrix
* Perform global sequence alignment
* Trace back the optimal alignment path
* Calculate alignment identity
* Count matches, mismatches, and gaps
* Generate a complete alignment report

---

# Project Structure

day-27/
│── sequence_alignment.py
│── test.fasta
│── README.md

---

# Scoring System

| Event | Score |
|-------|------:|
| Match | +1 |
| Mismatch | -1 |
| Gap | -2 |

---

# Algorithm Workflow

Read FASTA
        ↓
Validate DNA sequences
        ↓
Create score matrix
        ↓
Initialize first row and column
        ↓
Fill score matrix
        ↓
Traceback
        ↓
Generate optimal alignment
        ↓
Calculate statistics
        ↓
Generate report

---

# Example Output

------------------------------------------------------------
Needleman-Wunsch Global Alignment
------------------------------------------------------------

Sequence 1: sequence_1
Sequence 2: sequence_2

Alignment:

GATTACA
|..|.||
GCATGCA

Alignment statistics:

Alignment length: 7
Matches: 4
Mismatches: 3
Gaps: 0
Identity: 57.14%
Final alignment score: 1

Scoring system:

Match: 1
Mismatch: -1
Gap: -2

---

# Skills Practiced

* Dynamic programming
* Matrix manipulation
* Nested loops
* Dictionaries
* Functions
* Conditional statements
* Sequence validation
* FASTA file processing
* Global sequence alignment
* Traceback algorithms
* Alignment statistics
* Identity calculation

---

# What I Learned

* How the Needleman-Wunsch algorithm performs global sequence alignment
* How dynamic programming is applied in bioinformatics
* How to construct and fill a scoring matrix
* How traceback reconstructs the optimal alignment
* How to calculate alignment identity and statistics
* How gap penalties affect sequence alignment

---

# Biological Applications

Needleman-Wunsch is widely used in bioinformatics for:

* DNA sequence comparison
* Gene similarity analysis
* Evolutionary studies
* Comparative genomics
* Sequence annotation
* Reference sequence alignment

---

# Next Steps

In the next project, I will continue exploring sequence alignment algorithms by implementing more advanced bioinformatics methods.