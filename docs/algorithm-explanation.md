# Algorithms Used

## Naive String Matching

Compares pattern with every position in text.

Time Complexity:

O(N × M)

---

## KMP Algorithm

Uses Longest Prefix Suffix (LPS) array.

Time Complexity:

O(N + M)

Advantages:

- Faster than naive matching
- Avoids redundant comparisons

---

## Rabin-Karp Algorithm

Uses rolling hash technique.

Average Time Complexity:

O(N + M)

Advantages:

- Fast substring matching
- Suitable for multiple pattern detection

---

## Similarity Calculation

Similarity =

(Common Words / Total Words) × 100