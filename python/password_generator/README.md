# 🔐 Secure Password Generator & Entropy Analyzer

A cryptographically secure password generation and strength evaluation tool written in **Python 3**.

Unlike basic generators that rely on Python's pseudo-random `random` module, this tool uses Python's `secrets` module, providing **cryptographically secure random numbers (CSPRNG)** suitable for managing sensitive data like account credentials, security tokens, and encryption keys.

---

## 🚀 Features

- **Cryptographically Secure (CSPRNG)**: Powered by `secrets.choice()` and `secrets.randbelow()`, leveraging system-level hardware entropy (`/dev/urandom` on Unix, `CryptGenRandom` / `BCryptGenRandom` on Windows).
- **Guaranteed Category Representation**: If uppercase, lowercase, numbers, or symbols are requested, the generator guarantees that **at least one** character from every selected category is included, and then shuffles the result using a cryptographically secure Fisher-Yates algorithm.
- **Configurable Character Sets**:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Numerical digits (`0-9`)
  - Special punctuation and symbols (`!@#$%^&*...`)
  - Option to omit visually ambiguous characters (`0`, `O`, `1`, `l`, `I`, `|`).
- **Shannon Entropy Analysis**:
  Evaluates password strength mathematically using Shannon's information entropy formula:
  $$\text{Entropy (bits)} = L \times \log_2(R)$$
  where $L$ is password length and $R$ is character pool size.
- **Qualitative Strength Categorization**:
  - `< 36 bits`: Very Weak
  - `36 – 59 bits`: Weak
  - `60 – 79 bits`: Moderate
  - `80 – 109 bits`: Strong
  - `≥ 110 bits`: Very Strong

---

## 📂 Project Structure

```text
python/password_generator/
├── generator.py   # Secure generator, entropy calculator, and interactive CLI
└── README.md      # Security documentation and developer API guide
```

---

## 🖥️ How to Run

### Interactive CLI
From the repository root:
```bash
python python/password_generator/generator.py
```

You will be prompted to customize:
1. Desired length (e.g. 16, 24, 32).
2. Character inclusion options (Uppercase, Lowercase, Digits, Symbols).
3. Ambiguity filtering.

### Programmatic API Usage
The module is designed for clean integration into scripts and backend systems:

```python
from python.password_generator.generator import (
    PasswordConfig,
    generate_password,
    evaluate_password_strength,
)

# 1. Define configuration
config = PasswordConfig(
    length=20,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
)

# 2. Generate secure password
password = generate_password(config)
print(f"Generated Password: {password}")

# 3. Evaluate entropy & strength
eval_result = evaluate_password_strength(password)
print(f"Entropy: {eval_result.entropy_bits} bits")
print(f"Rating : {eval_result.rating}")
```

---

## 🧪 Testing

The generator and entropy analyzer are thoroughly verified via automated tests in `tests/test_python_projects.py`, validating:
- Exact requested length enforcement.
- Guaranteed presence of characters from each selected category.
- Error raising when length is insufficient or when zero character sets are selected.
- Entropy formula accuracy against known theoretical values.
- Strength categorization thresholds and feedback generation.
