Day 04 - DNA to RNA Transcription

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and transcribes valid DNA sequences into RNA.

If a sequence contains invalid nucleotide characters, the program reports the number of errors and the position of each invalid character instead of performing the transcription.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Report invalid nucleotide positions
* Transcribe DNA into RNA

Example Input:

>seq1
ATGCGTACGTTAGC

>seq2
ATGCGTXCGTTAGC

Example Output:

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

* FASTA parsing
* String manipulation
* DNA validation
* DNA to RNA transcription
* Error detection
* Functions
* Loops
* Dictionaries