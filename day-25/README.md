# Day 25 - Amino Acid Class Composition Analysis

# Overview

This project analyzes the biochemical composition of proteins translated from DNA sequences. It classifies amino acids into biochemical groups (Hydrophobic, Polar, Positive, and Negative), counts their occurrences, calculates their relative percentages, and generates a detailed composition report for each valid sequence in a FASTA file.

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Translate DNA into protein sequences
* Classify amino acids into biochemical classes
* Count amino acids in each class
* Calculate the percentage of each amino acid class
* Generate a formatted protein composition report

# Project Structure

day-25/
│── sequence_analyzer.py
│── genetic_code.py
│── amino_acid_classes.py
│── test_sequences.fasta
└── README.md

# Example Output

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Protein:
MAVKDEFL

Length: 8 aa

Amino Acid Class Composition:
Hydrophobic: 4 (50.00%)
Polar: 1 (12.50%)
Positive: 1 (12.50%)
Negative: 2 (25.00%)

# Skills Practiced

* Dictionary comprehensions
* Nested loops
* Working with dictionaries of sets
* Membership testing using `in`
* Counting categorized data
* Percentage calculations
* Function modularization
* FASTA file processing
* Protein sequence analysis

# What I Learned

* How to classify amino acids into biochemical groups
* How to work with dictionaries whose values are sets
* How to count categorized biological data
* How to calculate and display class percentages
* How to organize a bioinformatics workflow into reusable functions

# Next Steps

In the next project, I will continue expanding my bioinformatics toolkit by implementing another protein sequence analysis feature.