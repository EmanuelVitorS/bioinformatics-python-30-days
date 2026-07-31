# Day 26 - Protein Isoelectric Point Estimation

# Overview

This project estimates the isoelectric point (pI) of proteins translated from DNA sequences in a FASTA file.

The program validates DNA sequences, translates them into proteins, counts ionizable amino acids, calculates the protein net charge at different pH values using the Henderson–Hasselbalch equation, and estimates the pH where the net charge is closest to zero.

---

# Features

* Read DNA sequences from FASTA files
* Validate DNA sequences
* Translate DNA into protein sequences
* Count ionizable amino acids
* Calculate protein net charge at different pH values
* Estimate the protein isoelectric point (pI)
* Generate a protein analysis report

---

# Project Structure

day-26/
│── sequence_analyzer.py
│── genetic_code.py
│── amino_acid_pka.py
│── amino_acid_names.py
│── README.md

---

# Example Output

--------------------------------------------------

Sequence: Protein_1

Protein: MKRVDEHCK

Protein length: 9

Ionizable amino acids:
K - Lysine: 2
R - Arginine: 1
H - Histidine: 1
D - Aspartic acid: 1
E - Glutamic acid: 1
C - Cysteine: 1

Estimated isoelectric point: 8.47

---

# Skills Practiced

* Dictionaries
* Dictionary comprehensions
* Loops
* Conditional statements
* Functions
* FASTA file processing
* DNA translation
* Mathematical calculations in Python
* Henderson–Hasselbalch equation
* Protein charge estimation
* Bioinformatics data analysis

---

# What I Learned

* How to identify ionizable amino acids in protein sequences
* How amino acid pKa values influence protein charge
* How to calculate protein net charge at different pH values
* How to estimate the isoelectric point (pI)
* How to integrate biological concepts with Python programming

---

# Next Steps

In the next project, I will continue expanding my bioinformatics toolkit by implementing more advanced protein sequence analysis methods.