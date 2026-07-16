# Day 14 - DNA Sequence Analyzer

# Overview

On Day 14, I integrated the bioinformatics functions developed throughout the previous days into a complete DNA sequence analysis pipeline.

The program reads DNA sequences from a FASTA file and performs multiple analyses, including sequence validation, GC/AT content calculation, DNA transcription, protein translation, Open Reading Frame (ORF) detection, and formatted report generation.

This project represents the first complete bioinformatics workflow of the challenge, combining all previous modules into a single application.

---

# Features

* Read DNA sequences from FASTA files
* Validate nucleotide sequences
* Calculate sequence length
* Calculate GC and AT content
* Transcribe DNA into RNA
* Translate DNA into protein sequences
* Detect Open Reading Frames (ORFs)
* Generate a formatted analysis report for each sequence

---

# Project Structure

```text
day*14/
│
├── sequence_analyzer.py
├── genetic_code.py
├── example.fasta
└── README.md
```

---

# Workflow

```text
Read FASTA
     │
     ▼
Validate Sequence
     │
     ▼
Calculate GC & AT Content
     │
     ▼
Transcribe DNA → RNA
     │
     ▼
Translate DNA → Protein
     │
     ▼
Find ORFs
     │
     ▼
Generate Report
```

---

# Example Output

==================================================
Sequence: seq1
Status: Valid ✅

Length: 39 bp
GC: 56.41%
AT: 43.59%

RNA:
AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG

Protein:
MAIVMGR

ORFs found: 1

---

# What I Learned

* Integrating multiple bioinformatics functions into a single workflow
* Organizing Python projects into reusable modules
* Separating analysis logic from report generation
* Importing custom modules
* Working with dictionaries to store analysis results
* Building a simple bioinformatics analysis pipeline
* Writing cleaner and more maintainable code

---

# Next Steps

* Export reports to TXT or CSV
* Analyze reverse complement sequences
* Detect the longest ORF
* Add sequence statistics and summary reports
* Start using Biopython for sequence manipulation