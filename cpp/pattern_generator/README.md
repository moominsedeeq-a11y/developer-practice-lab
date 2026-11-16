# 🔷 Algorithmic Number Pattern Generator (C++)

A modular, menu-driven C++ application demonstrating nested loops, arithmetic sequences, coordinate symmetry, and dynamic combinatorial calculations.

---

## 📐 Patterns & Algorithmic Analysis

### 1. Palindromic Number Pyramid
- **Structure**: Symmetrical pyramid where each row increases from `1` to `i`, then decreases back to `1`.
- **Logic**:
  - Outer loop tracks row `i` from `1` to `rows`.
  - Leading spaces: `(rows - i) * 2`.
  - Inner loop 1 (Ascending): `1` to `i`.
  - Inner loop 2 (Descending): `i - 1` down to `1`.
- **Complexity**: Time: $\mathcal{O}(n^2)$ | Space: $\mathcal{O}(1)$.

### 2. Inverted Number Pyramid
- **Structure**: Symmetrical inverted pyramid starting at row `n` down to `1`.
- **Logic**: Symmetrical inversion of the standard pyramid with decreasing row index $i$.
- **Complexity**: Time: $\mathcal{O}(n^2)$ | Space: $\mathcal{O}(1)$.

### 3. Symmetric Number Diamond
- **Structure**: Full diamond created by conjoining an upper pyramid of $n$ rows with a lower inverted pyramid of $n - 1$ rows.
- **Complexity**: Time: $\mathcal{O}(n^2)$ | Space: $\mathcal{O}(1)$.

### 4. Floyd's Triangle
- **Structure**: Right-angled triangle of consecutive natural numbers.
  ```text
  1
  2   3
  4   5   6
  7   8   9  10
  ```
- **Logic**: A single monotonically increasing counter printed across row $i$ containing exactly $i$ elements. Total elements printed equals the $n$-th triangular number:
  $$T_n = \frac{n(n + 1)}{2}$$
- **Complexity**: Time: $\mathcal{O}(n^2)$ | Space: $\mathcal{O}(1)$.

### 5. Pascal's Triangle
- **Structure**: Triangular array of the binomial coefficients:
  $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
- **Logic**: Computes terms iteratively to prevent factorial overflow:
  $$C(n, k) = C(n, k - 1) \times \frac{n - k + 1}{k}$$
- **Complexity**: Time: $\mathcal{O}(n^2)$ | Space: $\mathcal{O}(1)$.

---

## 📂 Project Structure

```text
cpp/pattern_generator/
├── patterns.cpp   # Pattern rendering algorithms, input validation, and menu
└── README.md      # Mathematical explanations and compilation instructions
```

---

## 🖥️ Compilation & Execution

### Prerequisites
- Modern C++ compiler supporting C++11 (GCC / MinGW, Clang, or MSVC).

### Compilation
From the project folder:
```bash
g++ -std=c++11 -Wall -Wextra -O2 patterns.cpp -o patterns.exe
```

### Execution
```bash
# Interactive menu:
.\patterns.exe

# Automated headless verification suite:
.\patterns.exe --test
```
