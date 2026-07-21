# Day 19 - Pairwise Sequence Alignment

# Overview

In this project, I implemented a simple pairwise DNA sequence alignment tool in Python.

The program reads two DNA sequences from a FASTA file, validates both sequences, compares them nucleotide by nucleotide, and generates an alignment report including matches, mismatches, sequence identity, and alignment score.

This project introduces one of the fundamental concepts in bioinformatics: sequence alignment.

# Features

* Read DNA sequences from a FASTA file
* Validate nucleotide sequences
* Compare two DNA sequences position by position
* Generate an alignment visualization
* Count matches and mismatches
* Calculate sequence identity (%)
* Calculate alignment score

# Example Input
>human
ATGGCTAACGTTAGCCTGA

>mouse
ATGGCTAATGTCAGCCTGA

# Example Output
--------------------------------------------------
Sequence 1: human
Sequence 2: mouse

ATGGCTAACGTTAGCCTGA
||||||| ||| |||||||
ATGGCTAATGTCAGCCTGA

Matches: 17
Mismatches: 2
Identity: 89.47%
Alignment Score: 15
Project Structure
day-19/
│── pairwise_sequence_alignment.py
│── genetic_code.py
│── test_sequences.fasta
└── README.md

# Concepts Learned

* Pairwise sequence comparison
* Sequence alignment visualization
* Sequence identity calculation
* Alignment scoring
* DNA sequence validation
* Dictionary-based result storage
* Separation of data processing and reporting

# Python Concepts Practiced

* Functions
* Dictionaries
* Loops
* Conditional statements
* zip()
* String manipulation
* FASTA file parsing
* Modular programming
* Technologies
* Python 3

# What I Learned

Through this project, I learned how pairwise sequence alignment works by comparing DNA sequences nucleotide by nucleotide.

I also practiced organizing code into reusable functions, separating sequence analysis from report generation, and calculating important bioinformatics metrics such as sequence identity and alignment score.

# Future Improvements

* Support gap insertion (-)
* Implement Needleman–Wunsch global alignment
* Support local alignment (Smith–Waterman)
* Compare multiple sequence pairs automatically
* Export alignment reports to a file