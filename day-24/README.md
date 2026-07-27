# Day 24 - Protein Hydrophobicity Analysis

# Overview

This project translates DNA sequences into proteins and analyzes their average hydrophobicity using the Kyte-Doolittle hydrophobicity scale. It validates DNA sequences, calculates the average hydrophobicity of the translated protein, classifies the protein based on its hydrophobicity, and generates a detailed analysis report.

---

# Features

* Read DNA sequences from a FASTA file
* Validate DNA sequences
* Translate DNA into protein sequences
* Calculate average protein hydrophobicity
* Classify proteins based on hydrophobicity
* Generate a protein analysis report

---

# Project Structure

day-24/
├── protein_hydrophobicity_analysis.py
├── genetic_code.py
├── amino_acid_hydrophobicity.py
├── test_sequences.fasta
└── README.md

---

# Example Output

--------------------------------------------------
Sequence: seq1
Status: Valid ✅

Protein:
MAVLIFG

Length:
7 aa

Average Hydrophobicity:
2.34

Classification:
Hydrophobic

---

# Skills Practiced

* FASTA file parsing
* DNA sequence validation
* DNA to protein translation
* Dictionary lookup
* Numerical calculations
* Conditional statements
* Report generation
* Modular programming

---

# What I Learned

* How to use the Kyte*Doolittle hydrophobicity scale
* How to calculate the average hydrophobicity of a protein
* How to classify proteins based on hydrophobicity values
* How to organize biological reference data into reusable Python modules
* How to build modular bioinformatics pipelines

---

# Next Steps

The next project will continue expanding protein sequence analysis by exploring additional biological properties and protein characterization techniques.