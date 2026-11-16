/**
 * Personal Calculator Engine
 * Implements standard arithmetic operations, state management,
 * keyboard shortcuts, and floating-point precision guards.
 */

class Calculator {
  constructor(previousOperandElement, currentOperandElement) {
    this.previousOperandElement = previousOperandElement;
    this.currentOperandElement = currentOperandElement;
    this.clear();
  }

  /**
   * Resets calculator state to defaults
   */
  clear() {
    this.currentOperand = '0';
    this.previousOperand = '';
    this.operation = undefined;
    this.isErrorState = false;
  }

  /**
   * Removes the last entered character from the current operand
   */
  delete() {
    if (this.isErrorState) {
      this.clear();
      return;
    }
    if (this.currentOperand === '0') return;
    if (this.currentOperand.length === 1 || (this.currentOperand.length === 2 && this.currentOperand.startsWith('-'))) {
      this.currentOperand = '0';
    } else {
      this.currentOperand = this.currentOperand.slice(0, -1);
    }
  }

  /**
   * Appends a number or decimal point to the current operand
   * @param {string} number 
   */
  appendNumber(number) {
    if (this.isErrorState) {
      this.clear();
    }
    // Prevent multiple decimals
    if (number === '.' && this.currentOperand.includes('.')) return;
    // Replace standalone 0 unless appending decimal
    if (this.currentOperand === '0' && number !== '.') {
      this.currentOperand = number.toString();
    } else {
      this.currentOperand = this.currentOperand.toString() + number.toString();
    }
  }

  /**
   * Toggles positive/negative sign of current operand
   */
  toggleSign() {
    if (this.isErrorState || this.currentOperand === '0') return;
    if (this.currentOperand.startsWith('-')) {
      this.currentOperand = this.currentOperand.substring(1);
    } else {
      this.currentOperand = '-' + this.currentOperand;
    }
  }

  /**
   * Converts current operand to percentage
   */
  applyPercent() {
    if (this.isErrorState) return;
    const current = parseFloat(this.currentOperand);
    if (isNaN(current)) return;
    // High-precision division by 100
    this.currentOperand = (current / 100).toString();
  }

  /**
   * Selects an arithmetic operator (+, -, ×, ÷)
   * @param {string} operation 
   */
  chooseOperation(operation) {
    if (this.isErrorState) this.clear();
    if (this.currentOperand === '' && this.previousOperand === '') return;

    // Allow changing operator if no new number entered
    if (this.currentOperand === '' && this.previousOperand !== '') {
      this.operation = operation;
      return;
    }

    if (this.previousOperand !== '') {
      this.compute();
      if (this.isErrorState) return;
    }

    this.operation = operation;
    this.previousOperand = this.currentOperand;
    this.currentOperand = '';
  }

  /**
   * Computes the mathematical result of previousOperand and currentOperand
   */
  compute() {
    if (this.operation == null || this.previousOperand === '' || this.currentOperand === '') {
      return;
    }

    const prev = parseFloat(this.previousOperand);
    const current = parseFloat(this.currentOperand);

    if (isNaN(prev) || isNaN(current)) {
      return;
    }

    let computation;
    switch (this.operation) {
      case '+':
        computation = prev + current;
        break;
      case '-':
        computation = prev - current;
        break;
      case '×':
      case '*':
        computation = prev * current;
        break;
      case '÷':
      case '/':
        if (current === 0) {
          this.currentOperand = 'Cannot divide by 0';
          this.previousOperand = '';
          this.operation = undefined;
          this.isErrorState = true;
          return;
        }
        computation = prev / current;
        break;
      default:
        return;
    }

    // Fix floating point inaccuracies (e.g., 0.1 + 0.2 = 0.3)
    const rounded = Math.round((computation + Number.EPSILON) * 1e12) / 1e12;
    this.currentOperand = rounded.toString();
    this.operation = undefined;
    this.previousOperand = '';
  }

