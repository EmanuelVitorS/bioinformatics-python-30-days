# Day 10 - DNA Sequence Comparison and Mutation Analysis

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, compares reference and sample sequences, identifies mutations, and calculates sequence identity.

The program compares DNA sequences in pairs. It checks for invalid nucleotide characters, detects differences between sequences, reports mutation positions and nucleotide changes, and calculates the percentage of identical bases between the reference and sample sequences.

If a sequence contains invalid nucleotide characters or if the sequences have different lengths, the program reports that the comparison cannot be performed.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Compare reference and sample sequences
* Detect nucleotide mutations
* Report mutation positions
* Show nucleotide changes (reference → sample)
* Calculate sequence identity percentage
* Process multiple sequence comparisons

Example Input:

>seq1
ATGCGTACGTAGCTAG

>seq2
ATGCGTTCGTAGCTAG

>seq3
ATGCGTXCGTAGCTAG

>seq4
ATGCGTACGTAGCTAG


Example Output:

--------------------------------------------------
Status: Valid ✅

Length: 16 bp

Comparing:

Reference: seq1
Sequence: ATGCGTACGTAGCTAG

Sample: seq2
Sequence: ATGCGTTCGTAGCTAG

Mutations: 1

Base 7: A -> T

Identity: 93.75%


--------------------------------------------------
Status: Invalid ❌

Comparing: seq3 and seq4

Reference: seq3
Sequence: ATGCGTXCGTAGCTAG

Position 7: X


Concepts Learned:

* DNA sequence comparison
* Sequence identity calculation
* Mutation identification
* Reference and sample sequences
* Nucleotide differences
* Sequence validation


Concepts Practiced:

* Functions
* Loops
* Conditional statements
* Dictionaries
* Lists
* Tuples
* FASTA parsing
* File handling
* String manipulation
* enumerate()
* zip()
* pathlib


Used Technologies:

* Python 3
* pathlib