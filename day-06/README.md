Day 06 - DNA to Protein Translation

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and translates valid DNA sequences into protein sequences using the standard genetic code.

Invalid sequences are detected and reported with the position of each invalid nucleotide. Translation stops at stop codons and ignores incomplete codons.

The program:

* Reads one or more DNA sequences from a FASTA file.
* Validates each sequence.
* Translates DNA into protein.
* Stops translation when a stop codon is found.
* Ignores incomplete codons at the end of the sequence.

Features:

* Read FASTA files
* DNA sequence validation
* Translation using the standard genetic code
* Recognition of stop codons ("TAA", "TAG", "TGA")
* Ignores incomplete codons
* Supports multiple sequences in a single FASTA file

Example:

Input (FASTA)

>seq1
ATGGTTGAATTT

>seq2
ATGGTTGAATAACCC

Output:

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Protein:
MVEF

--------------------------------------------------
Sequence: seq2
Status: Valid ✅

Protein:
MVE

Concepts Learned:

* Genetic code
* Reading frame
* DNA to protein translation
* Protein sequence generation

Concepts Practiced:

* Dictionaries
* Dictionary lookup
* Functions
* Loops
* String slicing
* FASTA file parsing
* DNA validation
* Codon processing
* Stop codon recognition

Used Technologies:

* Python 3
* pathlib