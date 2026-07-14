# Day 04 - DNA to RNA Transcription

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and transcribes valid DNA sequences into RNA.

If a sequence contains invalid nucleotide characters, the program reports the number of errors and the position of each invalid character instead of performing the transcription.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Transcribe DNA into RNA
* Process multiple DNA sequences

Input (FASTA):

>seq1
ATGCGTACGTTAGC

>seq2
ATGCGTXCGTTAGC

Output:

Sequence: seq1
Status: Valid ✅

DNA:
ATGCGTACGTTAGC

RNA:
AUGCGUACGUUAGC
--------------------------------------------------

Sequence: seq2
Status: Invalid ❌
Errors Found: 1
Position 7: X
--------------------------------------------------

Concepts Learned:

* String manipulation
* DNA validation
* DNA to RNA transcription

Concepts Practiced:

* Dictionaries
* Loops
* Functions
* FASTA parsing
* String methods
* enumerate
* Lists
* Tuples
* Input validation
* Error detection
* Error handling
* enumerate()
* pathlib

Used Technologies:

* Python 3
* pathlib