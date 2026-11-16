/**
 * Precision Digital Stopwatch
 * Implements drift-free delta time tracking, lap recording,
 * fastest/slowest lap detection, and keyboard hotkeys.
 */

class Stopwatch {
  constructor(options = {}) {
    this.elapsedTime = 0;
    this.startTime = 0;
    this.timerId = null;
    this.isRunning = false;
    this.laps = [];
    this.lastLapTime = 0;

    // DOM References (optional for headless testing)
    this.elements = {
      hours: options.hours || null,
      minutes: options.minutes || null,
      seconds: options.seconds || null,
      milliseconds: options.milliseconds || null,
      startPauseBtn: options.startPauseBtn || null,
      lapBtn: options.lapBtn || null,
      resetBtn: options.resetBtn || null,
      lapsList: options.lapsList || null,
      noLapsMsg: options.noLapsMsg || null
    };
  }

  /**
   * Formats a millisecond duration into an object with zero-padded components
   * @param {number} ms - Milliseconds
   * @returns {{hours: string, minutes: string, seconds: string, milliseconds: string, formatted: string}}
   */
  static formatTime(ms) {
    if (ms < 0) ms = 0;
    const totalSeconds = Math.floor(ms / 1000);
    const milliseconds = Math.floor(ms % 1000);
    const seconds = totalSeconds % 60;
    const minutes = Math.floor(totalSeconds / 60) % 60;
    const hours = Math.floor(totalSeconds / 3600);

    const pad = (num, digits = 2) => num.toString().padStart(digits, '0');

    return {
      hours: pad(hours),
      minutes: pad(minutes),
      seconds: pad(seconds),
      milliseconds: pad(milliseconds, 3),
      formatted: `${pad(hours)}:${pad(minutes)}:${pad(seconds)}.${pad(milliseconds, 3)}`
    };
  }

  /**
   * Starts or resumes the stopwatch
   */
  start() {
    if (this.isRunning) return;
    this.isRunning = true;
    this.startTime = Date.now() - this.elapsedTime;

    const tick = () => {
      if (!this.isRunning) return;
      this.elapsedTime = Date.now() - this.startTime;
      this.updateDisplay();
      this.timerId = requestAnimationFrame(tick);
    };

    this.timerId = requestAnimationFrame(tick);
    this.updateControls();
  }

  /**
   * Pauses the stopwatch
   */
  pause() {
    if (!this.isRunning) return;
    this.isRunning = false;
    if (this.timerId) {
      cancelAnimationFrame(this.timerId);
      this.timerId = null;
    }
    this.elapsedTime = Date.now() - this.startTime;
    this.updateDisplay();
    this.updateControls();
  }

  /**
   * Toggles between start and pause states
   */
  toggle() {
    if (this.isRunning) {
      this.pause();
    } else {
      this.start();
    }
  }

  /**
   * Resets the stopwatch to 0 and clears all recorded laps
   */
  reset() {
    this.pause();
    this.elapsedTime = 0;
    this.startTime = 0;
    this.lastLapTime = 0;
    this.laps = [];
    this.updateDisplay();
    this.renderLaps();
    this.updateControls();
  }

  /**
   * Records a lap split
   * @returns {{lapNumber: number, lapDuration: number, totalTime: number}|null}
   */
  recordLap() {
    if (!this.isRunning && this.elapsedTime === 0) return null;

    const currentTotal = this.elapsedTime;
    const lapDuration = currentTotal - this.lastLapTime;
    this.lastLapTime = currentTotal;

    const lap = {
      lapNumber: this.laps.length + 1,
      lapDuration,
      totalTime: currentTotal
    };

    this.laps.unshift(lap); // Most recent lap at top
    this.renderLaps();
    return lap;
  }

  /**
   * Identifies the fastest and slowest recorded laps
   * @returns {{fastestId: number|null, slowestId: number|null}}
   */
  getLapExtremes() {
    if (this.laps.length < 2) {
      return { fastestId: null, slowestId: null };
    }

    let fastest = this.laps[0];
    let slowest = this.laps[0];

    for (const lap of this.laps) {
      if (lap.lapDuration < fastest.lapDuration) fastest = lap;
      if (lap.lapDuration > slowest.lapDuration) slowest = lap;
    }

    return {
      fastestId: fastest.lapNumber,
      slowestId: slowest.lapNumber
    };
  }

