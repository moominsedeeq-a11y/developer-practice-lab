/**
 * Algorithmic Number Pattern Generator
 * A menu-driven C++ application demonstrating nested loops, algorithmic
 * symmetry, dynamic combinatorial calculations, and formatted terminal output.
 */

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <limits>

/**
 * 1. Symmetric Palindrome Number Pyramid
 * Example for rows = 4:
 *          1
 *        1 2 1
 *      1 2 3 2 1
 *    1 2 3 4 3 2 1
 */
void generatePyramid(int rows, std::ostream& out) {
    out << "\n--- Palindromic Number Pyramid (" << rows << " rows) ---\n\n";
    for (int i = 1; i <= rows; ++i) {
        // Leading spaces for centering
        for (int s = 0; s < (rows - i) * 2; ++s) {
            out << " ";
        }
        // Ascending sequence
        for (int j = 1; j <= i; ++j) {
            out << j << " ";
        }
        // Descending sequence
        for (int j = i - 1; j >= 1; --j) {
            out << j << " ";
        }
        out << "\n";
    }
    out << "\n";
}

/**
 * 2. Inverted Symmetric Number Pyramid
 * Example for rows = 4:
 *    1 2 3 4 3 2 1
 *      1 2 3 2 1
 *        1 2 1
 *          1
 */
void generateInvertedPyramid(int rows, std::ostream& out) {
    out << "\n--- Inverted Number Pyramid (" << rows << " rows) ---\n\n";
    for (int i = rows; i >= 1; --i) {
        // Leading spaces
        for (int s = 0; s < (rows - i) * 2; ++s) {
            out << " ";
        }
        // Ascending
        for (int j = 1; j <= i; ++j) {
            out << j << " ";
        }
        // Descending
        for (int j = i - 1; j >= 1; --j) {
            out << j << " ";
        }
        out << "\n";
    }
    out << "\n";
}

/**
 * 3. Symmetric Number Diamond Pattern
 * Combines upper pyramid and lower inverted pyramid.
 */
void generateDiamond(int rows, std::ostream& out) {
    out << "\n--- Symmetric Number Diamond (" << rows << " radius rows) ---\n\n";
    // Upper half (including center row)
    for (int i = 1; i <= rows; ++i) {
        for (int s = 0; s < (rows - i) * 2; ++s) out << " ";
        for (int j = 1; j <= i; ++j) out << j << " ";
        for (int j = i - 1; j >= 1; --j) out << j << " ";
        out << "\n";
    }
    // Lower half
    for (int i = rows - 1; i >= 1; --i) {
        for (int s = 0; s < (rows - i) * 2; ++s) out << " ";
        for (int j = 1; j <= i; ++j) out << j << " ";
        for (int j = i - 1; j >= 1; --j) out << j << " ";
        out << "\n";
    }
    out << "\n";
}

/**
 * 4. Floyd's Triangle
 * Consecutive natural numbers placed in right-triangular matrix:
 * 1
 * 2  3
 * 4  5  6
 * 7  8  9  10
 */
void generateFloydsTriangle(int rows, std::ostream& out) {
    out << "\n--- Floyd's Triangle (" << rows << " rows) ---\n\n";
    int currentNum = 1;
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) {
            out << std::setw(4) << currentNum++ << " ";
        }
        out << "\n";
    }
    out << "\n";
}

/**
 * 5. Pascal's Triangle
 * Mathematical triangle where each entry is the binomial coefficient:
 * C(n, k) = C(n, k-1) * (n - k + 1) / k
 * Example for rows = 5:
 *             1
 *           1   1
 *         1   2   1
 *       1   3   3   1
 *     1   4   6   4   1
 */
void generatePascalsTriangle(int rows, std::ostream& out) {
    out << "\n--- Pascal's Triangle (" << rows << " rows) ---\n\n";
    for (int i = 0; i < rows; ++i) {
        // Leading space for isosceles centering
        for (int s = 0; s < (rows - i - 1) * 3; ++s) {
            out << " ";
        }

        long long val = 1;
        for (int j = 0; j <= i; ++j) {
            out << std::setw(6) << val;
            // Incremental combination calculation: val * (i - j) / (j + 1)
            val = val * (i - j) / (j + 1);
        }
        out << "\n";
    }
    out << "\n";
}

