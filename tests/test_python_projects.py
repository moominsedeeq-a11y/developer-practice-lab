"""Comprehensive Unit Test Suite for Python Lab Projects.

Tests both Number Guessing Game and Secure Password Generator
across normal conditions, invalid inputs, and boundary edge cases.
"""

import math
import os
import string
import sys
import unittest

# Ensure repo root is on python path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from python.number_guessing_game.game import (
    DIFFICULTIES,
    DifficultyLevel,
    GameRoundResult,
    GameSessionStats,
    NumberGuessingGame,
)
from python.password_generator.generator import (
    PasswordConfig,
    calculate_entropy,
    evaluate_password_strength,
    generate_password,
)


class TestNumberGuessingGame(unittest.TestCase):
    """Unit tests for the Number Guessing Game engine."""

    def setUp(self) -> None:
        self.easy_diff = DIFFICULTIES["1"]
        self.game = NumberGuessingGame(self.easy_diff, target_number=25)

    def test_initial_state(self) -> None:
        """Verifies game initializes with correct defaults."""
        self.assertEqual(self.game.min_num, 1)
        self.assertEqual(self.game.max_num, 50)
        self.assertEqual(self.game.max_attempts, 10)
        self.assertEqual(self.game.attempts_used, 0)
        self.assertFalse(self.game.is_finished)
        self.assertFalse(self.game.is_won)

    def test_validation_out_of_range(self) -> None:
        """Guards against numbers outside the permitted range."""
        valid_low, _ = self.game.validate_guess(0)
        valid_high, _ = self.game.validate_guess(51)
        self.assertFalse(valid_low)
        self.assertFalse(valid_high)

    def test_validation_duplicate_guess(self) -> None:
        """Guards against repeated guesses."""
        self.game.evaluate_guess(10)
        valid, msg = self.game.validate_guess(10)
        self.assertFalse(valid)
        self.assertIn("already guessed", msg)

    def test_evaluate_guess_directional_hints(self) -> None:
        """Tests TOO LOW and TOO HIGH directional feedback."""
        dir_low, _ = self.game.evaluate_guess(10)
        self.assertEqual(dir_low, "TOO LOW")

        dir_high, _ = self.game.evaluate_guess(40)
        self.assertEqual(dir_high, "TOO HIGH")

    def test_winning_round(self) -> None:
        """Tests that guessing target number wins the game immediately."""
        direction, msg = self.game.evaluate_guess(25)
        self.assertEqual(direction, "CORRECT")
        self.assertTrue(self.game.is_won)
        self.assertTrue(self.game.is_finished)
        self.assertEqual(self.game.attempts_used, 1)

    def test_attempt_exhaustion(self) -> None:
        """Tests that game finishes as a loss when max attempts are reached."""
        short_diff = DifficultyLevel("Test", 1, 10, 3, "Test mode")
        short_game = NumberGuessingGame(short_diff, target_number=7)

        short_game.evaluate_guess(1)
        short_game.evaluate_guess(2)
        short_game.evaluate_guess(3)

        self.assertTrue(short_game.is_finished)
        self.assertFalse(short_game.is_won)
        self.assertEqual(short_game.get_remaining_attempts(), 0)

    def test_session_statistics(self) -> None:
        """Tests win streaks, win rate, and best score across multiple rounds."""
        stats = GameSessionStats()

        # Round 1: Win with 3 attempts
        r1 = GameRoundResult(
            1, "Easy", 20, 3, 10, True, guesses=[10, 15, 20]
        )
        stats.record_round(r1)
        self.assertEqual(stats.total_played, 1)
        self.assertEqual(stats.total_won, 1)
        self.assertEqual(stats.win_rate, 100.0)
        self.assertEqual(stats.best_score, 3)
        self.assertEqual(stats.current_streak, 1)

        # Round 2: Loss
        r2 = GameRoundResult(
            2, "Hard", 100, 6, 6, False, guesses=[10, 20, 30, 40, 50, 60]
        )
        stats.record_round(r2)
        self.assertEqual(stats.total_played, 2)
        self.assertEqual(stats.total_won, 1)
        self.assertEqual(stats.win_rate, 50.0)
        self.assertEqual(stats.current_streak, 0)
        self.assertEqual(stats.best_streak, 1)