  /**
   * Updates display segments in the DOM
   */
  updateDisplay() {
    const formatted = Stopwatch.formatTime(this.elapsedTime);

    if (this.elements.hours) this.elements.hours.textContent = formatted.hours;
    if (this.elements.minutes) this.elements.minutes.textContent = formatted.minutes;
    if (this.elements.seconds) this.elements.seconds.textContent = formatted.seconds;
    if (this.elements.milliseconds) this.elements.milliseconds.textContent = formatted.milliseconds;
  }

  /**
   * Updates button states and labels
   */
  updateControls() {
    if (!this.elements.startPauseBtn) return;

    if (this.isRunning) {
      this.elements.startPauseBtn.textContent = 'Pause';
      this.elements.startPauseBtn.classList.add('is-running');
      if (this.elements.lapBtn) this.elements.lapBtn.disabled = false;
      if (this.elements.resetBtn) this.elements.resetBtn.disabled = false;
    } else {
      this.elements.startPauseBtn.textContent = this.elapsedTime > 0 ? 'Resume' : 'Start';
      this.elements.startPauseBtn.classList.remove('is-running');
      if (this.elements.lapBtn) this.elements.lapBtn.disabled = true;
      if (this.elements.resetBtn) this.elements.resetBtn.disabled = this.elapsedTime === 0;
    }
  }

  /**
   * Renders the laps table with highlight badges
   */
  renderLaps() {
    if (!this.elements.lapsList) return;

    if (this.laps.length === 0) {
      if (this.elements.noLapsMsg) {
        this.elements.lapsList.innerHTML = '<p class="no-laps-msg" id="noLapsMsg">No laps recorded yet.</p>';
      }
      return;
    }

    const { fastestId, slowestId } = this.getLapExtremes();

    const rows = this.laps.map(lap => {
      let badgeClass = '';
      if (lap.lapNumber === fastestId) badgeClass = 'lap-fastest';
      else if (lap.lapNumber === slowestId) badgeClass = 'lap-slowest';

      const lapFormatted = Stopwatch.formatTime(lap.lapDuration);
      const totalFormatted = Stopwatch.formatTime(lap.totalTime);

      return `
        <div class="lap-item ${badgeClass}" role="listitem">
          <span>Lap ${lap.lapNumber}</span>
          <span>+${lapFormatted.minutes}:${lapFormatted.seconds}.${lapFormatted.milliseconds}</span>
          <span>${totalFormatted.formatted}</span>
        </div>
      `;
    }).join('');

    this.elements.lapsList.innerHTML = rows;
  }
}

// Browser Initialization
if (typeof window !== 'undefined' && typeof document !== 'undefined') {
  const stopwatch = new Stopwatch({
    hours: document.getElementById('hours'),
    minutes: document.getElementById('minutes'),
    seconds: document.getElementById('seconds'),
    milliseconds: document.getElementById('milliseconds'),
    startPauseBtn: document.getElementById('startPauseBtn'),
    lapBtn: document.getElementById('lapBtn'),
    resetBtn: document.getElementById('resetBtn'),
    lapsList: document.getElementById('lapsList'),
    noLapsMsg: document.getElementById('noLapsMsg')
  });

  // Button Listeners
  document.getElementById('startPauseBtn')?.addEventListener('click', () => {
    stopwatch.toggle();
  });

  document.getElementById('lapBtn')?.addEventListener('click', () => {
    stopwatch.recordLap();
  });

  document.getElementById('resetBtn')?.addEventListener('click', () => {
    stopwatch.reset();
  });

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    // Ignore hotkeys when typing in input/textarea (if any added later)
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    if (e.code === 'Space') {
      e.preventDefault();
      stopwatch.toggle();
    } else if (e.key === 'l' || e.key === 'L') {
      if (stopwatch.isRunning) {
        stopwatch.recordLap();
      }
    } else if (e.key === 'r' || e.key === 'R') {
      if (stopwatch.elapsedTime > 0) {
        stopwatch.reset();
      }
    }
  });
}

// CommonJS export for automated unit tests
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { Stopwatch };
}
