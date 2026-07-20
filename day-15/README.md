# Day 15 - DNA Profile Matrix and Consensus Sequence

# Overview

This project reads aligned DNA sequences from a FASTA file and builds a DNA profile matrix, which stores the number of occurrences of each nucleotide (A, C, G, and T) at every sequence position.

Using this profile matrix, the program generates a consensus sequence and identifies conserved and variable positions across the alignment.

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Build a DNA profile matrix
* Generate the consensus sequence
* Identify conserved positions
* Identify variable positions
* Display a complete profile report
* 
# Example Input

>seq1
ATGCGTACGA

>seq2
ATGCGTTCGA

>seq3
ATGCGTACGG

>seq4
ATGCGTACGA

>seq5
ATGCGTACGA

>seq6
ATGCGTACGA

# Example Output

Consensus sequence:
ATGCGTACGA

Profile Matrix

      1 2 3 4 5 6 7 8 9 10
A:    6 0 0 0 0 0 5 0 0 5
C:    0 0 0 6 0 0 0 6 0 0
G:    0 0 6 0 6 0 0 0 6 1
T:    0 6 0 0 0 6 1 0 0 0

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

# Project Structure

read_fasta()
        │
        ▼
build_profile_matrix()
        │
        ▼
build_consensus()
        │
        ▼
analyze_profile_positions()
        │
        ▼
print_profile_report()

# Concepts Learned

* DNA multiple sequence alignment
* Profile matrix construction
* Consensus sequence generation
* Conserved position detection
* Variable position analysis
* Frequency counting using dictionaries
* Separation of responsibilities between functions

# Python Concepts Practiced

* Functions
* Dictionaries
* Lists
* Loops
* Nested loops
* Dictionary methods (.get())
* Returning multiple values
* Code modularization
* FASTA file parsing
* Technologies
* Python 3
* pathlib
* FASTA format
* 
# What I Learned

In this project, I learned how profile matrices are used in bioinformatics to summarize multiple aligned DNA sequences. Instead of repeatedly counting nucleotides, I generated a reusable profile matrix that allowed me to build the consensus sequence and analyze conserved and variable positions efficiently. This project also reinforced the importance of modular code design, where each function performs a single, well-defined task.