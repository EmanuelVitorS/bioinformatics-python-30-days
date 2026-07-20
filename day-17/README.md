# Day 17 - K-mer Frequency Analysis

# Overview

This project reads DNA sequences from a FASTA file and performs k-mer frequency analysis. A k-mer is a DNA fragment of length k, commonly used in genome assembly, sequence comparison, and many bioinformatics algorithms.

The program validates each DNA sequence, generates all possible k-mers using a sliding window approach, counts their frequencies, and displays the results for each sequence.

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Accept a user-defined k value
* Generate all possible k-mers
* Count k-mer frequencies
* Display a frequency report for each sequence
* Handle invalid sequences
* Validate the k value

# Example Input

FASTA file

>seq1
ATGATGCGATG

>seq2
ATGCGATGCG

>seq3
ATGCXTAG

k value

3
# Example Output
--------------------------------------------------
Sequence: seq1
Status: Valid ✅

k = 3

Unique k-mers: 6

K-mer Frequencies

ATG: 3
TGA: 2
GAT: 2
TGC: 1
GCG: 1
CGA: 1

--------------------------------------------------
Sequence: seq2
Status: Valid ✅

k = 3

Unique k-mers: 5

K-mer Frequencies

ATG: 2
TGC: 2
GCG: 2
CGA: 1
GAT: 1

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
count_kmers()
        │
        ▼
print_kmer_report()
        │
        ▼
main()

# Concepts Learned

* K-mer generation
* Sliding window algorithm
* Frequency counting
* DNA sequence validation
* Dictionary-based counting
* Sequence statistics
* Modular program design

# Python Concepts Practiced

* Functions
* Dictionaries
* Loops
* String slicing
* Conditional statements
* User input validation
* Returning dictionaries
* Code modularization
* Technologies
* Python 3
* pathlib
* FASTA format

# What I Learned

In this project, I learned how to generate and count DNA k-mers using a sliding window algorithm. I practiced using dictionaries to store frequency data efficiently and reinforced the importance of validating both user input and DNA sequences before analysis. This project also demonstrated how modular programming improves code organization, readability, and reusability.

# Future Improvements

Sort k-mers by frequency
Display the most frequent k-mer(s)
Export results to a CSV file
Support RNA sequences
Ignore ambiguous nucleotides (N)