  /**
   * Formats numbers with comma thousands-separators while keeping decimals intact
   * @param {string|number} numberStr 
   * @returns {string}
   */
  getDisplayNumber(numberStr) {
    if (!numberStr && numberStr !== 0) return '';
    const stringNumber = numberStr.toString();
    if (this.isErrorState) return stringNumber;

    const [integerDigits, decimalDigits] = stringNumber.split('.');
    const integerNumber = parseFloat(integerDigits);
    let integerDisplay = '';

    if (isNaN(integerNumber)) {
      integerDisplay = '';
    } else {
      integerDisplay = integerNumber.toLocaleString('en-US', {
        maximumFractionDigits: 0
      });
    }

    if (decimalDigits != null) {
      return `${integerDisplay}.${decimalDigits}`;
    }
    return integerDisplay;
  }

  /**
   * Updates display elements in the DOM
   */
  updateDisplay() {
    if (this.currentOperandElement) {
      if (this.isErrorState) {
        this.currentOperandElement.innerText = this.currentOperand;
      } else {
        this.currentOperandElement.innerText = this.getDisplayNumber(this.currentOperand);
      }
    }

    if (this.previousOperandElement) {
      if (this.operation != null && this.previousOperand !== '') {
        this.previousOperandElement.innerText = `${this.getDisplayNumber(this.previousOperand)} ${this.operation}`;
      } else {
        this.previousOperandElement.innerText = '';
      }
    }
  }
}

// Browser Initialization
if (typeof window !== 'undefined' && typeof document !== 'undefined') {
  const previousOperandElement = document.getElementById('previousOperand');
  const currentOperandElement = document.getElementById('currentOperand');
  const calculator = new Calculator(previousOperandElement, currentOperandElement);

  // Click Event Listeners
  document.querySelectorAll('[data-number]').forEach(button => {
    button.addEventListener('click', () => {
      calculator.appendNumber(button.getAttribute('data-number'));
      calculator.updateDisplay();
    });
  });

  document.querySelectorAll('[data-operator]').forEach(button => {
    button.addEventListener('click', () => {
      calculator.chooseOperation(button.getAttribute('data-operator'));
      calculator.updateDisplay();
    });
  });

  document.querySelector('[data-action="calculate"]')?.addEventListener('click', () => {
    calculator.compute();
    calculator.updateDisplay();
  });

  document.querySelector('[data-action="all-clear"]')?.addEventListener('click', () => {
    calculator.clear();
    calculator.updateDisplay();
  });

  document.querySelector('[data-action="delete"]')?.addEventListener('click', () => {
    calculator.delete();
    calculator.updateDisplay();
  });

  document.querySelector('[data-action="negate"]')?.addEventListener('click', () => {
    calculator.toggleSign();
    calculator.updateDisplay();
  });

  document.querySelector('[data-action="percent"]')?.addEventListener('click', () => {
    calculator.applyPercent();
    calculator.updateDisplay();
  });

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    if ((e.key >= '0' && e.key <= '9') || e.key === '.') {
      calculator.appendNumber(e.key);
      calculator.updateDisplay();
    } else if (e.key === '+') {
      calculator.chooseOperation('+');
      calculator.updateDisplay();
    } else if (e.key === '-') {
      calculator.chooseOperation('-');
      calculator.updateDisplay();
    } else if (e.key === '*') {
      calculator.chooseOperation('×');
      calculator.updateDisplay();
    } else if (e.key === '/') {
      e.preventDefault(); // Prevent Firefox quick find
      calculator.chooseOperation('÷');
      calculator.updateDisplay();
    } else if (e.key === 'Enter' || e.key === '=') {
      e.preventDefault();
      calculator.compute();
      calculator.updateDisplay();
    } else if (e.key === 'Backspace') {
      calculator.delete();
      calculator.updateDisplay();
    } else if (e.key === 'Escape') {
      calculator.clear();
      calculator.updateDisplay();
    } else if (e.key === '%') {
      calculator.applyPercent();
      calculator.updateDisplay();
    }
  });
}

// CommonJS export for automated testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { Calculator };
}
