"""Number Guessing Game.

A feature-rich terminal game demonstrating clean Python architecture, input
validation, session statistics, customizable difficulty tiers, and proximity
hints.
"""

from dataclasses import dataclass, field
import random
import sys
from typing import Dict, List, Optional, Tuple


@dataclass
class DifficultyLevel:
    """Represents a game difficulty configuration."""

    name: str
    min_num: int
    max_num: int
    max_attempts: int
    description: str


# Preset difficulty configurations
DIFFICULTIES: Dict[str, DifficultyLevel] = {
    "1": DifficultyLevel(
        "Easy", 1, 50, 10, "Range: 1 - 50 | 10 attempts (Beginner friendly)"
    ),
    "2": DifficultyLevel(
        "Medium", 1, 100, 7, "Range: 1 - 100 | 7 attempts (Standard challenge)"
    ),
    "3": DifficultyLevel(
        "Hard", 1, 250, 6, "Range: 1 - 250 | 6 attempts (Advanced players)"
    ),
    "4": DifficultyLevel(
        "Expert", 1, 500, 5, "Range: 1 - 500 | 5 attempts (Precision master)"
    ),
}


@dataclass
class GameRoundResult:
    """Stores the outcome of a single game round."""

    round_number: int
    difficulty_name: str
    target_number: int
    attempts_used: int
    max_attempts: int
    won: bool
    guesses: List[int] = field(default_factory=list)


class GameSessionStats:
    """Tracks cumulative session statistics across multiple rounds."""

    def __init__(self) -> None:
        self.rounds: List[GameRoundResult] = []
        self.current_streak: int = 0
        self.best_streak: int = 0

    def record_round(self, result: GameRoundResult) -> None:
        """Records a completed round and updates streaks."""
        self.rounds.append(result)
        if result.won:
            self.current_streak += 1
            if self.current_streak > self.best_streak:
                self.best_streak = self.current_streak
        else:
            self.current_streak = 0

    @property
    def total_played(self) -> int:
        return len(self.rounds)

    @property
    def total_won(self) -> int:
        return sum(1 for r in self.rounds if r.won)

    @property
    def win_rate(self) -> float:
        if not self.total_played:
            return 0.0
        return (self.total_won / self.total_played) * 100.0

    @property
    def best_score(self) -> Optional[int]:
        """Returns the fewest attempts used in any winning round."""
        winning_attempts = [r.attempts_used for r in self.rounds if r.won]
        return min(winning_attempts) if winning_attempts else None


class NumberGuessingGame:
    """Core game engine managing a single game round."""

    def __init__(
        self,
        difficulty: DifficultyLevel,
        target_number: Optional[int] = None,
    ) -> None:
        self.difficulty = difficulty
        self.min_num = difficulty.min_num
        self.max_num = difficulty.max_num
        self.max_attempts = difficulty.max_attempts

        # Target can be injected for deterministic unit testing
        if target_number is not None:
            self.target_number = target_number
        else:
            self.target_number = random.randint(self.min_num, self.max_num)

        self.guesses: List[int] = []
        self.attempts_used: int = 0
        self.is_finished: bool = False
        self.is_won: bool = False

    def validate_guess(self, guess: int) -> Tuple[bool, str]:
        """Validates if a guess is within range and not previously attempted.

        Returns (is_valid, message).
        """
        if guess < self.min_num or guess > self.max_num:
            return (
                False,
                f"Out of range! Please guess a number between {self.min_num} and {self.max_num}.",
            )
        if guess in self.guesses:
            return (
                False,
                f"You already guessed {guess}! Try a different number.",
            )
        return (True, "")

    def evaluate_guess(self, guess: int) -> Tuple[str, str]:
        """Evaluates a valid guess.

        Returns (direction_hint, proximity_hint).
        """
        self.guesses.append(guess)
        self.attempts_used += 1

        if guess == self.target_number:
            self.is_finished = True
            self.is_won = True
            return ("CORRECT", "Spot on! You found the secret number.")

        if self.attempts_used >= self.max_attempts:
            self.is_finished = True
            self.is_won = False

        diff = abs(guess - self.target_number)
        total_range = self.max_num - self.min_num + 1

        # Directional feedback
        direction = "TOO LOW" if guess < self.target_number else "TOO HIGH"

        # Proximity feedback based on percentage of range
        if diff <= max(2, int(total_range * 0.03)):
            proximity = "Burning hot! (Extremely close)"
        elif diff <= max(5, int(total_range * 0.10)):
            proximity = "Warm (Getting closer)"
        elif diff <= max(12, int(total_range * 0.25)):
            proximity = "Lukewarm"
        else:
            proximity = "Cold"

        return (direction, proximity)

    def get_remaining_attempts(self) -> int:
        """Returns the number of attempts left."""
        return max(0, self.max_attempts - self.attempts_used)


