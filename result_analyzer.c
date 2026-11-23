/**
 * ============================================================================
 * Project: Student Result and Grade Analyzer
 * Problem Statement: Develop a menu-driven C program to record student details,
 *                    compute total marks, percentages, assign letter grades,
 *                    enforce individual subject pass thresholds, and generate
 *                    comprehensive class analytics and topper reports.
 * 
 * Batch: Batch - 19
 * Team Number: APEX FOUR
 * Team Members:
 *   1. Daksh
 *   2. Shriman Nautiyal
 *   3. Shivam Rawat
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_STUDENTS 100
#define NUM_SUBJECTS 5
#define MAX_NAME_LEN 50
#define PASSING_MARKS 35.0f
#define MAX_BUFFER 256

/* Subject names for clear reporting */
static const char *SUBJECT_NAMES[NUM_SUBJECTS] = {
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science",
    "English"
};

/**
 * Structure representing an individual student's record.
 * Demonstrates: struct, 1D array, and string handling.
 */
typedef struct {
    int rollNo;
    char name[MAX_NAME_LEN];
    float marks[NUM_SUBJECTS];
    float totalMarks;
    float percentage;
    char grade[3]; /* "A+", "A", "B", "C", "D", "E", "F" */
    int isPassed;  /* 1 = PASS, 0 = FAIL */
} Student;

/* ============================================================================
 * FUNCTION PROTOTYPES
 * Demonstrates: Modular programming with functions and pointer parameters.
 * ============================================================================
 */
void displayMainMenu(void);
void clearInputBuffer(void);
int getValidatedInt(int *output, int minVal, int maxVal, const char *prompt, const char *errorMsg);
int getValidatedFloat(float *output, float minVal, float maxVal, const char *prompt, const char *errorMsg);
void getValidatedString(char *output, int maxLen, const char *prompt);

void addStudentRecords(Student *students, int *studentCount);
void calculateResult(Student *s);
void computeGrade(Student *s);
void displayResultSummary(const Student *students, int studentCount);
void displayClassReport(const Student *students, int studentCount);
void searchStudentByRoll(const Student *students, int studentCount);
int isRollNumberUnique(const Student *students, int studentCount, int rollNo);

/* ============================================================================
 * MAIN FUNCTION
 * Demonstrates: switch-case, loops, and control flow.
 * ============================================================================
 */
int main(void) {
    Student students[MAX_STUDENTS];
    int studentCount = 0;
    int choice = 0;
    int running = 1;

    printf("\n======================================================================\n");
    printf("         WELCOME TO STUDENT RESULT AND GRADE ANALYZER                \n");
    printf("         Batch: Batch - 19 | Team: APEX FOUR                         \n");
    printf("         Developed by: Daksh, Shriman Nautiyal, Shivam Rawat         \n");
    printf("======================================================================\n");

    while (running) {
        displayMainMenu();
        if (!getValidatedInt(&choice, 1, 5, "Enter your choice [1-5]: ", "Invalid choice! Please select an option between 1 and 5.")) {
            continue;
        }

        switch (choice) {
            case 1:
                addStudentRecords(students, &studentCount);
                break;
            case 2:
                displayResultSummary(students, studentCount);
                break;
            case 3:
                displayClassReport(students, studentCount);
                break;
            case 4:
                searchStudentByRoll(students, studentCount);
                break;
            case 5:
                printf("\n======================================================================\n");
                printf(" Thank you for using Student Result and Grade Analyzer!\n");
                printf(" Project by Team APEX FOUR (Batch - 19). Exiting successfully...\n");
                printf("======================================================================\n\n");
                running = 0;
                break;
            default:
                printf("\n[ERROR] Invalid option selected. Please choose between 1 and 5.\n");
                break;
        }
    }

    return 0;
}

/* ============================================================================
 * USER INTERFACE & INPUT VALIDATION UTILITIES
 * Demonstrates: Pointer manipulation, standard I/O buffer clearing, string checks.
 * ============================================================================
 */

/**
 * Displays the formatted main navigation menu.
 */
