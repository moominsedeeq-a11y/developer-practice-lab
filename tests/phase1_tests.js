/**
 * Automated Verification Suite for Phase 1
 * Validates Calculator mathematical accuracy and Stopwatch timing logic.
 */

const assert = require('assert');
const { Calculator } = require('../web/calculator/app.js');
const { Stopwatch } = require('../web/stopwatch/app.js');

let passedTests = 0;
let totalTests = 0;

function runTest(testName, fn) {
  totalTests++;
  try {
    fn();
    console.log(`  [PASS] ${testName}`);
    passedTests++;
  } catch (err) {
    console.error(`  [FAIL] ${testName}`);
    console.error(`         ${err.message}`);
  }
}

console.log('====================================================');
console.log(' RUNNING PHASE 1 TEST SUITE (Calculator & Stopwatch)');
console.log('====================================================\n');

console.log('--- 1. CALCULATOR TESTS ---');

runTest('Initial state is clean', () => {
  const calc = new Calculator();
  assert.strictEqual(calc.currentOperand, '0');
  assert.strictEqual(calc.previousOperand, '');
  assert.strictEqual(calc.operation, undefined);
  assert.strictEqual(calc.isErrorState, false);
});

runTest('Appends digits and ignores leading redundant zeros', () => {
  const calc = new Calculator();
  calc.appendNumber('0');
  assert.strictEqual(calc.currentOperand, '0');
  calc.appendNumber('7');
  assert.strictEqual(calc.currentOperand, '7');
  calc.appendNumber('5');
  assert.strictEqual(calc.currentOperand, '75');
});

runTest('Prevents multiple decimal points', () => {
  const calc = new Calculator();
  calc.appendNumber('3');
  calc.appendNumber('.');
  calc.appendNumber('1');
  calc.appendNumber('.');
  calc.appendNumber('4');
  assert.strictEqual(calc.currentOperand, '3.14');
});

runTest('Performs addition correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('15');
  calc.chooseOperation('+');
  calc.appendNumber('27');
  calc.compute();
  assert.strictEqual(calc.currentOperand, '42');
});

runTest('Solves floating point addition accurately (0.1 + 0.2 = 0.3)', () => {
  const calc = new Calculator();
  calc.appendNumber('0.1');
  calc.chooseOperation('+');
  calc.appendNumber('0.2');
  calc.compute();
  assert.strictEqual(calc.currentOperand, '0.3');
});

runTest('Performs subtraction correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('100');
  calc.chooseOperation('-');
  calc.appendNumber('35.5');
  calc.compute();
  assert.strictEqual(calc.currentOperand, '64.5');
});

runTest('Performs multiplication correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('6');
  calc.chooseOperation('×');
  calc.appendNumber('7');
  calc.compute();
  assert.strictEqual(calc.currentOperand, '42');
});

runTest('Performs division correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('84');
  calc.chooseOperation('÷');
  calc.appendNumber('4');
  calc.compute();
  assert.strictEqual(calc.currentOperand, '21');
});

runTest('Handles division by zero safely', () => {
  const calc = new Calculator();
  calc.appendNumber('50');
  calc.chooseOperation('÷');
  calc.appendNumber('0');
  calc.compute();
  assert.strictEqual(calc.currentOperand, 'Cannot divide by 0');
  assert.strictEqual(calc.isErrorState, true);

  // Verifies safe recovery upon next number entry
  calc.appendNumber('9');
  assert.strictEqual(calc.currentOperand, '9');
  assert.strictEqual(calc.isErrorState, false);
});

runTest('Toggles sign (negation) correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('42');
  calc.toggleSign();
  assert.strictEqual(calc.currentOperand, '-42');
  calc.toggleSign();
  assert.strictEqual(calc.currentOperand, '42');
});

runTest('Calculates percentage correctly', () => {
  const calc = new Calculator();
  calc.appendNumber('75');
  calc.applyPercent();
  assert.strictEqual(calc.currentOperand, '0.75');
});

runTest('Deletes single characters and recovers to zero', () => {
  const calc = new Calculator();
  calc.appendNumber('9');
  calc.appendNumber('8');
  calc.appendNumber('7');
  calc.delete();
  assert.strictEqual(calc.currentOperand, '98');
  calc.delete();
  assert.strictEqual(calc.currentOperand, '9');
  calc.delete();
  assert.strictEqual(calc.currentOperand, '0');
});

runTest('Formats numbers with comma thousand separators', () => {
  const calc = new Calculator();
  assert.strictEqual(calc.getDisplayNumber('1234567.89'), '1,234,567.89');
  assert.strictEqual(calc.getDisplayNumber('1000'), '1,000');
  assert.strictEqual(calc.getDisplayNumber('0'), '0');
});

console.log('\n--- 2. STOPWATCH TESTS ---');

runTest('Formats time components with zero padding', () => {
  assert.strictEqual(Stopwatch.formatTime(0).formatted, '00:00:00.000');
  assert.strictEqual(Stopwatch.formatTime(1000).formatted, '00:00:01.000');
  assert.strictEqual(Stopwatch.formatTime(65432).formatted, '00:01:05.432');
  assert.strictEqual(Stopwatch.formatTime(3661042).formatted, '01:01:01.042');
});

runTest('Calculates consecutive lap durations accurately', () => {
  const sw = new Stopwatch();
  sw.isRunning = true;

  sw.elapsedTime = 2000;
  const lap1 = sw.recordLap();
  assert.strictEqual(lap1.lapNumber, 1);
  assert.strictEqual(lap1.lapDuration, 2000);
  assert.strictEqual(lap1.totalTime, 2000);

  sw.elapsedTime = 5500;
  const lap2 = sw.recordLap();
  assert.strictEqual(lap2.lapNumber, 2);
  assert.strictEqual(lap2.lapDuration, 3500);
  assert.strictEqual(lap2.totalTime, 5500);

  sw.elapsedTime = 7000;
  const lap3 = sw.recordLap();
  assert.strictEqual(lap3.lapNumber, 3);
  assert.strictEqual(lap3.lapDuration, 1500);
  assert.strictEqual(lap3.totalTime, 7000);
});

runTest('Detects fastest and slowest lap splits', () => {
  const sw = new Stopwatch();
  sw.isRunning = true;

  sw.elapsedTime = 2000;
  sw.recordLap(); // 2000ms

  sw.elapsedTime = 6000;
  sw.recordLap(); // 4000ms (slowest)

  sw.elapsedTime = 7000;
  sw.recordLap(); // 1000ms (fastest)

  const extremes = sw.getLapExtremes();
  assert.strictEqual(extremes.fastestId, 3);
  assert.strictEqual(extremes.slowestId, 2);
});

runTest('Resets stopwatch state and clears recorded laps', () => {
  const sw = new Stopwatch();
  sw.isRunning = true;
  sw.elapsedTime = 5000;
  sw.recordLap();
  assert.strictEqual(sw.laps.length, 1);

  sw.reset();
  assert.strictEqual(sw.isRunning, false);
  assert.strictEqual(sw.elapsedTime, 0);
  assert.strictEqual(sw.laps.length, 0);
});

console.log('\n====================================================');
console.log(` SUMMARY: ${passedTests} / ${totalTests} tests passed.`);
console.log('====================================================');

if (passedTests !== totalTests) {
  process.exit(1);
}
