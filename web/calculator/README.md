# Personal Calculator

A modern, accessible, and responsive personal calculator built with pure vanilla **HTML5**, **CSS3**, and **JavaScript (ES6+)**.

---

## 🚀 Features

- **Standard Arithmetic**: Addition (`+`), Subtraction (`−`), Multiplication (`×`), and Division (`÷`).
- **Precision Floating-Point**: Solves common binary floating-point rounding issues (e.g., `0.1 + 0.2 = 0.3`).
- **Input Guards**:
  - Prevents multiple consecutive or duplicate decimal points (e.g., `5..4` or `3.1.2`).
  - Safe zero handling and leading zero cleanup.
  - Division by zero error handling (`Cannot divide by 0`).
- **Keyboard Shortcuts**: Complete interactive typing support for all operations.
- **Display Formatting**: Comma-separated thousands formatting for large integers while preserving exact decimal entries.
- **Utility Actions**:
  - `AC`: All clear (resets operand state and memory).
  - `DEL`: Backspace / single-character deletion.
  - `±`: Sign toggle between positive and negative.
  - `%`: Direct percentage calculation.

---

## ⌨️ Keyboard Shortcuts

| Key | Calculator Action |
|:---|:---|
| `0` – `9` | Enter numbers |
| `.` | Enter decimal point |
| `+` | Add operation |
| `-` | Subtract operation |
| `*` | Multiply operation |
| `/` | Divide operation |
| `Enter` or `=` | Calculate result |
| `Backspace` | Delete last digit (`DEL`) |
| `Escape` | Clear all (`AC`) |
| `%` | Percentage |

---

## 📂 Project Structure

```text
web/calculator/
├── index.html   # Accessible semantic structure and layout
├── style.css    # Responsive grid, color tokens, and button styles
├── app.js       # Core Calculator state machine and event handlers
└── README.md    # Documentation and usage guide
```

---

## 🖥️ How to Run

1. Clone or open the repository folder on your machine.
2. Navigate to `web/calculator/`.
3. Double-click `index.html` to open it in any web browser (Chrome, Edge, Firefox, Safari).
   - Alternatively, right-click `index.html` and select **Open with Live Server** if using VS Code.

---

## 🧪 Testing

The calculator logic is architected with a modular `Calculator` class exportable for automated testing (e.g., via Node.js). It handles edge cases including:
- Negative operand calculations: `-5 × 3 = -15`
- Division by zero: `10 ÷ 0` results in a polite error message.
- Decimal operations: `0.1 + 0.2 = 0.3`
- Sequential operation chaining: `2 + 3 + 4 = 9`