void displayMainMenu(void) {
    printf("\n+--------------------------------------------------------------------+\n");
    printf("|                         MAIN MENU                                  |\n");
    printf("+--------------------------------------------------------------------+\n");
    printf("|  [1] Add Student Records                                           |\n");
    printf("|  [2] View Student-wise Result Summary Table                        |\n");
    printf("|  [3] View Class Performance & Analytics Report                     |\n");
    printf("|  [4] Search Student Record by Roll Number                          |\n");
    printf("|  [5] Exit Application                                              |\n");
    printf("+--------------------------------------------------------------------+\n");
}

/**
 * Clears trailing characters and newlines from standard input buffer.
 * Eliminates infinite loop scenarios when invalid non-numeric data is provided.
 */
void clearInputBuffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
        /* Discard characters until newline or EOF */
    }
}

/**
 * Validates integer inputs within a range [minVal, maxVal].
 * Rejects non-numeric characters and out-of-range numbers.
 */
int getValidatedInt(int *output, int minVal, int maxVal, const char *prompt, const char *errorMsg) {
    char buffer[MAX_BUFFER];
    char extra;
    int value;

    while (1) {
        printf("%s", prompt);
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            clearerr(stdin);
            return 0;
        }

        /* Check for empty enter / newline only */
        if (buffer[0] == '\n' || buffer[0] == '\0') {
            printf("[ERROR] Input cannot be blank. Please try again.\n");
            continue;
        }

        /* Parse integer and ensure no trailing invalid alphanumeric characters */
        if (sscanf(buffer, "%d %c", &value, &extra) == 1) {
            if (value < minVal || value > maxVal) {
                printf("[ERROR] %s (Must be between %d and %d)\n", errorMsg, minVal, maxVal);
                continue;
            }
            *output = value;
            return 1;
        } else {
            printf("[ERROR] Invalid numeric input! Non-numeric characters detected.\n");
        }
    }
}

/**
 * Validates floating-point marks within range [minVal, maxVal] (0.0 to 100.0).
 * Demonstrates: Float validation, boundary checks, and robust error recovery.
 */
int getValidatedFloat(float *output, float minVal, float maxVal, const char *prompt, const char *errorMsg) {
    char buffer[MAX_BUFFER];
    char extra;
    float value;

    while (1) {
        printf("%s", prompt);
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            clearerr(stdin);
            return 0;
        }

        if (buffer[0] == '\n' || buffer[0] == '\0') {
            printf("[ERROR] Input cannot be blank. Please enter a valid number.\n");
            continue;
        }

        if (sscanf(buffer, "%f %c", &value, &extra) == 1) {
            if (value < minVal || value > maxVal) {
                printf("[ERROR] %s (Allowed range: %.2f to %.2f)\n", errorMsg, minVal, maxVal);
                continue;
            }
            *output = value;
            return 1;
        } else {
            printf("[ERROR] Invalid numeric input! Please enter a valid decimal/integer value.\n");
        }
    }
}

/**
 * Reads and cleans a string from standard input.
 * Strips trailing newline and ensures input is non-empty.
 */
void getValidatedString(char *output, int maxLen, const char *prompt) {
    char buffer[MAX_BUFFER];

    while (1) {
        printf("%s", prompt);
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            clearerr(stdin);
            continue;
        }

        /* Remove trailing newline character */
        buffer[strcspn(buffer, "\r\n")] = '\0';

        /* Trim leading whitespace */
        char *start = buffer;
        while (isspace((unsigned char)*start)) {
            start++;
        }

        if (strlen(start) == 0) {
            printf("[ERROR] Name cannot be empty or solely whitespace. Please enter again.\n");
            continue;
        }

        /* Copy up to maxLen - 1 bytes */
        strncpy(output, start, (size_t)(maxLen - 1));
        output[maxLen - 1] = '\0';
        break;
    }
}

/**
 * Checks whether a given roll number already exists in the system.
 */
int isRollNumberUnique(const Student *students, int studentCount, int rollNo) {
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            return 0; /* Duplicate found */
        }
    }
    return 1; /* Unique */
}

/* ============================================================================
 * CORE LOGIC: CALCULATION & GRADE ASSIGNMENT
 * Demonstrates: Pointers, arithmetic operators, if-else chains.
 * ============================================================================
 */

