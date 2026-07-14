# Day 03 - DNA Sequence Validator

Description:

This project reads DNA sequences from a FASTA file and validates whether they contain only valid DNA nucleotides (A, T, G, and C).

If invalid characters are found, the program reports:

* The sequence name
* Validation status
* Number of errors
* Position of each invalid character

Features:

* Read FASTA files
* Validate DNA sequences
* Detect invalid nucleotides
* Report error positions
* Process multiple DNA sequences

Input (FASTA):

>seq1
ATGCGTACGTXAGCTAGCTAGC

>seq2
ATGCGATCGATCGATCGATCG

Output:

Sequence: seq1
Status: Invalid ❌
Errors Found: 1
Position 11: X

Sequence: seq2
Status: Valid ✅

Concepts Learned:

* Input validation
* Error detection
* Error handling
* enumerate
* Lists
* Tuples

Concepts Practiced:

* Dictionaries
* Loops
* Functions
* File handling
* FASTA parsing
* String methods
* enumerate()
* pathlib

Used Technologies:

* Python 3
* pathlib