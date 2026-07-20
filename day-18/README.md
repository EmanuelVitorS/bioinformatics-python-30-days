# Day 18 - DNA Translation in Reading Frames

# Overview

This project reads DNA sequences from a FASTA file and translates each sequence into protein sequences using the three forward reading frames. Each DNA sequence is validated before translation, and the resulting proteins are displayed along with their corresponding reading frame.

This project demonstrates how different reading frames can produce different protein sequences from the same DNA sequence.

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Translate DNA into proteins using the genetic code
* Analyze the three forward reading frames
* Display protein sequences for each frame
* Report protein length
* Handle invalid DNA sequences

# Example Input

FASTA file

>seq1
ATGGTTGAACTG

>seq2
ATGCGATAGCTG

>seq3
ATGCXTAG
# Example Output
--------------------------------------------------
Sequence: seq1
Status: Valid ✅

DNA:
ATGGTTGAACTG

Frame 1:
Length: 4 amino acids
MVEL

Frame 2:
Length: 3 amino acids
WLN

Frame 3:
Length: 2 amino acids
G*

--------------------------------------------------
Sequence: seq3
Status: Invalid ❌
Errors found: 1

Position 5: X

Note: Depending on the implementation of translate_dna(), translation may stop at the first stop codon.

# Project Structure

read_fasta()
        │
        ▼
find_errors()
        │
        ▼
translate_dna()
        │
        ▼
translate_reading_frames()
        │
        ▼
print_translation_report()
        │
        ▼
main()

# Concepts Learned

* DNA translation
* Reading frames
* Genetic code
* Codon interpretation
* Protein sequence generation
* DNA validation
* Modular programming
* Function reuse

# Python Concepts Practiced

* Functions
* Dictionaries
* Loops
* String slicing
* Imports
* Returning dictionaries
* Nested function calls
* Code modularization
* Technologies
* Python 3
* pathlib
* FASTA format
* Genetic code dictionary

# What I Learned

In this project, I learned how different reading frames can produce different protein sequences from the same DNA molecule. I also reinforced the concept of translating DNA into proteins using the genetic code while practicing function reuse and modular programming. This project showed how a single translation function can be applied to multiple reading frames, reducing duplicated code and improving maintainability.

# Future Improvements

Translate the six reading frames (three forward and three reverse)
Continue translation after stop codons
Highlight stop codons in the protein sequence
Detect the longest protein among all frames
Export protein sequences to a FASTA file