/**
 * Computes letter grade based on percentage and individual subject pass criteria.
 * Rule: If ANY subject mark < 35, student FAILS with grade "F",
 * regardless of overall percentage.
 */
void computeGrade(Student *s) {
    /* Subject-level pass rule check */
    if (!s->isPassed) {
        strcpy(s->grade, "F");
        return;
    }

    /* Overall percentage grading criteria */
    if (s->percentage >= 90.0f) {
        strcpy(s->grade, "A+");
    } else if (s->percentage >= 80.0f) {
        strcpy(s->grade, "A");
    } else if (s->percentage >= 70.0f) {
        strcpy(s->grade, "B");
    } else if (s->percentage >= 60.0f) {
        strcpy(s->grade, "C");
    } else if (s->percentage >= 50.0f) {
        strcpy(s->grade, "D");
    } else if (s->percentage >= 35.0f) {
        strcpy(s->grade, "E");
    } else {
        strcpy(s->grade, "F");
    }
}

/**
 * Calculates total marks, percentage, pass/fail status, and grade for a student.
 */
void calculateResult(Student *s) {
    s->totalMarks = 0.0f;
    s->isPassed = 1; /* Assume pass initially */

    for (int i = 0; i < NUM_SUBJECTS; i++) {
        s->totalMarks += s->marks[i];
        if (s->marks[i] < PASSING_MARKS) {
            s->isPassed = 0; /* Failed in at least one subject */
        }
    }

    s->percentage = (s->totalMarks / (NUM_SUBJECTS * 100.0f)) * 100.0f;
    computeGrade(s);
}

/* ============================================================================
 * FEATURE 1: ADD STUDENT RECORDS
 * ============================================================================
 */
void addStudentRecords(Student *students, int *studentCount) {
    int numToAdd = 0;

    printf("\n----------------------------------------------------------------------\n");
    printf("                     ADD NEW STUDENT RECORDS                          \n");
    printf("----------------------------------------------------------------------\n");
    printf("Current records in database: %d / %d\n", *studentCount, MAX_STUDENTS);

    if (*studentCount >= MAX_STUDENTS) {
        printf("[WARNING] Student database is full! Cannot add more records.\n");
        return;
    }

    int remainingCapacity = MAX_STUDENTS - *studentCount;
    char promptMsg[100];
    sprintf(promptMsg, "Enter number of students to add (1 to %d): ", remainingCapacity);

    getValidatedInt(&numToAdd, 1, remainingCapacity, promptMsg, "Number of students out of permissible bounds.");

    for (int i = 0; i < numToAdd; i++) {
        Student *s = &students[*studentCount];
        printf("\n>>> Entering details for Student %d of %d <<<\n", i + 1, numToAdd);

        /* Roll Number input with uniqueness validation */
        while (1) {
            int rNo = 0;
            getValidatedInt(&rNo, 1, 999999, " Enter Roll Number (positive integer): ", "Roll number must be a positive integer.");
            if (!isRollNumberUnique(students, *studentCount, rNo)) {
                printf("[ERROR] Roll Number %d already exists! Each student must have a unique roll number.\n", rNo);
                continue;
            }
            s->rollNo = rNo;
            break;
        }

        /* Student Name */
        getValidatedString(s->name, MAX_NAME_LEN, " Enter Student Full Name: ");

        /* Subject Marks */
        printf(" Enter marks for 5 subjects (Passing mark per subject is %.0f, Scale: 0 to 100):\n", PASSING_MARKS);
        for (int sub = 0; sub < NUM_SUBJECTS; sub++) {
            char subPrompt[100];
            sprintf(subPrompt, "   - %-16s Marks [0-100]: ", SUBJECT_NAMES[sub]);
            getValidatedFloat(&s->marks[sub], 0.0f, 100.0f, subPrompt, "Marks must be between 0.0 and 100.0.");
        }

        /* Compute results immediately */
        calculateResult(s);
        (*studentCount)++;

        printf("[SUCCESS] Record saved for Roll No %d (%s)! Total: %.1f/500, Status: %s, Grade: %s\n",
               s->rollNo, s->name, s->totalMarks, s->isPassed ? "PASS" : "FAIL", s->grade);
    }

    printf("\n[COMPLETED] Successfully added %d student record(s). Total enrolled: %d\n", numToAdd, *studentCount);
}

