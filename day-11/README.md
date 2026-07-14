# Day 11 - DNA Sequence Comparison with Modular Report Functions

Description:

This project is a refactored version of the previous DNA sequence comparison program. It reads DNA sequences from a FASTA file, validates each sequence, compares reference and sample sequences, identifies mutations, and calculates sequence identity.

The main improvement in this version is the code organization. Instead of handling all output inside the "main()" function, the program now uses dedicated report functions for valid comparisons, invalid sequences, and sequences with different lengths, making the code cleaner, easier to read, and more maintainable.

The program compares DNA sequences in pairs. It validates nucleotide characters, detects mutations, reports invalid nucleotides, and calculates the percentage of identical bases between two valid sequences.

If a sequence contains invalid nucleotide characters or if the sequences have different lengths, the program generates the appropriate report instead of performing the comparison.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Compare DNA sequences in pairs
* Detect nucleotide mutations
* Report mutation positions
* Display nucleotide substitutions (reference → sample)
* Calculate sequence identity percentage
* Detect sequences with different lengths
* Generate separate reports for valid, invalid, and incompatible sequence pairs
* Improved code organization through modular functions

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

Total mutations: 1

Base 7: A -> T

Identity: 93.75%

--------------------------------------------------
Comparing: seq3 and seq4

Status: Invalid ❌

Reference: seq3
Sequence: ATGCGTXCGTAGCTAG

Position 7: X

Sample: seq4
Sequence: ATGCGTACGTAGCTAG


Concepts Learned:

* Code refactoring
* Function decomposition
* Separation of concerns
* Modular program design
* DNA sequence comparison
* Mutation identification
* Sequence validation
* Sequence identity calculation

Concepts Practiced:

* Functions
* Modular programming
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
