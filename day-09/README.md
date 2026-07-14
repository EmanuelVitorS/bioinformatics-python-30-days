# Day 09 - DNA Mutation Detection

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, compares reference and sample sequences, and identifies nucleotide mutations.

The program processes DNA sequences in pairs, considering the first sequence as the reference and the second sequence as the sample. It checks for invalid nucleotide characters and compares each position to detect differences between the sequences.

If sequences contain invalid nucleotide characters or have different lengths, the program reports that the comparison cannot be performed.

Features:

* Read DNA sequences from a FASTA file
* Store sequences using dictionaries
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Compare reference and sample sequences
* Identify nucleotide mutations
* Report mutation positions
* Show nucleotide changes (reference → sample)
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

Comparing:

Reference: seq1

Sample: seq2

Base 7: A -> T


--------------------------------------------------
Comparing: seq3 and seq4

Status: Invalid ❌

Reference:

Position 7: X

Sample:

No errors found.


Concepts Learned:

* DNA mutation detection
* Reference and sample sequences
* Nucleotide comparison
* Sequence validation
* FASTA file structure
* zip()


Concepts Practiced:

* Functions
* Loops
* Conditional statements
* Dictionaries
* Lists
* Tuples
* FASTA parsing
* File handling
* String comparison
* enumerate()
* pathlib

Used Technologies:

* Python 3
* pathlib