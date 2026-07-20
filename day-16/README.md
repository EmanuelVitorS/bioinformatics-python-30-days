# Day 16 - DNA Motif Search
# Overview

This project searches for specific DNA motifs within one or more sequences stored in a FASTA file.

The program validates each DNA sequence, searches for all occurrences of a user-defined motif, and reports the positions where the motif is found.

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Validate user-input motif
* Search for DNA motifs
* Detect multiple motif occurrences
* Support overlapping motif matches
* Generate a report for each sequence
* Example Input

FASTA file

>seq1
ATGCGTATGCGATG

>seq2
ATGCCCATGTTTATG

>seq3
ATGCXTAG

Motif

ATG
# Example Output
--------------------------------------------------
Sequence: seq1

Motif: ATG

Matches found: 3

Positions:
1
7
12

--------------------------------------------------
Sequence: seq2

Motif: ATG

Matches found: 3

Positions:
1
7
13

--------------------------------------------------
Sequence: seq3

Status: Invalid ❌
Errors found: 1

Position 5: X

# Project Structure
read_fasta()
        │
        ▼
find_errors()
        │
        ▼
find_motif()
        │
        ▼
print_motif_report()
        │
        ▼
main()

# Concepts Learned
* DNA motif searching
* Pattern matching in DNA sequences
* Substring comparison
* Motif position detection
* DNA sequence validation
* User input validation
* Handling multiple DNA sequences

# Python Concepts Practiced
* Functions
* Loops
* Conditional statements
* String slicing
* Lists
* Dictionaries
* Enumerate
* Returning lists
* Code modularization
* Technologies
* Python 3
* pathlib
* FASTA format

# What I Learned

In this project, I learned how motif searching is performed by scanning DNA sequences and comparing substrings to a target pattern. I also improved the program by validating both DNA sequences and user-provided motifs before analysis. This project reinforced the importance of modular programming, where each function is responsible for a single task, making the code easier to maintain and extend.