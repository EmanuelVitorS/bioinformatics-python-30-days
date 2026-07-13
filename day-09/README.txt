Day 09 - DNA Mutation Detection
Description:

This project reads DNA sequences from a FASTA file, validates each sequence, and compares DNA sequence pairs to identify nucleotide mutations.

For each valid pair of sequences, the program reports every nucleotide difference, including its position, the reference nucleotide, and the sample nucleotide.

If invalid nucleotide characters are detected, the program reports the errors instead of performing the comparison.

Features:
* Read DNA sequences from a FASTA file
* Process DNA sequences in pairs
* Validate DNA sequences
* Detect invalid nucleotide characters
* Compare two DNA sequences
* Identify nucleotide mutations
* Report mutation positions
* Display reference and sample nucleotides
* Report invalid nucleotide positions

Example Input:
>Reference
ATGCGTACGTAG

>Sample
ATGCGTTCGTAG
Example Output
--------------------------------------------------
Status: Valid ✅

Comparing:
Reference: Reference
Sample: Sample

Mutations:
Position 7: A -> T
Example (Invalid Sequence)
>Reference
ATGCGTXCGTAG

>Sample
ATGCGTACGTAG

Output:

--------------------------------------------------
Status: Invalid ❌

Errors Found: 1
Position 7: X

Concepts Learned:
*Sequence comparison
*Mutation detection
*Pairwise analysis
*zip()
*Concepts Practiced
*Functions
*Loops
*Dictionaries
*Lists
*Tuples
*enumerate()
*zip()
*File handling
*FASTA parsing
*DNA validation
*Input validation
*Error detection
*Error handling
*String comparison

Concepts Practiced:
*

Used Technologies:
* Python 3
* pathlib