class TestPasswordGenerator(unittest.TestCase):
    """Unit tests for Secure Password Generator and Entropy Analyzer."""

    def test_exact_length_generation(self) -> None:
        """Ensures generated password matches requested length."""
        for length in (8, 16, 32, 64):
            config = PasswordConfig(length=length)
            pwd = generate_password(config)
            self.assertEqual(len(pwd), length)

    def test_guaranteed_category_presence(self) -> None:
        """Ensures every enabled character set has at least one character present."""
        config = PasswordConfig(
            length=16,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_symbols=True,
        )

        for _ in range(25):  # Sample 25 independent runs
            pwd = generate_password(config)
            has_upper = any(c in string.ascii_uppercase for c in pwd)
            has_lower = any(c in string.ascii_lowercase for c in pwd)
            has_digit = any(c in string.digits for c in pwd)
            has_symbol = any(c in config.custom_symbols for c in pwd)

            self.assertTrue(has_upper, f"Missing uppercase in {pwd}")
            self.assertTrue(has_lower, f"Missing lowercase in {pwd}")
            self.assertTrue(has_digit, f"Missing digit in {pwd}")
            self.assertTrue(has_symbol, f"Missing symbol in {pwd}")

    def test_digits_only_configuration(self) -> None:
        """Verifies PIN-style generation with digits only."""
        config = PasswordConfig(
            length=6,
            use_uppercase=False,
            use_lowercase=False,
            use_digits=True,
            use_symbols=False,
        )
        pwd = generate_password(config)
        self.assertEqual(len(pwd), 6)
        self.assertTrue(pwd.isdigit())

    def test_ambiguous_character_filtering(self) -> None:
        """Ensures ambiguous characters are excluded when flag is enabled."""
        config = PasswordConfig(
            length=40,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_symbols=False,
            exclude_ambiguous=True,
        )
        ambiguous_chars = set("1lIO0")
        for _ in range(10):
            pwd = generate_password(config)
            self.assertTrue(ambiguous_chars.isdisjoint(set(pwd)))

    def test_validation_errors(self) -> None:
        """Tests that ValueError is raised on invalid configurations."""
        # Length too short for 4 categories
        with self.assertRaises(ValueError):
            generate_password(PasswordConfig(length=3))

        # No categories selected
        with self.assertRaises(ValueError):
            generate_password(
                PasswordConfig(
                    length=10,
                    use_uppercase=False,
                    use_lowercase=False,
                    use_digits=False,
                    use_symbols=False,
                )
            )

    def test_shannon_entropy_calculation(self) -> None:
        """Validates information entropy formula."""
        # 10 characters from pool of 2 (binary): 10 * log2(2) = 10 bits
        self.assertAlmostEqual(calculate_entropy(10, 2), 10.0, places=2)
        # 16 characters from pool of 94: 16 * log2(94) ≈ 104.87 bits
        expected_94 = 16 * math.log2(94)
        self.assertAlmostEqual(calculate_entropy(16, 94), expected_94, places=2)

    def test_strength_evaluation_ratings(self) -> None:
        """Tests strength categorizations across various passwords."""
        # Empty
        eval_empty = evaluate_password_strength("")
        self.assertEqual(eval_empty.rating, "Empty")

        # Very Weak (short, single character class)
        eval_weak = evaluate_password_strength("cat")
        self.assertEqual(eval_weak.rating, "Very Weak")

        # Strong / Very Strong (long, diverse character classes)
        strong_pwd = "P@ssw0rd!#2026_SecureKey"
        eval_strong = evaluate_password_strength(strong_pwd)
        self.assertIn(eval_strong.rating, ("Strong", "Very Strong"))
        self.assertGreater(eval_strong.entropy_bits, 80.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
