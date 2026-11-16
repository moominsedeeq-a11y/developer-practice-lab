# 🚀 Developer Practice Lab

A structured, multi-language software engineering and programming laboratory maintained by **Moomin Sedeeq** ([@moominsedeeq-a11y](https://github.com/moominsedeeq-a11y)), a BCA (Bachelor of Computer Applications) student.

This repository tracks my journey across computer science fundamentals, object-oriented programming, systems thinking, and web application architecture. Rather than storing fragmented snippets or empty templates, every sub-project here is a **complete, verified, self-contained application** featuring dedicated documentation, input validation, and clean architecture.

---

## 🛠️ Technologies & Tooling

| Domain | Technologies & Libraries |
|:---|:---|
| **Web Development** | HTML5 (Semantic & Accessible), CSS3 (Grid, Flexbox, Custom Properties), Vanilla JavaScript (ES6+) |
| **Python Ecosystem** | Python 3.8+ (Standard Library: `secrets`, `dataclasses`, `math`, `unittest`, `typing`) |
| **Systems Programming** | Modern C++ (C++11/C++14 standard compliant), GCC / MinGW compiler |
| **Tooling & Workflow** | Git, PowerShell, Visual Studio Code |

---

## 📂 Repository Directory Structure

```text
developer-practice-lab/
├── .gitignore                      # Environment and compiler exclusions
├── LICENSE                         # MIT open-source license
├── README.md                       # Repository master index & guide
├── web/
│   ├── calculator/                 # Project 1: Personal Calculator
│   │   ├── index.html              # Accessible semantic markup
│   │   ├── style.css               # Responsive dark-theme styling
│   │   ├── app.js                  # Arithmetic engine & keyboard handling
│   │   └── README.md               # Calculator documentation
│   └── stopwatch/                  # Project 2: Precision Stopwatch
│       ├── index.html              # Digital readout & lap table
│       ├── style.css               # Modern UI & lap badge highlights
│       ├── app.js                  # Drift-free delta timing engine
│       └── README.md               # Stopwatch documentation
├── python/
│   ├── number_guessing_game/       # Project 3: Number Guessing Game
│   │   ├── game.py                 # Core game loop & session analytics
│   │   └── README.md               # Game rules & architecture
│   └── password_generator/         # Project 4: Secure Password Generator
│       ├── generator.py            # CSPRNG generator & entropy analyzer
│       └── README.md               # Security guide & developer API
├── cpp/
│   ├── student_grading_system/     # Project 5: Student Grading System
│   │   ├── main.cpp                # OOP student records & tabular reports
│   │   └── README.md               # Grade boundaries & compilation guide
│   └── pattern_generator/          # Project 6: Number Pattern Generator
│       ├── patterns.cpp            # 5 algorithmic nested-loop patterns
│       └── README.md               # Mathematical analysis of patterns
└── tests/
    ├── phase1_tests.js             # Automated web verification suite (Node.js)
    ├── test_python_projects.py     # Comprehensive Python test suite (unittest)
    └── run_all_tests.py            # Unified cross-language test runner
```

---

## 🔬 Featured Projects Overview

### 1. 🧮 Personal Calculator (`web/calculator/`)
- **Stack:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Key Features:**
  - Standard arithmetic: addition (`+`), subtraction (`−`), multiplication (`×`), and division (`÷`).
  - Floating-point precision guard (solves binary roundoff issues, e.g., `0.1 + 0.2 = 0.3`).
  - Decimal point deduplication and safe division by zero protection.
  - Full interactive keyboard shortcuts (`0-9`, `+ - * /`, `Enter`, `Backspace`, `Escape`).
  - Formatted comma thousands-separators preserving active decimal editing.

### 2. ⏱️ Precision Stopwatch (`web/stopwatch/`)
- **Stack:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Key Features:**
  - Drift-free delta timing engine using timestamp offsets (`Date.now() - startTime`), unaffected by browser throttling or tab switching.
  - Millisecond precision readout (`00:00:00.000`).
  - Interactive lap split recording computing discrete lap duration vs. cumulative time.
  - Automatic detection and badge highlighting for fastest (green) and slowest (red) laps.
  - Keyboard hotkeys (<kbd>Space</kbd> Start/Pause, <kbd>L</kbd> Lap, <kbd>R</kbd> Reset).

### 3. 🎯 Number Guessing Game (`python/number_guessing_game/`)
- **Stack:** Python 3 (Object-Oriented, Type Hints, Dataclasses)
- **Key Features:**
  - 4 tiered difficulty presets (Easy, Medium, Hard, Expert) plus customizable user bounds.
  - Dual-feedback system: Directional hints (`TOO HIGH`, `TOO LOW`) combined with proximity alerts (`Burning hot!`, `Warm`, `Lukewarm`, `Cold`).
  - Strict input sanitization guarding against non-integers, out-of-range guesses, and repeated guesses without penalizing attempts.
  - Persistent session analytics tracking win rate, win streaks, and best game scores.

### 4. 🔐 Cryptographically Secure Password Generator (`python/password_generator/`)
- **Stack:** Python 3 (`secrets` CSPRNG, `math`, `dataclasses`)
- **Key Features:**
  - True cryptographic randomness powered by OS-level entropy (`secrets` module), avoiding insecure PRNGs.
  - Guaranteed character category coverage (at least one uppercase, lowercase, digit, and symbol).
  - Optional visual ambiguity filter (excludes `0`, `O`, `1`, `l`, `I`, `|`).
  - Shannon information entropy calculation: $\text{Entropy (bits)} = L \times \log_2(R)$.
  - Qualitative security categorization (5 tiers from Very Weak to Very Strong).
  - Interactive CLI and reusable programmatic library API.

### 5. 🎓 Student Grading & Record System (`cpp/student_grading_system/`)
- **Stack:** C++ (C++11/C++14 Standard Compliant, GCC/MinGW)
- **Key Features:**
  - Object-oriented architecture with encapsulated `Student` entity and `GradeBook` registry.
  - Academic grading system mapping percentage marks to letter grades (`A+` to `F`) and GPA on a 4.0 scale.
  - Formatted tabular reporting with stream width manipulators (`std::setw`, `std::left`, `std::right`, `std::fixed`).
  - Multi-criteria search by unique Student ID or partial student name.
  - Class performance statistics (average score, pass rate, highest/lowest scorers).
  - Built-in headless automated test routine (`--test`).

### 6. 🔷 Algorithmic Number Pattern Generator (`cpp/pattern_generator/`)
- **Stack:** C++ (C++11/C++14 Standard Compliant, GCC/MinGW)
- **Key Features:**
  - 5 mathematical and geometric pattern engines:
    1. *Palindromic Number Pyramid* (coordinate symmetry).
    2. *Inverted Number Pyramid* (inverted nested loops).
    3. *Symmetric Number Diamond* (conjoined upper and lower half algorithms).
    4. *Floyd’s Triangle* (continuous natural number sequence $T_n = \frac{n(n+1)}{2}$).
    5. *Pascal’s Triangle* (combinatorial binomial coefficients $\binom{n}{k}$).
  - Strict row count validation preventing integer overflow and terminal distortion.
  - Automated algorithmic self-test suite (`--test`).

---

## 🚀 Getting Started & Execution

### Prerequisites
- Modern web browser (Chrome, Edge, Firefox, Brave)
- [Python 3.8+](https://www.python.org/)
- [GCC / G++](https://gcc.gnu.org/) (MinGW for Windows)
- [Node.js](https://nodejs.org/) (optional, for web verification runner)

### Clone Repository
```bash
git clone https://github.com/moominsedeeq-a11y/developer-practice-lab.git
cd developer-practice-lab
```

### 1. Web Projects
Simply open the `index.html` file in any modern browser:
- Calculator: `web/calculator/index.html`
- Stopwatch: `web/stopwatch/index.html`

### 2. Python Projects
Execute from the repository root:
```bash
# Run Number Guessing Game:
python python/number_guessing_game/game.py

# Run Secure Password Generator:
python python/password_generator/generator.py
```

### 3. C++ Projects
Compile and execute using `g++`:
```bash
# Student Grading System:
g++ -std=c++11 -Wall -Wextra -O2 cpp/student_grading_system/main.cpp -o student_system.exe
.\student_system.exe

# Pattern Generator:
g++ -std=c++11 -Wall -Wextra -O2 cpp/pattern_generator/patterns.cpp -o patterns.exe
.\patterns.exe
```

---

## 🧪 Unified Automated Testing

The repository includes a master test runner that runs all automated test suites across Web, Python, and C++ in a single command:

```bash
python tests/run_all_tests.py
```

### Individual Test Suites
- **Web Suite (Node.js):** `node tests/phase1_tests.js` (17 tests)
- **Python Suite (unittest):** `python tests/test_python_projects.py` (14 tests)
- **C++ Student System:** `.\cpp\student_grading_system\student_system.exe --test`
- **C++ Pattern Generator:** `.\cpp\pattern_generator\patterns.exe --test`

---

## 🎯 Learning Objectives & Philosophy

1. **Foundational Competence**: Building complete, production-ready mini applications without heavy third-party boilerplate.
2. **Clean Code & Structure**: Enforcing clean naming conventions, single-responsibility principle, and comprehensive inline documentation.
3. **Rigorous Input Validation**: Guarding against division by zero, float rounding errors, stream input invalidation, and boundary edge cases.
4. **Authentic Git History**: Maintaining an incremental, granular commit log documenting real, step-by-step progress.

---

## 🔮 Future Improvements & Roadmap

- [x] **Phase 1**: Web fundamentals (Calculator & Precision Stopwatch).
- [x] **Phase 2**: Python essentials (Number Guessing Game & Secure Password Generator).
- [x] **Phase 3**: C++ fundamentals (Student Grading System & Number Pattern Generator).
- [ ] **Phase 4**: Add interactive To-Do List with local storage persistence.
- [ ] **Phase 5**: Add automated Python File Organizer utility.
- [ ] **Phase 6**: Implement classic Data Structures (Linked Lists, Binary Trees) in modern C++.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE) — feel free to explore, learn from, and build upon it.

---
*Maintained with dedication by **Moomin Sedeeq** ([@moominsedeeq-a11y](https://github.com/moominsedeeq-a11y))*