# =====================================================================
# Terminal UI & Interactive Flow
# =====================================================================


def print_banner() -> None:
    """Prints game title banner."""
    print("=" * 60)
    print("       🎯  NUMBER GUESSING GAME - PYTHON LAB  🎯       ")
    print("=" * 60)
    print("Test your deductive reasoning and find the secret number!\n")


def display_difficulty_menu() -> None:
    """Displays the difficulty selection options."""
    print("Select Difficulty Level:")
    for key, diff in DIFFICULTIES.items():
        print(f"  [{key}] {diff.name:<8} : {diff.description}")
    print(
        "  [5] Custom   : Configure your own range and attempt limit\n"
    )


def prompt_custom_difficulty() -> DifficultyLevel:
    """Prompts user to configure a custom difficulty."""
    while True:
        try:
            min_val = int(input("Enter minimum number (e.g., 1): ").strip())
            max_val = int(input("Enter maximum number (e.g., 200): ").strip())
            if max_val <= min_val:
                print("Error: Maximum must be greater than minimum. Try again.")
                continue
            attempts = int(
                input("Enter maximum attempts allowed (1 - 50): ").strip()
            )
            if attempts < 1 or attempts > 50:
                print("Error: Attempts must be between 1 and 50.")
                continue
            return DifficultyLevel(
                name="Custom",
                min_num=min_val,
                max_num=max_val,
                max_attempts=attempts,
                description=f"Range: {min_val} - {max_val} | {attempts} attempts",
            )
        except ValueError:
            print("Invalid input. Please enter whole numbers.")


def select_difficulty() -> DifficultyLevel:
    """Handles difficulty selection input."""
    while True:
        display_difficulty_menu()
        choice = input("Enter choice (1-5): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        if choice == "5":
            return prompt_custom_difficulty()
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.\n")


def play_round(
    difficulty: DifficultyLevel, round_num: int
) -> GameRoundResult:
    """Plays a single round of the game."""
    game = NumberGuessingGame(difficulty)
    print("-" * 60)
    print(f"▶ ROUND {round_num}: {difficulty.name} Mode")
    print(
        f"I have picked a number between {game.min_num} and {game.max_num}."
    )
    print(f"You have {game.max_attempts} attempts. Good luck!\n")

    while not game.is_finished:
        remaining = game.get_remaining_attempts()
        print(
            f"Attempt {game.attempts_used + 1}/{game.max_attempts} (Remaining: {remaining})"
        )

        raw_input = input("Enter your guess: ").strip()

        # Input validation
        try:
            guess = int(raw_input)
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid integer.\n")
            continue

        is_valid, error_msg = game.validate_guess(guess)
        if not is_valid:
            print(f"⚠️  {error_msg}\n")
            continue

        direction, proximity = game.evaluate_guess(guess)

        if direction == "CORRECT":
            print(f"\n🎉 {proximity}")
            print(
                f"You solved it in {game.attempts_used} attempt(s)!\n"
            )
            break
        else:
            print(f"👉 {direction}! [{proximity}]")
            if game.is_finished:
                print(
                    f"\n💥 Game Over! You've used all {game.max_attempts} attempts."
                )
                print(f"The secret number was: {game.target_number}\n")
            else:
                print(f"Guesses so far: {game.guesses}\n")

    return GameRoundResult(
        round_number=round_num,
        difficulty_name=difficulty.name,
        target_number=game.target_number,
        attempts_used=game.attempts_used,
        max_attempts=game.max_attempts,
        won=game.is_won,
        guesses=game.guesses,
    )


def display_session_stats(stats: GameSessionStats) -> None:
    """Displays cumulative stats table."""
    print("\n" + "=" * 60)
    print("                📊  SESSION STATISTICS  📊              ")
    print("=" * 60)
    print(f"Total Games Played : {stats.total_played}")
    print(f"Total Victories    : {stats.total_won}")
    print(f"Win Rate           : {stats.win_rate:.1f}%")
    best = stats.best_score if stats.best_score is not None else "N/A"
    print(f"Best Win Score     : {best} attempts")
    print(f"Current Win Streak : {stats.current_streak}")
    print(f"Highest Win Streak : {stats.best_streak}")
    print("=" * 60 + "\n")


def main() -> None:
    """Main application loop."""
    print_banner()
    stats = GameSessionStats()
    round_count = 1

    while True:
        difficulty = select_difficulty()
        result = play_round(difficulty, round_count)
        stats.record_round(result)
        display_session_stats(stats)

        # Replay prompt
        again = (
            input("Would you like to play another round? (y/n): ")
            .strip()
            .lower()
        )
        if again not in ("y", "yes"):
            print("\nThank you for playing! Keep practicing your problem-solving.")
            break
        round_count += 1
        print("\n")


if __name__ == "__main__":
    main()