// =====================================================================
// Automated Unit Verification Routine
// =====================================================================

bool runPatternTests() {
    std::cout << "Running automated verification for Number Pattern Generator...\n";

    // Test 1: Floyd's Triangle line count and total numbers
    std::ostringstream ssFloyd;
    generateFloydsTriangle(4, ssFloyd);
    std::string strFloyd = ssFloyd.str();
    // 4 rows should contain numbers 1 through 10
    if (strFloyd.find("10") == std::string::npos) return false;

    // Test 2: Palindrome Pyramid symmetry check
    std::ostringstream ssPyramid;
    generatePyramid(3, ssPyramid);
    std::string strPyramid = ssPyramid.str();
    if (strPyramid.find("1 2 3 2 1") == std::string::npos) return false;

    // Test 3: Pascal's Triangle binomial coefficient check
    std::ostringstream ssPascal;
    generatePascalsTriangle(5, ssPascal);
    std::string strPascal = ssPascal.str();
    // Row index 4 (5th row) contains "1   4   6   4   1"
    if (strPascal.find("6") == std::string::npos) return false;

    std::cout << "[PASS] All pattern generation algorithm checks passed successfully.\n";
    return true;
}

// =====================================================================
// Interactive Terminal Menu
// =====================================================================

void printBanner() {
    std::cout << "=============================================================\n";
    std::cout << "        🔷  ALGORITHMIC NUMBER PATTERN GENERATOR  🔷         \n";
    std::cout << "=============================================================\n";
    std::cout << "Explore nested loops, algorithmic symmetry, and combinatorics.\n\n";
}

void printMenu() {
    std::cout << "Available Pattern Types:\n";
    std::cout << "  [1] Palindromic Number Pyramid\n";
    std::cout << "  [2] Inverted Number Pyramid\n";
    std::cout << "  [3] Symmetric Number Diamond\n";
    std::cout << "  [4] Floyd's Triangle (Continuous Series)\n";
    std::cout << "  [5] Pascal's Triangle (Binomial Coefficients)\n";
    std::cout << "  [6] Run Automated Algorithm Tests\n";
    std::cout << "  [0] Exit Application\n";
    std::cout << "Enter selection (0-6): ";
}

int promptRows(int maxLimit = 15) {
    int rows = 0;
    while (true) {
        std::cout << "Enter number of rows (1 to " << maxLimit << "): ";
        if (std::cin >> rows && rows >= 1 && rows <= maxLimit) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return rows;
        }
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "[!] Invalid row count. Please enter a number between 1 and " << maxLimit << ".\n";
    }
}

int main(int argc, char* argv[]) {
    // Check for automated test flag
    if (argc > 1 && std::string(argv[1]) == "--test") {
        return runPatternTests() ? 0 : 1;
    }

    printBanner();

    int choice = -1;
    while (true) {
        printMenu();
        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "\n[!] Please enter a valid number (0-6).\n\n";
            continue;
        }
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        if (choice == 0) {
            std::cout << "\nExiting Pattern Generator. Happy Coding!\n";
            break;
        }

        switch (choice) {
            case 1: {
                int r = promptRows(15);
                generatePyramid(r, std::cout);
                break;
            }
            case 2: {
                int r = promptRows(15);
                generateInvertedPyramid(r, std::cout);
                break;
            }
            case 3: {
                int r = promptRows(12);
                generateDiamond(r, std::cout);
                break;
            }
            case 4: {
                int r = promptRows(20);
                generateFloydsTriangle(r, std::cout);
                break;
            }
            case 5: {
                int r = promptRows(13); // limit to 13 to avoid integer overflow and terminal wrap
                generatePascalsTriangle(r, std::cout);
                break;
            }
            case 6:
                runPatternTests();
                break;
            default:
                std::cout << "\n[!] Invalid choice. Please select from 0 to 6.\n\n";
                break;
        }
    }

    return 0;
}
