# System Architecture

## Workflow

Input Documents
        |
        V
Text Preprocessing
        |
        V
Sentence Tokenization
        |
        V
Naive Matching
        |
        V
KMP Matching
        |
        V
Rabin-Karp Matching
        |
        V
Similarity Calculation
        |
        V
Report Generation
        |
        V
Final Output

## Components

### File Reader

Reads original and submitted files.

### Preprocessor

Removes punctuation, extra spaces and converts text to lowercase.

### Matching Engine

Uses:
- Naive Matching
- KMP
- Rabin-Karp

### Similarity Engine

Calculates plagiarism percentage.

### Report Generator

Creates detailed plagiarism report.