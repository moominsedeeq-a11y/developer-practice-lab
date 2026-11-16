# 🚀 Developer Practice Lab

Welcome to **Developer Practice Lab**, a structured hands-on repository maintained by **Moomin Sedeeq** ([@moominsedeeq-a11y](https://github.com/moominsedeeq-a11y)), a BCA (Bachelor of Computer Applications) student.

This repository tracks my journey in core programming, algorithms, and practical software engineering. Rather than storing fragmented snippets or empty templates, every sub-project here is a **fully working, self-contained application** complete with dedicated documentation, input validation, and clean architecture.

---

## 🛠️ Languages & Technologies

- **Web Technologies:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Systems & Scripting:** Python 3 (3.8+), C++ (C++11/C++14 via GCC/MinGW)
- **Version Control & Tooling:** Git, VS Code, PowerShell

---

## 📂 Repository Directory

| Category | Project | Language(s) | Description | Status |
|:---|:---|:---|:---|:---:|
| **Web** | [Personal Calculator](./web/calculator/) | HTML5, CSS3, JS | Responsive arithmetic calculator with keyboard support and floating-point precision guards | ✅ Complete |
| **Web** | [Precision Stopwatch](./web/stopwatch/) | HTML5, CSS3, JS | Millisecond stopwatch with drift-free delta timing, split laps, and fastest/slowest detection | ✅ Complete |
| **Python** | [Number Guessing Game](./python/number_guessing_game/) | Python 3 | Interactive terminal game with difficulty tiers, statistical tracking, and input sanitization | ✅ Complete |
| **Python** | [Secure Password Generator](./python/password_generator/) | Python 3 | Cryptographically secure customizable password generator with Shannon entropy evaluation | ✅ Complete |
| **C++** | [Student Grading System](./cpp/student_grading_system/) | C++ | Terminal-based student record manager with GPA computation and tabular summary reports | ✅ Complete |
| **C++** | [Pattern Generator](./cpp/pattern_generator/) | C++ | Algorithmic generator for geometric, pyramid, diamond, and Pascal's triangle patterns | ✅ Complete |

---

## 🎯 Learning Objectives

1. **Foundational Competence**: Build complete, functional programs without relying on heavy abstractions or third-party boilerplate.
2. **Clean Code & Structure**: Write maintainable code with clear naming conventions, separation of concerns, and meaningful inline comments.
3. **Robust Input Handling**: Guard against edge cases such as division by zero, floating-point roundoff, type errors, and unexpected user inputs.
4. **Professional Git Workflow**: Maintain an authentic, granular commit history that accurately documents every incremental milestone.

---

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Edge, Firefox, Brave)
- [Python 3.8+](https://www.python.org/) for Python modules
- [GCC / G++](https://gcc.gnu.org/) (MinGW for Windows) for C++ programs
- [Node.js](https://nodejs.org/) (optional, for web verification suite)

### Clone & Explore
```bash
git clone https://github.com/moominsedeeq-a11y/developer-practice-lab.git
cd developer-practice-lab
```

### 1. Running Web Applications
Navigate to the desired web directory and open `index.html` in any browser:
- Calculator: `web/calculator/index.html`
- Stopwatch: `web/stopwatch/index.html`

### 2. Running Python Applications
Execute directly from the repository root:
```bash
# Number Guessing Game:
python python/number_guessing_game/game.py

# Secure Password Generator:
python python/password_generator/generator.py
```

### 3. Compiling & Running C++ Applications
Compile and run with `g++`:
```bash
# Student Grading System:
g++ -std=c++11 -O2 cpp/student_grading_system/main.cpp -o student_system.exe
.\student_system.exe

# Algorithmic Pattern Generator:
g++ -std=c++11 -O2 cpp/pattern_generator/patterns.cpp -o patterns.exe
.\patterns.exe
```

---

## 🧪 Unified Automated Testing

Run the master test runner to execute the automated test suites across all three language ecosystems simultaneously:

```bash
python tests/run_all_tests.py
```

Individual test suites:
- Web unit tests: `node tests/phase1_tests.js`
- Python unit tests: `python tests/test_python_projects.py`
- C++ self-tests: `.\student_system.exe --test` & `.\patterns.exe --test`

---

## 📋 Roadmap

- [x] **Phase 1 (Web Fundamentals)**: Implement responsive Calculator and Precision Stopwatch with unit tests and full documentation.
- [x] **Phase 2 (Python Essentials)**: Build CLI Number Guessing Game and Secure Password Generator with automated `unittest` coverage.
- [x] **Phase 3 (C++ Fundamentals)**: Implement Student Grading System and Algorithmic Pattern Generator using object-oriented principles.
- [ ] **Phase 4 (Expansion)**: Add To-Do List application, Unit Converter, and File Organization utility.

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE) — free to reference and learn from.
