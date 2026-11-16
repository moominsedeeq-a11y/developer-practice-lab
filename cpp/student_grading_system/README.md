# 🎓 Student Grading & Record System (C++)

An object-oriented academic record management application written in modern standard **C++ (C++11/14)**.

Demonstrates encapsulation, class composition, stream formatting (`<iomanip>`), input validation, tabular report generation, and class-level statistical analytics.

---

## 🚀 Features

- **Object-Oriented Design**:
  - `Student`: Encapsulates student ID, name, marks per subject, percentage calculation, grade assignment, and GPA.
  - `GradeBook`: Manages the collection of student records, duplicate ID prevention, searching, and statistical aggregation.
- **Accurate Academic Grading & GPA**:
  Maps numerical percentages to standardized letter grades and GPA on a 4.0 scale:

  | Percentage Range | Grade | GPA Point | Classification |
  |:---:|:---:|:---:|:---|
  | `90.0% – 100.0%` | **A+** | **4.00** | Outstanding |
  | `80.0% – 89.9%`  | **A**  | **3.70** | Excellent |
  | `70.0% – 79.9%`  | **B**  | **3.00** | Good |
  | `60.0% – 69.9%`  | **C**  | **2.00** | Satisfactory |
  | `50.0% – 59.9%`  | **D**  | **1.00** | Pass |
  | `< 50.0%`        | **F**  | **0.00** | Fail |

- **Formatted Tabular Presentation**:
  Uses `std::setw`, `std::left`, `std::right`, and `std::fixed` with precision specifiers to render clean CLI tables.
- **Multi-criteria Search**:
  - Search by exact Student ID (displays complete subject-by-subject report card).
  - Search by Name / substring (case-insensitive partial matching).
- **Class Analytics**:
  Computes total enrolled count, pass/fail counts, class percentage average, highest scorer, and lowest scorer.
- **Robust Input Validation**:
  - Rejects empty IDs and names.
  - Rejects duplicate student IDs.
  - Enforces mark boundaries ($0.0 \le \text{mark} \le 100.0$).
  - Resilient against non-numeric menu input through stream state recovery (`std::cin.clear()` and buffer flushing).

---

## 📂 Project Structure

```text
cpp/student_grading_system/
├── main.cpp       # Student & GradeBook classes, CLI menu, and self-test suite
└── README.md      # Compilation instructions and architectural overview
```

---

## 🖥️ Compilation & Execution

### Prerequisites
- GCC / G++ (MinGW on Windows or GCC on Linux/macOS) supporting C++11 or higher.

### Compilation
From the project folder:
```bash
g++ -std=c++11 -Wall -Wextra -O2 main.cpp -o student_system.exe
```

### Running the Application
```bash
# Run interactive menu:
.\student_system.exe

# Run automated headless verification suite:
.\student_system.exe --test
```

---

## 🧪 Testing & Validation

The application contains a built-in automated test routine accessible via CLI flag `--test` or Menu Option `7`. It verifies:
- Mathematical accuracy of grade and GPA boundaries.
- Total and percentage calculations across 5 subjects.
- Rejection of duplicate student IDs.
- Rejection of out-of-bounds marks (`> 100` or `< 0`).
- Case-insensitive substring name search.
