# Student Management System (SMS)

## 📘 Project Overview

The **Student Management System (SMS)** is a Python-based console application designed to manage student records, subject-wise marks, and generate detailed report cards. It is a beginner-friendly project that demonstrates the use of **Python programming**, **SQLite database**, and basic **data processing** concepts.

The system allows users to:

* Add and manage student details
* Enter marks for multiple subjects at once
* Automatically calculate totals, grades, and pass/fail status
* Generate formatted report cards
* View and delete student records

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3.x
* **Database:** SQLite
* **Libraries:**

  * `sqlite3`
  * `pandas` (for report formatting and Excel export)

---



## ⚙️ Features

### 1. Add Student

* Adds new student details
* Prevents duplicate roll numbers

### 2. View Students

* Displays all student records in tabular format

### 3. Add Marks (Multiple Subjects)

* Enter marks for multiple subjects in one go
* Automatically calculates:

  * T1 and T2 totals
  * Final marks (out of 100)
  * Grade and Pass/Fail result

### 4. Generate Report Card

* Displays a wide-format report card similar to school reports
* Includes:

  * FA, SA, totals
  * Final marks, grade, result
  * TOTAL row
* Optional Excel export

### 5. Delete Student

* Deletes student and all related marks using roll number

---

## 🧮 Grade Criteria

| Final Marks | Grade | Result |
| ----------- | ----- | ------ |
| ≥ 90        | A+    | PASS   |
| 75–89       | A     | PASS   |
| 60–74       | B     | PASS   |
| 50–59       | C     | PASS   |
| < 40        | D     | FAIL   |

---



## 🚀 Future Enhancements

### 1.Graphical Analysis

* Use Matplotlib or Plotly to generate graphs like:

  - Subject-wise performance

  - Term-wise comparison (T1 vs T2)

  - Grade distribution among students

### 2.PDF Report Generation

* Export progress reports as PDF for school records.

### 3.Login and Role Management

* Separate roles for Admin, Teacher, and Student.

* Restrict actions like deleting students or entering marks.

### 4.Search and Filter

* Search students by name, class, or roll number.

* Filter reports by subject or grade.

### 5.Web or GUI Interface

* Build using Tkinter, PyQt, or Flask for a user-friendly interface.

### 6.Analytics Dashboard

* Show average marks, pass/fail percentages, and top-performing students visually.
---

## 📌 Conclusion

This Student Management System is a complete beginner-level Python project that demonstrates CRUD operations, database integration, and report generation. It is ideal for academic submissions, mini-projects, and learning database-driven Python app
