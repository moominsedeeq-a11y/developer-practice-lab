"""Cryptographically Secure Password Generator & Entropy Analyzer.

Demonstrates secure pseudo-random number generation (secrets module),
customizable character sets, guaranteed character category inclusion,
Shannon entropy calculation, and password strength evaluation.
"""

from dataclasses import dataclass
import math
import secrets
import string
import sys
from typing import Dict, List, Optional, Tuple


@dataclass
class PasswordConfig:
    """Configuration options for password generation."""

    length: int = 16
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    custom_symbols: str = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    exclude_ambiguous: bool = False  # e.g., l, 1, I, O, 0


@dataclass
class StrengthEvaluation:
    """Detailed password strength and entropy evaluation."""

    score: int  # 0 to 4
    rating: str  # Very Weak, Weak, Moderate, Strong, Very Strong
    entropy_bits: float
    pool_size: int
    feedback: List[str]


def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculates password entropy in bits: E = L * log2(R).

    Args:
        length: Number of characters in password.
        pool_size: Total count of unique possible characters.

    Returns:
        Entropy in bits.
    """
    if length <= 0 or pool_size <= 0:
        return 0.0
    return length * math.log2(pool_size)


def evaluate_password_strength(password: str) -> StrengthEvaluation:
    """Evaluates the strength of any given password based on entropy,

    character diversity, and length.
    """
    if not password:
        return StrengthEvaluation(
            score=0,
            rating="Empty",
            entropy_bits=0.0,
            pool_size=0,
            feedback=["Password cannot be empty."],
        )

    length = len(password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    # Calculate character pool size based on character variety
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_symbol:
        pool_size += 32

    # Fallback for custom or unique unicode characters
    pool_size = max(pool_size, len(set(password)))

    entropy = calculate_entropy(length, pool_size)
    feedback: List[str] = []

    if length < 8:
        feedback.append("Critically short: length should be at least 12 characters.")
    elif length < 12:
        feedback.append("Moderate length: consider 14+ characters for high security.")

    if not (has_lower and has_upper):
        feedback.append("Mix uppercase and lowercase letters.")
    if not has_digit:
        feedback.append("Include numerical digits (0-9).")
    if not has_symbol:
        feedback.append("Include special symbols (e.g., !, @, #, $).")

    # Determine qualitative rating
    if entropy < 36 or length < 8:
        score = 0
        rating = "Very Weak"
    elif entropy < 60 or length < 10:
        score = 1
        rating = "Weak"
    elif entropy < 80:
        score = 2
        rating = "Moderate"
    elif entropy < 110:
        score = 3
        rating = "Strong"
    else:
        score = 4
        rating = "Very Strong"

    if not feedback:
        feedback.append("Excellent combination of length and character diversity.")

    return StrengthEvaluation(
        score=score,
        rating=rating,
        entropy_bits=round(entropy, 2),
        pool_size=pool_size,
        feedback=feedback,
    )


def generate_password(config: PasswordConfig) -> str:
    """Generates a cryptographically secure random password based on config.

    Guarantees at least one character from each enabled character set.

    Raises:
        ValueError: If length is less than number of selected sets or if no sets selected.
    """
    if config.length <= 0:
        raise ValueError("Password length must be a positive integer.")

    char_pools: List[str] = []

    if config.use_lowercase:
        chars = string.ascii_lowercase
        if config.exclude_ambiguous:
            chars = chars.replace("l", "").replace("o", "")
        char_pools.append(chars)

    if config.use_uppercase:
        chars = string.ascii_uppercase
        if config.exclude_ambiguous:
            chars = chars.replace("I", "").replace("O", "")
        char_pools.append(chars)

    if config.use_digits:
        chars = string.digits
        if config.exclude_ambiguous:
            chars = chars.replace("0", "").replace("1", "")
        char_pools.append(chars)

    if config.use_symbols:
        symbols = config.custom_symbols
        if config.exclude_ambiguous:
            for amb in ("|", "'", '"', "`"):
                symbols = symbols.replace(amb, "")
        char_pools.append(symbols)

    if not char_pools:
        raise ValueError("At least one character category must be enabled.")

    if config.length < len(char_pools):
        raise ValueError(
            f"Requested length ({config.length}) is too short to include at least "
            f"one character from each of the {len(char_pools)} selected categories."
        )

    # Guarantee at least one character from each active pool
    password_chars: List[str] = [
        secrets.choice(pool) for pool in char_pools
    ]

    # Combine all allowed characters for the remaining slots
    combined_pool = "".join(char_pools)
    remaining_length = config.length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(secrets.choice(combined_pool))

    # Cryptographically secure shuffle of character array using Fisher-Yates
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


# =====================================================================
# Terminal CLI Interface
# =====================================================================


def print_cli_banner() -> None:
    """Displays CLI tool banner."""
    print("=" * 65)
    print("      🔐  SECURE PASSWORD GENERATOR & ENTROPY ANALYZER  🔐     ")
    print("=" * 65)
    print("Powered by Python's 'secrets' module (Cryptographic CSPRNG)\n")


def prompt_boolean(prompt_text: str, default: bool = True) -> bool:
    """Prompts the user for a yes/no boolean choice."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        choice = input(prompt_text + suffix).strip().lower()
        if not choice:
            return default
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def prompt_password_length() -> int:
    """Prompts user for desired password length with validation."""
    while True:
        val = input("Enter password length (recommended 12 - 64) [16]: ").strip()
        if not val:
            return 16
        try:
            length = int(val)
            if length < 4:
                print("Minimum recommended length is 4. Please enter 4 or higher.")
                continue
            if length > 256:
                print("Maximum supported length is 256.")
                continue
            return length
        except ValueError:
            print("Please enter a valid whole number.")


def run_interactive_generator() -> None:
    """Runs interactive generator menu."""
    print_cli_banner()

    while True:
        length = prompt_password_length()
        use_upper = prompt_boolean("Include Uppercase Letters (A-Z)?", True)
        use_lower = prompt_boolean("Include Lowercase Letters (a-z)?", True)
        use_digits = prompt_boolean("Include Numbers (0-9)?", True)
        use_symbols = prompt_boolean("Include Symbols (!@#$%...)?", True)
        exclude_ambig = prompt_boolean(
            "Exclude ambiguous characters (e.g. 0/O, 1/l/I)?", False
        )

        config = PasswordConfig(
            length=length,
            use_uppercase=use_upper,
            use_lowercase=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_ambiguous=exclude_ambig,
        )

        try:
            password = generate_password(config)
            evaluation = evaluate_password_strength(password)

            print("\n" + "-" * 65)
            print("🔑 GENERATED PASSWORD:")
            print(f"   {password}")
            print("-" * 65)
            print(f"Length         : {len(password)} characters")
            print(f"Character Pool : {evaluation.pool_size} unique symbols")
            print(f"Entropy Score  : {evaluation.entropy_bits} bits")
            print(f"Strength Rating: {evaluation.rating}")
            print("Recommendations:")
            for note in evaluation.feedback:
                print(f"   • {note}")
            print("-" * 65 + "\n")

        except ValueError as err:
            print(f"⚠️  Error: {err}\n")

        again = prompt_boolean("Generate another password?", True)
        if not again:
            print("\nStay secure! Use strong, unique passwords.")
            break
        print("\n")


if __name__ == "__main__":
    run_interactive_generator()
