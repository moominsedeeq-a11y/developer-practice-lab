/**
 * Student Grading & Record System
 * A comprehensive object-oriented C++ application for managing student
 * academic records, calculating grades/GPA, searching records, and computing
 * class summary statistics.
 */

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cctype>
#include <limits>

// Grade boundary information
struct GradeDetail {
    std::string letter;
    double gpa;
};

/**
 * Maps a numerical percentage (0 - 100) to standard letter grade and GPA.
 */
GradeDetail computeGradeAndGPA(double percentage) {
    if (percentage >= 90.0) return {"A+", 4.0};
    if (percentage >= 80.0) return {"A",  3.7};
    if (percentage >= 70.0) return {"B",  3.0};
    if (percentage >= 60.0) return {"C",  2.0};
    if (percentage >= 50.0) return {"D",  1.0};
    return {"F", 0.0};
}

/**
 * Trims leading and trailing whitespace from a string.
 */
std::string trim(const std::string& str) {
    size_t first = str.find_first_not_of(" \t\r\n");
    if (first == std::string::npos) return "";
    size_t last = str.find_last_not_of(" \t\r\n");
    return str.substr(first, (last - first + 1));
}

/**
 * Converts a string to lowercase for case-insensitive searching.
 */
std::string toLower(const std::string& str) {
    std::string lower = str;
    std::transform(lower.begin(), lower.end(), lower.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    return lower;
}

/**
 * Represents an individual student record.
 */
class Student {
private:
    std::string id;
    std::string name;
    std::vector<double> marks;
    double totalMarks;
    double percentage;
    std::string grade;
    double gpa;

public:
    Student(const std::string& studentId, const std::string& studentName,
            const std::vector<double>& subjectMarks)
        : id(trim(studentId)), name(trim(studentName)), marks(subjectMarks),
          totalMarks(0.0), percentage(0.0), grade("F"), gpa(0.0) {
        calculatePerformance();
    }

    void calculatePerformance() {
        totalMarks = 0.0;
        for (double m : marks) {
            totalMarks += m;
        }

        if (!marks.empty()) {
            percentage = totalMarks / marks.size();
        } else {
            percentage = 0.0;
        }

        GradeDetail detail = computeGradeAndGPA(percentage);
        grade = detail.letter;
        gpa = detail.gpa;
    }

    // Accessors
    const std::string& getId() const { return id; }
    const std::string& getName() const { return name; }
    const std::vector<double>& getMarks() const { return marks; }
    double getTotalMarks() const { return totalMarks; }
    double getPercentage() const { return percentage; }
    const std::string& getGrade() const { return grade; }
    double getGPA() const { return gpa; }
    bool isPassed() const { return grade != "F"; }

    /**
     * Prints a formatted single row for tabular display.
     */
    void printTableRow() const {
        std::cout << "| " << std::left << std::setw(10) << id
                  << "| " << std::setw(22) << name
                  << "| " << std::right << std::fixed << std::setprecision(1) << std::setw(8) << totalMarks
                  << " | " << std::setw(7) << percentage << "%"
                  << " | " << std::setw(6) << grade
                  << " | " << std::setprecision(2) << std::setw(5) << gpa
                  << " |\n";
    }

    /**
     * Prints detailed individual student report.
     */
    void printDetailedReport(const std::vector<std::string>& subjectNames) const {
        std::cout << "\n+-------------------------------------------------------------+\n";
        std::cout << "|                  INDIVIDUAL STUDENT REPORT                  |\n";
        std::cout << "+-------------------------------------------------------------+\n";
        std::cout << "  Student ID  : " << id << "\n";
        std::cout << "  Full Name   : " << name << "\n";
        std::cout << "  Subjects Breakdown:\n";
        for (size_t i = 0; i < marks.size(); ++i) {
            std::string subName = (i < subjectNames.size()) ? subjectNames[i] : "Subject " + std::to_string(i + 1);
            std::cout << "    - " << std::left << std::setw(25) << subName
                      << ": " << std::right << std::fixed << std::setprecision(1) << std::setw(5) << marks[i] << " / 100\n";
        }
        std::cout << "  -----------------------------------------------------------\n";
        std::cout << "  Total Marks : " << std::fixed << std::setprecision(1) << totalMarks
                  << " / " << (marks.size() * 100) << "\n";
        std::cout << "  Percentage  : " << std::fixed << std::setprecision(2) << percentage << "%\n";
        std::cout << "  Final Grade : " << grade << "\n";
        std::cout << "  GPA         : " << std::fixed << std::setprecision(2) << gpa << " / 4.00\n";
        std::cout << "  Status      : " << (isPassed() ? "[PASS]" : "[FAIL]") << "\n";
        std::cout << "+-------------------------------------------------------------+\n";
    }
};

/**
 * Manages the collection of student records and grade analytics.
 */
class GradeBook {
private:
    std::vector<Student> students;
    std::vector<std::string> subjectNames;

public:
    GradeBook() {
        // Standard core computer science / BCA curriculum subjects
        subjectNames = {
            "Programming in C++",
            "Data Structures",
            "Discrete Mathematics",
            "Database Management",
            "Computer Networks"
        };
    }

    const std::vector<std::string>& getSubjectNames() const {
        return subjectNames;
    }

    size_t getStudentCount() const {
        return students.size();
    }

    /**
     * Checks if a student ID already exists.
     */
    bool idExists(const std::string& id) const {
        std::string target = trim(id);
        return std::any_of(students.begin(), students.end(),
                           [&target](const Student& s) { return s.getId() == target; });
    }

    /**
     * Adds a student record after validating unique ID and mark bounds.
     */
    bool addStudent(const std::string& id, const std::string& name,
                    const std::vector<double>& marks, std::string& outError) {
        if (trim(id).empty()) {
            outError = "Student ID cannot be empty.";
            return false;
        }
        if (trim(name).empty()) {
            outError = "Student name cannot be empty.";
            return false;
        }
        if (idExists(id)) {
            outError = "A student with ID '" + id + "' already exists.";
            return false;
        }
        if (marks.size() != subjectNames.size()) {
            outError = "Expected marks for " + std::to_string(subjectNames.size()) + " subjects.";
            return false;
        }
        for (double m : marks) {
            if (m < 0.0 || m > 100.0) {
                outError = "All marks must be between 0.0 and 100.0.";
                return false;
            }
        }

        students.emplace_back(id, name, marks);
        return true;
    }

    /**
     * Searches for a student by exact ID.
     */
    const Student* findById(const std::string& id) const {
        std::string target = trim(id);
        for (const auto& s : students) {
            if (s.getId() == target) return &s;
        }
        return nullptr;
    }

    /**
     * Searches for students by partial name (case-insensitive).
     */
    std::vector<const Student*> searchByName(const std::string& query) const {
        std::vector<const Student*> results;
        std::string target = toLower(trim(query));
        if (target.empty()) return results;

        for (const auto& s : students) {
            if (toLower(s.getName()).find(target) != std::string::npos) {
                results.push_back(&s);
            }
        }
        return results;
    }

    /**
     * Displays all students in a formatted tabular view.
     */
    void displayTable() const {
        if (students.empty()) {
            std::cout << "\n[!] No student records registered yet.\n";
            return;
        }

        std::string divider = "+-----------+-----------------------+----------+---------+--------+-------+";
        std::cout << "\n" << divider << "\n";
        std::cout << "| " << std::left << std::setw(10) << "Student ID"
                  << "| " << std::setw(22) << "Student Name"
                  << "| " << std::right << std::setw(8) << "Total"
                  << " | " << std::setw(7) << "Percent"
                  << " | " << std::setw(6) << "Grade"
                  << " | " << std::setw(5) << "GPA" << " |\n";
        std::cout << divider << "\n";

        for (const auto& s : students) {
            s.printTableRow();
        }
        std::cout << divider << "\n";
    }

    /**
     * Displays class-wide summary statistics.
     */
    void displayStatistics() const {
        if (students.empty()) {
            std::cout << "\n[!] No records available to compute class statistics.\n";
            return;
        }

        double totalClassPercent = 0.0;
        int passCount = 0;
        const Student* topStudent = &students[0];
        const Student* lowestStudent = &students[0];

        for (const auto& s : students) {
            totalClassPercent += s.getPercentage();
            if (s.isPassed()) passCount++;
            if (s.getPercentage() > topStudent->getPercentage()) topStudent = &s;
            if (s.getPercentage() < lowestStudent->getPercentage()) lowestStudent = &s;
        }

        double classAvg = totalClassPercent / students.size();
        double passRate = (static_cast<double>(passCount) / students.size()) * 100.0;

        std::cout << "\n+-------------------------------------------------------------+\n";
        std::cout << "|                   CLASS PERFORMANCE SUMMARY                 |\n";
        std::cout << "+-------------------------------------------------------------+\n";
        std::cout << "  Total Enrolled Students : " << students.size() << "\n";
        std::cout << "  Passed Students         : " << passCount << " (" << std::fixed << std::setprecision(1) << passRate << "%)\n";
        std::cout << "  Failed Students         : " << (students.size() - passCount) << "\n";
        std::cout << "  Class Average Score     : " << std::fixed << std::setprecision(2) << classAvg << "%\n";
        std::cout << "  Highest Scorer          : " << topStudent->getName() << " (" << topStudent->getId()
                  << ") with " << std::fixed << std::setprecision(1) << topStudent->getPercentage() << "% ("
                  << topStudent->getGrade() << ")\n";
        std::cout << "  Lowest Scorer           : " << lowestStudent->getName() << " (" << lowestStudent->getId()
                  << ") with " << std::fixed << std::setprecision(1) << lowestStudent->getPercentage() << "% ("
                  << lowestStudent->getGrade() << ")\n";
        std::cout << "+-------------------------------------------------------------+\n";
    }

    /**
     * Seeds realistic sample records for demonstration and instant testing.
     */
    void seedSampleData() {
        std::string err;
        addStudent("BCA-101", "Amina Mir",    {94.0, 92.5, 88.0, 95.0, 91.0}, err);
        addStudent("BCA-102", "Danish Wani",  {82.0, 78.5, 85.0, 80.0, 76.5}, err);
        addStudent("BCA-103", "Zahoor Lone",  {65.0, 70.0, 62.5, 58.0, 64.0}, err);
        addStudent("BCA-104", "Farhan Malik", {52.0, 48.0, 55.0, 51.5, 54.0}, err);
        addStudent("BCA-105", "Iqra Qureshi", {98.0, 96.0, 94.5, 99.0, 97.0}, err);
    }
};

// =====================================================================
// Automated Self-Test Verification Routine
// =====================================================================

bool runSelfTests() {
    std::cout << "Running automated unit verification for Student Grading System...\n";
    GradeBook gb;

    // Test 1: Grade and GPA calculation
    GradeDetail g1 = computeGradeAndGPA(95.0);
    if (g1.letter != "A+" || g1.gpa != 4.0) return false;

    GradeDetail g2 = computeGradeAndGPA(82.5);
    if (g2.letter != "A" || g2.gpa != 3.7) return false;

    GradeDetail g3 = computeGradeAndGPA(74.0);
    if (g3.letter != "B" || g3.gpa != 3.0) return false;

    GradeDetail g4 = computeGradeAndGPA(63.0);
    if (g4.letter != "C" || g4.gpa != 2.0) return false;

    GradeDetail g5 = computeGradeAndGPA(52.0);
    if (g5.letter != "D" || g5.gpa != 1.0) return false;

    GradeDetail g6 = computeGradeAndGPA(45.0);
    if (g6.letter != "F" || g6.gpa != 0.0) return false;

    // Test 2: Add valid student
    std::string err;
    bool added = gb.addStudent("TEST-01", "Test Student", {90, 80, 70, 60, 50}, err);
    if (!added) return false;

    const Student* s = gb.findById("TEST-01");
    if (!s) return false;
    if (s->getTotalMarks() != 350.0) return false;
    if (s->getPercentage() != 70.0) return false;
    if (s->getGrade() != "B") return false;
    if (s->getGPA() != 3.0) return false;

    // Test 3: Reject duplicate ID
    bool dupAdded = gb.addStudent("TEST-01", "Duplicate Student", {80, 80, 80, 80, 80}, err);
    if (dupAdded) return false;

    // Test 4: Reject out of bounds marks (<0 or >100)
    bool invalidMarks = gb.addStudent("TEST-02", "Bad Marks", {105, 80, 80, 80, 80}, err);
    if (invalidMarks) return false;

    // Test 5: Search by Name
    auto results = gb.searchByName("test");
    if (results.size() != 1) return false;

    std::cout << "[PASS] All Student Grading System automated checks passed successfully.\n";
    return true;
}

// =====================================================================
// Interactive Terminal Menu
// =====================================================================

void printHeader() {
    std::cout << "\n=============================================================\n";
    std::cout << "         🎓  STUDENT GRADING & RECORD SYSTEM - C++  🎓        \n";
    std::cout << "=============================================================\n";
}

void printMenu() {
    std::cout << "\n[1] Add New Student Record\n";
    std::cout << "[2] Display All Student Records (Table View)\n";
    std::cout << "[3] Search Student by ID (Detailed Report)\n";
    std::cout << "[4] Search Students by Name\n";
    std::cout << "[5] View Class Performance & Statistics\n";
    std::cout << "[6] Load Sample Demonstration Data\n";
    std::cout << "[7] Run Automated Verification Suite\n";
    std::cout << "[0] Exit Application\n";
    std::cout << "Select an option (0-7): ";
}

int main(int argc, char* argv[]) {
    // Check for automated headless test flag
    if (argc > 1 && std::string(argv[1]) == "--test") {
        return runSelfTests() ? 0 : 1;
    }

    GradeBook gradeBook;
    printHeader();

    int choice = -1;
    while (true) {
        printMenu();
        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "\n[!] Invalid input. Please enter a number between 0 and 7.\n";
            continue;
        }
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear line buffer

        if (choice == 0) {
            std::cout << "\nExiting Student Grading System. Thank you!\n";
            break;
        }

        switch (choice) {
            case 1: {
                std::string id, name;
                std::cout << "\nEnter Student ID (e.g., BCA-106): ";
                std::getline(std::cin, id);

                std::cout << "Enter Student Full Name: ";
                std::getline(std::cin, name);

                std::vector<double> marks;
                const auto& subjects = gradeBook.getSubjectNames();
                std::cout << "Enter marks for " << subjects.size() << " subjects (0 to 100):\n";

                bool inputValid = true;
                for (size_t i = 0; i < subjects.size(); ++i) {
                    double m;
                    std::cout << "  - " << subjects[i] << ": ";
                    if (!(std::cin >> m) || m < 0.0 || m > 100.0) {
                        std::cout << "    [!] Invalid mark! Must be between 0.0 and 100.0.\n";
                        std::cin.clear();
                        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                        inputValid = false;
                        break;
                    }
                    marks.push_back(m);
                }
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

                if (inputValid) {
                    std::string err;
                    if (gradeBook.addStudent(id, name, marks, err)) {
                        std::cout << "\n[✓] Student '" << name << "' (" << id << ") successfully registered!\n";
                    } else {
                        std::cout << "\n[!] Error adding student: " << err << "\n";
                    }
                }
                break;
            }
            case 2:
                gradeBook.displayTable();
                break;
            case 3: {
                std::string searchId;
                std::cout << "\nEnter Student ID to search: ";
                std::getline(std::cin, searchId);
                const Student* found = gradeBook.findById(searchId);
                if (found) {
                    found->printDetailedReport(gradeBook.getSubjectNames());
                } else {
                    std::cout << "\n[!] No student found with ID '" << searchId << "'.\n";
                }
                break;
            }
            case 4: {
                std::string query;
                std::cout << "\nEnter Name (or partial name) to search: ";
                std::getline(std::cin, query);
                auto results = gradeBook.searchByName(query);
                if (results.empty()) {
                    std::cout << "\n[!] No students matched query '" << query << "'.\n";
                } else {
                    std::cout << "\n[✓] Found " << results.size() << " match(es):\n";
                    for (const auto* s : results) {
                        s->printDetailedReport(gradeBook.getSubjectNames());
                    }
                }
                break;
            }
            case 5:
                gradeBook.displayStatistics();
                break;
            case 6:
                gradeBook.seedSampleData();
                std::cout << "\n[✓] Sample student records loaded successfully!\n";
                gradeBook.displayTable();
                break;
            case 7:
                runSelfTests();
                break;
            default:
                std::cout << "\n[!] Option not recognized. Please choose between 0 and 7.\n";
                break;
        }
    }

    return 0;
}
