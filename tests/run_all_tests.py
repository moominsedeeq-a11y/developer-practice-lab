"""Unified Test Runner for Developer Practice Lab.

Executes all automated verification suites across Web (Node.js),
Python (unittest), and C++ (g++ test suites).
"""

import os
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def run_command(cmd, description):
    print(f"\n>> RUNNING: {description}")
    print(f"   Command: {cmd}")
    res = subprocess.run(
        cmd, shell=True, cwd=REPO_ROOT, capture_output=True, text=True
    )
    if res.returncode == 0:
        print(f"   [PASS] {description}")
        if res.stdout.strip():
            for line in res.stdout.strip().splitlines()[-4:]:
                print(f"          {line}")
        return True
    else:
        print(f"   [FAIL] {description} (Exit code: {res.returncode})")
        print(f"   STDOUT: {res.stdout}")
        print(f"   STDERR: {res.stderr}")
        return False


def main():
    print("=" * 65)
    print("       🧪  DEVELOPER PRACTICE LAB - FULL TEST DASHBOARD  🧪    ")
    print("=" * 65)

    all_passed = True

    # 1. Web tests (Node.js)
    if not run_command("node tests/phase1_tests.js", "Web Projects Suite (Node.js)"):
        all_passed = False

    # 2. Python tests (unittest)
    if not run_command("python tests/test_python_projects.py", "Python Projects Suite (unittest)"):
        all_passed = False

    # 3. C++ Student System
    cpp_student_cmd = (
        "g++ -std=c++11 -O2 cpp/student_grading_system/main.cpp -o cpp/student_grading_system/student_system.exe "
        "&& .\\cpp\\student_grading_system\\student_system.exe --test"
    )
    if not run_command(cpp_student_cmd, "C++ Student Grading System Build & Test"):
        all_passed = False

    # 4. C++ Pattern Generator
    cpp_pattern_cmd = (
        "g++ -std=c++11 -O2 cpp/pattern_generator/patterns.cpp -o cpp/pattern_generator/patterns.exe "
        "&& .\\cpp\\pattern_generator\\patterns.exe --test"
    )
    if not run_command(cpp_pattern_cmd, "C++ Pattern Generator Build & Test"):
        all_passed = False

    print("\n" + "=" * 65)
    if all_passed:
        print(" 🎉  ALL 4 PROJECT TEST SUITES PASSED FLAWLESSLY! (100% OK)")
    else:
        print(" ❌  ONE OR MORE TEST SUITES FAILED.")
    print("=" * 65)

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
