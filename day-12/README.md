# Day 12 - DNA Consensus Sequence Generator

Description:

This project reads multiple DNA sequences from a FASTA file and generates a consensus DNA sequence by selecting the most frequent nucleotide at each position.

The program parses DNA sequences from a FASTA file, analyzes each nucleotide position across all sequences, counts the occurrence of each nucleotide using a dictionary, and builds the consensus sequence one nucleotide at a time.

The implementation is divided into small, reusable functions. One function builds the consensus sequence, while another determines the most frequent nucleotide for each position. This modular approach makes the code easier to understand, maintain, and reuse.

At the end of the analysis, the program displays the consensus sequence, the total number of sequences analyzed, and the sequence length.

Features:

* Read multiple DNA sequences from a FASTA file
* Build a DNA consensus sequence
* Count nucleotide frequencies using dictionaries
* Determine the most frequent nucleotide at each position
* Display the consensus sequence
* Report the total number of sequences analyzed
* Report sequence length
* Modular program design using reusable functions

Example Input:

>seq1
ATGCGTACGA

>seq2
ATGCGTTCGA

>seq3
ATGCGTACGA

>seq4
ATGCGTACGG

>seq5
ATGCGTACGA

>seq6
ATGCGTACGA

Example Output:

Consensus sequence:
ATGCGTACGA

Number of sequences: 6
Sequence length: 10 bp

Concepts Learned:

* Consensus sequence generation
* Function decomposition
* Modular program design

Concepts Practiced:

* Nucleotide frequency analysis
* Counting occurrences with dictionaries
* Functions
* Dictionaries
* Loops
* Nested loops
* Conditional statements
* String manipulation
* FASTA parsing
* File handling
* Lists
* pathlib

Used Technologies:

* Python 3
* pathlib