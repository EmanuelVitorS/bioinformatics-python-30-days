# Day 30 - UPGMA Phylogenetic Tree Construction

# Overview

Phylogenetic trees are fundamental tools in bioinformatics for studying evolutionary relationships among biological sequences.

This project implements the UPGMA (Unweighted Pair Group Method with Arithmetic Mean) clustering algorithm to construct a simplified phylogenetic tree from DNA sequences.

The program reads multiple DNA sequences from a FASTA file, validates the sequences, calculates pairwise genetic distances using the normalized Hamming distance, progressively clusters the most similar sequences, and generates a phylogenetic tree in Newick format.

---

# Features

* Read multiple DNA sequences from FASTA files
* Validate DNA sequences
* Verify sequence length consistency
* Calculate normalized Hamming distances
* Build a pairwise distance matrix
* Identify the closest sequence clusters
* Construct a phylogenetic tree using the UPGMA algorithm
* Generate clustering steps
* Export the tree in Newick format
* Generate a complete phylogenetic analysis report

---

## Project Structure

day-30/
├── upgma_phylogenetic_tree.py
├── test.fasta
├── upgma_tree.newick
└── README.md

---

# Algorithm Workflow

Read FASTA
        ↓
Validate DNA sequences
        ↓
Check sequence lengths
        ↓
Calculate pairwise distances
        ↓
Build distance matrix
        ↓
Find closest clusters
        ↓
Merge clusters
        ↓
Update distance matrix
        ↓
Repeat until one cluster remains
        ↓
Generate Newick tree

---

## Distance Calculation

The program calculates the normalized Hamming distance:

                      
Distance = Number of mismatches / Sequence length
       

Example:


Sequence 1
ATGCGT

Sequence 2
ATGCAT


Mismatches = 1

Distance = 1 / 6 = 0.1667


---

## Example Input

>sequence_1
ATGCGTACGTAG

>sequence_2
ATGCGTACGTAA

>sequence_3
ATGAGTTCGTAG

>sequence_4
ATGAGTTCGTAA

---

# Example Output

----------------------------------------------------------------------
UPGMA Phylogenetic Tree
----------------------------------------------------------------------

Number of sequences: 4

Pairwise distance matrix:

               sequence_1  sequence_2  sequence_3  sequence_4

sequence_1         0.0000      0.0833      0.1667      0.2500
sequence_2         0.0833      0.0000      0.2500      0.1667
sequence_3         0.1667      0.2500      0.0000      0.0833
sequence_4         0.2500      0.1667      0.0833      0.0000

Clustering steps:

Step 1
Merge sequence_1 and sequence_2

Step 2
Merge sequence_3 and sequence_4

Step 3
Merge both clusters

Newick tree:

((sequence_1:0.0417,sequence_2:0.0417):0.0625,(sequence_3:0.0417,sequence_4:0.0417):0.0625);

---

# Skills Practiced

* Hierarchical clustering
* UPGMA algorithm
* Distance matrix construction
* Dictionary manipulation
* Nested dictionaries
* Matrix operations
* Loops
* Functions
* FASTA file processing
* DNA sequence validation
* Hamming distance calculation
* Newick tree generation
* Bioinformatics data analysis

---

# What I Learned

* How phylogenetic trees represent evolutionary relationships
* How the UPGMA algorithm progressively clusters similar sequences
* How pairwise distance matrices are constructed
* How normalized Hamming distance can be used to compare DNA sequences
* How Newick format represents phylogenetic trees
* How hierarchical clustering algorithms work
* How to combine multiple bioinformatics concepts into a complete analysis pipeline

---

# Biological Applications

UPGMA trees can be used for:

* Evolutionary studies
* Comparative genomics
* Gene family analysis
* Species relationship analysis
* Sequence similarity studies
* Educational phylogenetic analysis
* Clustering homologous sequences

---

# Limitations

This implementation is intended for educational purposes.

* Uses normalized Hamming distance
* Requires sequences with the same length
* Assumes a constant evolutionary rate (molecular clock)
* Does not perform multiple sequence alignment automatically
* Does not use substitution matrices
* Does not estimate branch support values

Professional phylogenetic software generally implements more sophisticated evolutionary models and tree reconstruction methods.

---

# Next Steps

This project concludes the **30 Days of Bioinformatics Python** challenge.

Throughout these 30 projects, I explored fundamental bioinformatics concepts including DNA sequence analysis, protein analysis, sequence alignment, multiple sequence alignment, and phylogenetic tree construction using Python.