# Day 28 - Smith-Waterman Local Sequence Alignment

# Overview

This project implements the Smith-Waterman algorithm for local DNA sequence alignment.

Unlike global alignment, which aligns complete sequences, the Smith-Waterman algorithm identifies the highest-scoring local region shared between two DNA sequences using dynamic programming.

The program reads two DNA sequences from a FASTA file, validates the sequences, constructs a scoring matrix, performs local traceback to reconstruct the optimal alignment, calculates alignment statistics, and generates a detailed alignment report.

---

# Features

* Read DNA sequences from FASTA files
* Validate DNA sequences
* Build a local alignment score matrix
* Perform Smith* Waterman local alignment
* Identify the highest* scoring local region
* Reconstruct the optimal local alignment
* Calculate alignment identity
* Count matches, mismatches, and gaps
* Generate a complete alignment report

---

# Project Structure

day-28/
│── local_alignment.py
│── test.fasta
│── README.md

---

# Scoring System

| Event | Score |
|-------|------:|
| Match | +2 |
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
Fill score matrix
        ↓
Find highest score
        ↓
Perform local traceback
        ↓
Generate local alignment
        ↓
Calculate statistics
        ↓
Generate report

---

# Example Output

------------------------------------------------------------
Smith-Waterman Local Alignment
------------------------------------------------------------

Sequence 1: sequence_1
Sequence 2: sequence_2

Best local alignment:

GTTAG
|||||
GTTAG

Alignment positions:

sequence_1: 3-7
sequence_2: 2-6

Alignment statistics:

Alignment length: 5
Matches: 5
Mismatches: 0
Gaps: 0
Identity: 100.00%
Highest local alignment score: 10

Scoring system:

Match: 2
Mismatch: -1
Gap: -2

---

# Skills Practiced

* Dynamic programming
* Matrix manipulation
* Nested loops
* Conditional statements
* Functions
* FASTA file processing
* DNA sequence validation
* Local sequence alignment
* Traceback algorithms
* Alignment statistics
* Identity calculation

---

# What I Learned

* How the Smith*Waterman algorithm performs local sequence alignment
* The difference between local and global sequence alignment
* How dynamic programming is used to identify highly similar sequence regions
* How to reconstruct the optimal local alignment using traceback
* How scoring systems influence local alignments
* How to calculate alignment identity and statistics

---

# Biological Applications

Smith-Waterman is widely used in bioinformatics for:

* Local DNA sequence comparison
* Protein sequence comparison
* Homology detection
* Conserved region identification
* Functional domain analysis
* Similarity searches
* Comparative genomics

---

# Comparison with Needleman-Wunsch

| Needleman-Wunsch | Smith-Waterman |
|------------------|----------------|
| Global alignment | Local alignment |
| Aligns complete sequences | Aligns only the best matching region |
| Traceback starts from the bottom-right corner | Traceback starts from the highest score |
| Matrix values may be negative | Matrix values are never negative |
| Traceback ends at (0,0) | Traceback ends when a score of 0 is reached |

---

# Next Steps

In the next project, I will continue exploring advanced sequence comparison techniques by implementing multiple sequence alignment and phylogenetic analysis methods.