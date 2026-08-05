# Day 29 - Progressive Multiple Sequence Alignment

# Overview

Multiple sequence alignment is a fundamental bioinformatics technique used to compare three or more biological sequences simultaneously. It helps identify conserved regions, mutations, sequence similarities, and possible evolutionary relationships.

This project implements a simplified progressive multiple sequence alignment strategy. The first DNA sequence in the FASTA file is used as a reference, and the remaining sequences are aligned to it using the Needleman-Wunsch global alignment algorithm. The pairwise alignments are then merged into a single multiple alignment.

---

# Features

* Read multiple DNA sequences from a FASTA file
* Validate nucleotide sequences
* Perform pairwise global alignments
* Build a simplified progressive multiple sequence alignment
* Propagate gaps across previously aligned sequences
* Generate a consensus sequence
* Calculate conservation percentages by alignment position
* Create a visual conservation line
* Calculate a pairwise identity matrix
* Display pairwise alignment scores against the reference

---

# Project Structure

day-29/
├── multiple_sequence_alignment.py
├── test.fasta
└── README.md

---

# Scoring System

| Event | Score |
|---|---:|
| Match | +1 |
| Mismatch | -1 |
| Gap | -2 |

---

# Algorithm Workflow

Read FASTA
        ↓
Validate DNA sequences
        ↓
Select the first sequence as reference
        ↓
Align each sequence to the reference
        ↓
Merge reference alignments
        ↓
Build multiple sequence alignment
        ↓
Generate consensus sequence
        ↓
Calculate conservation
        ↓
Calculate pairwise identity matrix
        ↓
Generate report

---

# Example Input

>sequence_1
ATGCGTACGTAG

>sequence_2
ATGCGTTCGTAG

>sequence_3
ATGCGACGTAG

>sequence_4
ATGCGTACGTTAG

>sequence_5
ATGAGTACGTAG

---

# Example Output

----------------------------------------------------------------------
Progressive Multiple Sequence Alignment
----------------------------------------------------------------------

Number of sequences: 5
Alignment length: 13

Multiple alignment:

sequence_1    ATGCGTACGT-AG
sequence_2    ATGCGTTCGT-AG
sequence_3    ATGCG-ACGT-AG
sequence_4    ATGCGTACGTTAG
sequence_5    ATGAGTACGT-AG
Conservation  ***.*****:***
Consensus     ATGCGTACGTTAG

Conservation symbols:
* = 100% conserved
: = at least 75% conserved
. = at least 50% conserved
  = less than 50% conserved

The exact placement of gaps can vary when multiple alignments have the same optimal score.

---

# Pairwise Identity Matrix

The program also calculates the percentage identity between every pair of aligned sequences.

Example:

Pairwise identity matrix (%):

              sequence_1  sequence_2  sequence_3
sequence_1        100.00       92.31       84.62
sequence_2         92.31      100.00       76.92
sequence_3         84.62       76.92      100.00

---

# Conservation Symbols

| Symbol | Meaning |
|:---:|---|
| `*` | 100% conserved |
| `:` | At least 75% conserved |
| `.` | At least 50% conserved |
| Blank | Less than 50% conserved |

---

# Skills Practiced

* Progressive sequence alignment
* Needleman*Wunsch global alignment
* Dynamic programming
* Matrix manipulation
* Nested loops
* Lists and dictionaries
* Gap propagation
* Consensus sequence generation
* Conservation analysis
* Pairwise identity calculation
* FASTA file processing
* Input validation
* Modular programming

---

# What I Learned

* How multiple DNA sequences can be aligned progressively
* How pairwise alignments can be merged into a multiple alignment
* How gaps added to a reference sequence must be propagated to previously aligned sequences
* How to generate a consensus sequence from alignment columns
* How to calculate conservation percentages
* How to construct and display a pairwise identity matrix
* How global alignment can be reused as part of a larger bioinformatics algorithm

---

# Biological Applications

Multiple sequence alignment is commonly used for:

* Identifying conserved DNA regions
* Detecting mutations and sequence variation
* Comparing homologous genes
* Studying evolutionary relationships
* Finding functional sequence motifs
* Preparing sequence data for phylogenetic analysis
* Supporting gene and protein annotation

---

# Limitations

This project is an educational and simplified implementation.

* The first FASTA sequence is always used as the reference
* It does not build a guide tree
* It uses a fixed linear gap penalty
* It does not perform profile*to*profile alignment
* It does not include iterative refinement
* Results may depend on the sequence order
* Gap placement may differ when several paths have equal scores

Professional tools such as Clustal Omega, MUSCLE, and MAFFT use more advanced progressive and iterative alignment strategies.

---

# Next Steps

The next project will use sequence similarities or distances to construct a simplified phylogenetic tree using the UPGMA clustering algorithm.