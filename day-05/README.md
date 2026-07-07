Day 05 - DNA Reverse Complement

Description:

This project reads DNA sequences from a FASTA file, validates each sequence, generates the complementary DNA sequence, reverses the sequence, and computes the reverse complement.

Invalid sequences are detected and reported with the position of each invalid nucleotide.

Features:

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Detect invalid nucleotide characters
* Generate the complementary DNA sequence
* Reverse DNA sequences
* Generate the reverse complement
* Report invalid nucleotide positions

Example Input:

>seq1
ATGCGTAC

>seq2
ATGCXTAC

Example Output:

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Original:
ATGCGTAC

Complement:
TACGCATG

Reverse:
CATGCGTA

Reverse Complement:
GTACGCAT
--------------------------------------------------
Sequence: seq2
Status: Invalid ❌

Errors Found: 1
Position 5: X


Concepts Learned:

* FASTA parsing
* DNA validation
* Dictionaries
* String slicing (`[::-1]`)
* Reverse complement algorithm
* Function reuse
* Error handling