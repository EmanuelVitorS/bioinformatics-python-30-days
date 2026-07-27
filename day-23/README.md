# Day 23 - Protein Molecular Weight Calculator

# Overview

This project translates DNA sequences into proteins and calculates their molecular weight. It validates DNA sequences, translates them using the genetic code, determines the protein length, and estimates the molecular weight based on the average mass of each amino acid.

---

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Translate DNA into protein sequences
* Calculate protein length
* Calculate protein molecular weight
* Generate a protein analysis report

---

# Project Structure

day-23/
├── protein_molecular_weight.py
├── genetic_code.py
├── amino_acid_weight.py
├── test_sequences.fasta
└── README.md

---

# Example Output

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Protein:
MAAFKG

Length:
6 aa

Molecular Weight:
771.90 Da

---

# Skills Practiced

* FASTA file parsing
* DNA sequence validation
* DNA to protein translation
* Dictionary lookup
* Numerical calculations
* Report generation
* Modular programming

---

# What I Learned

* How to use a dictionary to store amino acid molecular weights
* How to calculate protein molecular weight by summing amino acid masses
* How to reuse previously developed functions in a bioinformatics workflow
* How to build modular and reusable Python programs

---

# Next Steps

The next project will continue expanding protein sequence analysis by introducing new bioinformatics techniques and calculations.