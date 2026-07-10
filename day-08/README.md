Day 08 - DNA Melting Temperature (Tm) Calculator

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and calculates the DNA melting temperature (Tm) using the Wallace rule.

The program also reports the sequence length, nucleotide counts, and GC content for each valid DNA sequence.

If a sequence contains invalid nucleotide characters, the program reports the number of errors and the position of each invalid character instead of calculating the melting temperature.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Count nucleotide frequencies
* Calculate sequence length
* Calculate GC content percentage
* Calculate DNA melting temperature (Tm)
* Process multiple DNA sequences

Example Input:

>seq1
ATGCGTACGTAG

>seq2
ATGCXTACGTAG

Example Output:

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Length: 12 bp

Base Counts:
  A: 3
  T: 3
  G: 3
  C: 3

GC Content: 50.00%
Tm: 36 °C

--------------------------------------------------
Sequence: seq2
Status: Invalid ❌

Errors Found: 1
Position 5: X

Concepts Learned:

* DNA melting temperature (Tm)
* Wallace rule
* Formula-based sequence analysis

Concepts Practiced:

* Functions
* Dictionaries
* Dictionary access
* Loops
* File handling
* FASTA parsing
* DNA validation
* String methods
* Mathematical expressions
* Error detection
* Error handling

Used Technologies:

* Python 3
* pathlib
