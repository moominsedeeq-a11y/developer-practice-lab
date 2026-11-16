# 🎯 Number Guessing Game (Python CLI)

An interactive, object-oriented terminal guessing game written in **Python 3**. Demonstrates clean modular architecture, rigorous input validation, customizable difficulty levels, proximity feedback, and persistent session statistics.

---

## 🚀 Features

- **Tiered Difficulty Presets**:
  - **Easy**: Range `1 – 50` with `10` attempts (Ideal for beginners).
  - **Medium**: Range `1 – 100` with `7` attempts (Standard challenge).
  - **Hard**: Range `1 – 250` with `6` attempts (Advanced difficulty).
  - **Expert**: Range `1 – 500` with `5` attempts (Precision challenge).
  - **Custom Mode**: Fully configurable minimum, maximum, and maximum attempts.
- **Intelligent Feedback Engine**:
  - **Directional Hints**: Informs the player if their guess is `TOO HIGH` or `TOO LOW`.
  - **Proximity Clues**: Dynamic distance calculation providing clues (`Burning hot!`, `Warm`, `Lukewarm`, `Cold`).
- **Comprehensive Input Sanitization**:
  - Rejects non-integer inputs without consuming player attempts.
  - Detects and warns against out-of-range numbers.
  - Warns against repeated guesses so players do not waste attempts.
- **Cumulative Session Analytics**:
  - Tracks total games played and total victories.
  - Computes dynamic **Win Rate (%)**.
  - Records **Best Score** (fewest attempts used to win).
  - Tracks **Current Streak** and all-time **Highest Win Streak**.
- **Replay Loop**: Seamless round continuation with cumulative statistics retention.

---

## 📂 Project Structure

```text
python/number_guessing_game/
├── game.py       # Core game state engine, difficulty presets, and CLI loop
└── README.md     # Documentation, rules, and execution guide
```

---

## 🖥️ How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Execution
From the root of the repository or from the game's directory:

```bash
# From repository root:
python python/number_guessing_game/game.py

# Or navigate directly:
cd python/number_guessing_game
python game.py
```

---

## 🧪 Testing

The game logic is decoupled from terminal I/O via the `NumberGuessingGame` and `GameSessionStats` classes, making every component deterministic and testable.

Automated unit tests cover:
- Secret number initialization and boundary enforcement.
- Out-of-bounds input detection (`validate_guess`).
- Duplicate guess detection.
- Directional and proximity hint calculation.
- Maximum attempts limit and game termination.
- Session win rate and streak tracking.

To run the test suite, see `tests/test_python_projects.py`.
