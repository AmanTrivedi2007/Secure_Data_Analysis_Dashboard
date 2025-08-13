SecureDataAnalysisDashboard
Overview
SecureDataAnalysisDashboard is a Python-based command-line application that combines secure user authentication with powerful CSV data analysis. It uses Pandas, NumPy, and Matplotlib to process, analyze, and visualize multi-year datasets, while enforcing strong account security with salted SHA-256 password hashing and OTP-based two-factor authentication.

This project was built to solve two common problems in data-driven workflows:

Keeping user access secure while allowing multiple unique accounts without conflicts.

Analyzing large CSV data efficiently and providing clear insights without manual calculations.

Key Features
🔐 Secure User Authentication
Unique username generation with duplicate checks — solves the issue of conflicting usernames during account creation.

Random password generation and secure storage with per-user cryptographic salt + SHA-256 hash — solves the problem of weak or compromised password storage.

Time-bound OTP for additional verification — solves the risk of stolen credentials being used without the account owner’s knowledge.

Error-aware file handling ensures the system won't crash if credential files are missing or contain bad data.

📊 Data Analysis & Visualization
Reads any CSV file formatted with yearly & quarterly numeric data.

Calculates total and average revenue per year using NumPy, solving the tedious manual computation process.

Creates bar charts (average yearly revenue) and line charts (total yearly revenue trends) with Matplotlib — solving the difficulty of quickly understanding trends from raw numbers.

Handles invalid formats, missing files, and empty datasets gracefully, helping users correct issues without frustration.

💻 User-Friendly CLI
Guided, step-by-step account creation and login.

Clear feedback and prompts to reduce confusion.

Continuous loop with options to re-try or exit at any stage.

How It Works — Problem-Solving in Action
1️⃣ Account Creation
Validates that the user enters a proper name (3–20 characters, non-empty).

Checks existing usernames to prevent duplicates.

Generates strong, random passwords automatically.

Stores usernames and password hashes separately, maintaining synchronization with blank-line filtering to avoid mismatches.

Problem solved: Prevents duplicate accounts, insecure password storage, and crash errors when files are missing.

2️⃣ Login
Reads stored usernames and password hashes, skipping blank/corrupt lines.

Matches the index of the username to the correct hashed password + salt.

Hashes the entered password, compares to stored hash.

On success, issues a 6-digit OTP valid for 60 seconds.

Problem solved: Eliminates mismatches between usernames and passwords; adds two-factor verification for extra security.

3️⃣ Data Analysis
Requests a valid CSV file in a consistent format.

Uses Pandas to load data, NumPy to analyze it, and Matplotlib to visualize it.

Options:

View dataset

Total revenue/year

Average revenue/year

Bar chart (avg/year)

Line chart (total/year)

Exit

Problem solved: Reduces manual effort in computing and visualizing data; handles user errors gracefully.

CSV File Format Requirements
Must include a header row.

First column → Year.

Next 4 columns → Numeric data for quarters.

Example:

Year	Q1	Q2	Q3	Q4
2022	150	200	180	220
2023	170	210	190	230
Requirements
Python 3.6+

Libraries:

pandas

numpy

matplotlib

Conclusion
SecureDataAnalysisDashboard effectively integrates security and data analysis. The problem-solving design ensures:

No duplicate accounts → conflict-free login experience.

Strong password protection → prevents breaches from stored credential leaks.

Two-factor authentication → stops attackers even with stolen passwords.

Error handling → avoids crashes and guides users to correct mistakes.

Automated data calculations → saves time and ensures accuracy.

Visualized insights → makes decision-making faster and easier.

This project is a strong demonstration of both security-oriented coding and data-processing expertise in Python — ideal for professional showcasing on GitHub.
