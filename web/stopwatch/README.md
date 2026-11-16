# Precision Digital Stopwatch

A high-accuracy digital stopwatch with lap recording, split analysis, and keyboard shortcuts built with pure **HTML5**, **CSS3**, and **JavaScript (ES6+)**.

---

## 🚀 Features

- **Drift-Free Time Tracking**: Computes elapsed duration using delta timestamps (`Date.now() - startTime`), preventing browser timer drift even when running in background tabs.
- **Millisecond Precision**: Displays time down to the thousandth of a second (`00:00:00.000`).
- **Interactive Lap Split System**:
  - Records individual lap durations alongside total cumulative elapsed time.
  - Automatically identifies and highlights the **Fastest Lap** (green) and **Slowest Lap** (red).
  - Displays most recent lap at the top of a scrollable log.
- **Accessible State Machine**:
  - Context-aware button states (disables Lap/Reset when inactive to prevent invalid actions).
  - Accessible keyboard shortcuts.
- **Modern Responsive Design**: Dark aesthetic with high contrast and smooth interactions.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action | State Condition |
|:---|:---|:---|
| <kbd>Space</kbd> | Start / Pause / Resume | Any |
| <kbd>L</kbd> | Record Lap split | Only while running |
| <kbd>R</kbd> | Reset to zero | When stopwatch has elapsed time |

---

## 📂 Project Structure

```text
web/stopwatch/
├── index.html   # Stopwatch layout, readout segments, and lap table
├── style.css    # Clean dark UI, layout grid, and lap badge styles
├── app.js       # Timing engine, lap recorder, and event bindings
└── README.md    # Documentation and usage guide
```

---

## 🖥️ How to Run

1. Open the project folder on your machine.
2. Navigate to `web/stopwatch/`.
3. Double-click `index.html` to open in any web browser.
   - Or open via VS Code Live Server for hot reload during development.

---

## 🧪 Testing

The logic is encapsulated in a testable `Stopwatch` class:
- Time formatting verification: `formatTime(3661042)` returns `01:01:01.042`.
- Lap calculation verification: computes delta between consecutive splits correctly.
- Extremes detection: accurately flags lowest and highest lap durations among recorded splits.
