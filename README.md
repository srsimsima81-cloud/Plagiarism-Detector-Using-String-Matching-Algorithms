# ⚡ Plagiarism Detector Using String Matching Algorithms

A plagiarism detection system built using Python, Streamlit, and classic string matching algorithms (Naive Matching, KMP, Rabin-Karp). The system compares two documents, detects similarity, calculates plagiarism percentage, and generates a detailed report with a modern neon UI dashboard.

---

## 🚀 Project Overview

Plagiarism detection is widely used in academic institutions, research paper validation, content publishing platforms, online examination systems, EdTech platforms, and copyright protection systems. This project demonstrates how string matching algorithms can be used to detect similarity between documents efficiently.

---

## 🎯 Problem Statement

Given two text documents (original and submitted), the system must detect exact and partial matches, identify similar words and phrases, compute plagiarism percentage, and generate a detailed report along with a visual dashboard.

---

## ✨ Features

Document Processing: input text handling, cleaning, preprocessing, tokenization  
Plagiarism Detection: Naive Matching, KMP Algorithm, Rabin-Karp Algorithm, hashing techniques  
Analysis: similarity percentage, matched word extraction, phrase detection  
Dashboard: neon Streamlit UI, real-time detection, interactive panels  
Reports: detailed plagiarism report generation and exportable results  

---

## 🧠 DSA Concepts Used

Strings, arrays, sets, hash tables, pattern matching, rolling hash technique, prefix table (LPS array), sliding window, and time complexity analysis.

Naive Matching complexity: O(n × m)  
KMP complexity: O(n + m)  
Rabin-Karp average complexity: O(n + m)

---

## 🏗️ System Architecture

Document Input → Preprocessing → Tokenization → String Matching Engine (Naive / KMP / Rabin-Karp) → Similarity Calculation → Report Generation → Streamlit Dashboard Output

---

## 📂 Project Structure

Plagiarism-Detector-Using-String-Matching/
│
├── documents/ (original.txt, submitted.txt)
├── outputs/ (sample outputs)
├── reports/ (generated plagiarism reports)
├── images/ (UI screenshots and results)
├── docs/ (architecture, algorithm explanation, future enhancements)
├── src/ (preprocess, naive_match, kmp, rabin_karp, similarity, report modules)
├── main.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Installation

Clone the repository: git clone https://github.com/yourusername/Plagiarism-Detector-Using-String-Matching.git and cd into the folder.

Create virtual environment: python -m venv venv

Activate environment: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)

Install dependencies: pip install -r requirements.txt

---

## ▶️ Run Project

Run CLI version: python main.py  
Run Streamlit UI: streamlit run app.py

---

## 📊 Sample Output

Similarity Score: 81.25%  
Matched Words: data, structures, algorithms, python, databases

---

## 🖥️ UI Features

Neon dark dashboard, side-by-side document input, real-time plagiarism detection, similarity score display, and clean visualization of matched results.

---

## 🌟 Future Enhancements

Sentence-level plagiarism detection, PDF/DOCX support, Winnowing fingerprinting, MinHash and LSH algorithms, AI-based semantic similarity detection, highlight copied text, export PDF reports, multi-document comparison system.

---

## 💼 Industry Applications

Academic plagiarism detection, research validation, content verification systems, online exam monitoring systems, copyright protection tools, EdTech assessment platforms.

---

## 🎓 Learning Outcomes

Strong understanding of string algorithms, implementation of KMP and Rabin-Karp, text processing skills, Streamlit UI development, real-world DSA application, and GitHub project structuring.

---

