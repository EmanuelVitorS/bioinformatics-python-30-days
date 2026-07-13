# Day 07 - Open Reading Frame (ORF) Finder

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and identifies Open Reading Frames (ORFs).

An ORF starts with the start codon (ATG) and ends with one of the stop codons (TAA, TAG, or TGA). The program reports the start position, end position, and DNA sequence of each ORF found.

If a sequence contains invalid nucleotide characters, the program reports the number of errors and the position of each invalid character instead of searching for ORFs.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Identify Open Reading Frames (ORFs)
* Detect start and stop codons
* Report ORF start and end positions
* Extract ORF DNA sequences
* Process multiple DNA sequences

Example Input:

>seq1
ATGAAACCCTAA

>seq2
ATGCCCGGGTAAATGTTTTAG

>seq3
ATGXAAACCCTAA

Example Output:

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

ORFs:
ORF 1
Position 1-12: ATGAAACCCTAA

--------------------------------------------------
Sequence: seq2
Status: Valid ✅

ORFs:
ORF 1
Position 1-12: ATGCCCGGGTAA

ORF 2
Position 13-21: ATGTTTTAG

--------------------------------------------------
Sequence: seq3
Status: Invalid ❌
Errors Found: 1
Position 4: X

Concepts Learned:

* Open Reading Frames (ORFs)
* Reading frames
* Start codons
* Stop codons
* ORF identification

Concepts Practiced:

* Functions
* Loops
* Nested loops
* Conditional statements
* Dictionaries
* Lists
* Tuples
* FASTA parsing
* File handling
* DNA validation
* String slicing
* enumerate

Used Technologies:

* Python 3
* pathlib