/* ============================================================================
 * FEATURE 2: DISPLAY STUDENT-WISE RESULT SUMMARY TABLE
 * ============================================================================
 */
void displayResultSummary(const Student *students, int studentCount) {
    printf("\n========================================================================================================================\n");
    printf("                                              STUDENT-WISE RESULT SUMMARY TABLE                                         \n");
    printf("========================================================================================================================\n");

    if (studentCount == 0) {
        printf("[!] No student records found. Please add student records using Menu Option 1 first.\n");
        printf("========================================================================================================================\n");
        return;
    }

    /* Table Header */
    printf("+---------+----------------------+-------+-------+-------+-------+-------+---------+------------+-------+--------+\n");
    printf("| Roll No | Student Name         | Sub 1 | Sub 2 | Sub 3 | Sub 4 | Sub 5 |  Total  | Percentage | Grade | Status |\n");
    printf("+---------+----------------------+-------+-------+-------+-------+-------+---------+------------+-------+--------+\n");

    /* Table Rows */
    for (int i = 0; i < studentCount; i++) {
        const Student *s = &students[i];
        printf("| %-7d | %-20.20s | %5.1f | %5.1f | %5.1f | %5.1f | %5.1f | %7.1f |   %6.2f%%  |  %-4s |  %-5s |\n",
               s->rollNo,
               s->name,
               s->marks[0],
               s->marks[1],
               s->marks[2],
               s->marks[3],
               s->marks[4],
               s->totalMarks,
               s->percentage,
               s->grade,
               s->isPassed ? "PASS" : "FAIL");
    }

    printf("+---------+----------------------+-------+-------+-------+-------+-------+---------+------------+-------+--------+\n");
    printf(" Note: Sub 1: %s | Sub 2: %s | Sub 3: %s | Sub 4: %s | Sub 5: %s\n",
           SUBJECT_NAMES[0], SUBJECT_NAMES[1], SUBJECT_NAMES[2], SUBJECT_NAMES[3], SUBJECT_NAMES[4]);
    printf(" Criterion: Minimum %.0f marks required in EACH subject to PASS.\n", PASSING_MARKS);
    printf("========================================================================================================================\n");
}

/* ============================================================================
 * FEATURE 3: CLASS PERFORMANCE REPORT & ANALYTICS
 * Demonstrates: Aggregations, statistical computations, topper identification.
 * ============================================================================
 */
void displayClassReport(const Student *students, int studentCount) {
    printf("\n======================================================================\n");
    printf("                   CLASS PERFORMANCE & ANALYTICS REPORT               \n");
    printf("======================================================================\n");

    if (studentCount == 0) {
        printf("[!] No student records found. Cannot generate class performance report.\n");
        printf("======================================================================\n");
        return;
    }

    int passedCount = 0;
    int failedCount = 0;
    float sumPercentage = 0.0f;
    int topperIndex = -1;
    float highestPercentage = -1.0f;

    /* Grade distribution counters */
    int countAPlus = 0, countA = 0, countB = 0, countC = 0, countD = 0, countE = 0, countF = 0;

    for (int i = 0; i < studentCount; i++) {
        const Student *s = &students[i];
        sumPercentage += s->percentage;

        if (s->isPassed) {
            passedCount++;
            /* Topper must ideally be a passed student with highest percentage */
            if (s->percentage > highestPercentage) {
                highestPercentage = s->percentage;
                topperIndex = i;
            }
        } else {
            failedCount++;
        }

        /* Grade categorization */
        if (strcmp(s->grade, "A+") == 0) countAPlus++;
        else if (strcmp(s->grade, "A") == 0) countA++;
        else if (strcmp(s->grade, "B") == 0) countB++;
        else if (strcmp(s->grade, "C") == 0) countC++;
        else if (strcmp(s->grade, "D") == 0) countD++;
        else if (strcmp(s->grade, "E") == 0) countE++;
        else countF++;
    }

    /* Fallback: If no student passed, pick highest overall percentage student */
    if (topperIndex == -1 && studentCount > 0) {
        topperIndex = 0;
        highestPercentage = students[0].percentage;
        for (int i = 1; i < studentCount; i++) {
            if (students[i].percentage > highestPercentage) {
                highestPercentage = students[i].percentage;
                topperIndex = i;
            }
        }
    }

    float classAverage = sumPercentage / (float)studentCount;
    float passRate = ((float)passedCount / (float)studentCount) * 100.0f;
    float failRate = ((float)failedCount / (float)studentCount) * 100.0f;

    printf("\n--- Overall Class Metrics ---\n");
    printf(" Total Students Enrolled       : %d\n", studentCount);
    printf(" Students Passed               : %d (%.2f%%)\n", passedCount, passRate);
    printf(" Students Failed               : %d (%.2f%%)\n", failedCount, failRate);
    printf(" Overall Class Average         : %.2f%%\n", classAverage);

    printf("\n--- Class Topper Details ---\n");
    if (topperIndex != -1) {
        const Student *top = &students[topperIndex];
        printf(" Name                          : %s\n", top->name);
        printf(" Roll Number                   : %d\n", top->rollNo);
        printf(" Total Marks                   : %.1f / 500.0\n", top->totalMarks);
        printf(" Percentage Secured            : %.2f%%\n", top->percentage);
        printf(" Letter Grade                  : %s\n", top->grade);
        printf(" Final Status                  : %s\n", top->isPassed ? "PASS" : "FAIL (Notice: No student passed all subjects)");
    }

    printf("\n--- Grade Distribution Breakdown ---\n");
    printf(" Grade A+ (>= 90%%)              : %d student(s)\n", countAPlus);
    printf(" Grade A  (80%% - 89.9%%)         : %d student(s)\n", countA);
    printf(" Grade B  (70%% - 79.9%%)         : %d student(s)\n", countB);
    printf(" Grade C  (60%% - 69.9%%)         : %d student(s)\n", countC);
    printf(" Grade D  (50%% - 59.9%%)         : %d student(s)\n", countD);
    printf(" Grade E  (35%% - 49.9%%)         : %d student(s)\n", countE);
    printf(" Grade F  (< 35%% or Failed Sub) : %d student(s)\n", countF);

    printf("======================================================================\n");
}

/* ============================================================================
 * FEATURE 4: SEARCH STUDENT BY ROLL NUMBER
 * Demonstrates: Linear search, formatted single-record display.
 * ============================================================================
 */
void searchStudentByRoll(const Student *students, int studentCount) {
    printf("\n----------------------------------------------------------------------\n");
    printf("                     SEARCH STUDENT BY ROLL NUMBER                    \n");
    printf("----------------------------------------------------------------------\n");

    if (studentCount == 0) {
        printf("[!] No student records to search. Please add students first.\n");
        return;
    }

    int searchRoll = 0;
    getValidatedInt(&searchRoll, 1, 999999, "Enter Roll Number to search: ", "Invalid roll number format.");

    int foundIndex = -1;
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == searchRoll) {
            foundIndex = i;
            break;
        }
    }

    if (foundIndex != -1) {
        const Student *s = &students[foundIndex];
        printf("\n==================== STUDENT SCORECARD ====================\n");
        printf(" Roll Number     : %d\n", s->rollNo);
        printf(" Student Name    : %s\n", s->name);
        printf("-----------------------------------------------------------\n");
        printf(" Subject-wise Breakdown:\n");
        for (int j = 0; j < NUM_SUBJECTS; j++) {
            printf("   * %-16s : %5.1f / 100.0   [%s]\n",
                   SUBJECT_NAMES[j], s->marks[j],
                   (s->marks[j] >= PASSING_MARKS) ? "PASS" : "FAIL (< 35)");
        }
        printf("-----------------------------------------------------------\n");
        printf(" Total Marks     : %.1f / 500.0\n", s->totalMarks);
        printf(" Percentage      : %.2f%%\n", s->percentage);
        printf(" Letter Grade    : %s\n", s->grade);
        printf(" Final Result    : %s\n", s->isPassed ? "PASS" : "FAIL (Failed in one or more subjects)");
        printf("===========================================================\n");
    } else {
        printf("\n[NOT FOUND] No student record matches Roll Number %d.\n", searchRoll);
    }
}
