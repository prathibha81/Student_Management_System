""" Report Generation Module for Student Management System """

import pandas as pd
from database import connect

def generate_report():
    roll = input("Enter Roll No: ")

    conn = connect()
    cur = conn.cursor()

    # Fetch all subjects and marks 
    cur.execute("""
    SELECT s.name, s.class,
           m.subject,
           m.fa1, m.fa2, (m.fa1+m.fa2)/2 AS fa12,
           m.sa1,
           ((m.fa1+m.fa2)/2 + m.sa1) AS t1,
           m.fa3, m.fa4, (m.fa3+m.fa4)/2 AS fa34,
           m.sa2,
           ((m.fa3+m.fa4)/2 + m.sa2) AS t2,
           m.final, m.grade, m.result
    FROM students s
    JOIN marks m ON s.student_id = m.student_id
    WHERE s.roll_no = ?
    """, (roll,))

    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No records found.")
        return

    # Student details
    name, cls = rows[0][0], rows[0][1]

    columns = [
        "Subject",
        "FA1(20)", "FA2(20)", "FA1+FA2",
        "SA1(80)", "T1(100)",
        "FA3(20)", "FA4(20)", "FA3+FA4",
        "SA2(80)", "T2(100)",
        "Final(100)", "Grade", "Result"
    ]

    data = []
    numeric_cols = ["FA1(20)","FA2(20)","FA1+FA2","SA1(80)","T1(100)",
                    "FA3(20)","FA4(20)","FA3+FA4","SA2(80)","T2(100)","Final(100)"]

    for r in rows:
        data.append([
            r[2],      # Subject
            r[3], r[4], round(r[5],1),
            r[6], round(r[7],1),
            r[8], r[9], round(r[10],1),
            r[11], round(r[12],1),
            r[13],     # Final
            r[14],     # Grade
            r[15]      # Result
        ])

    df = pd.DataFrame(data, columns=columns)

    # TOTAL row
    total_row = ["TOTAL"] + [df[col].sum() if col in numeric_cols else "" for col in columns[1:]]
    df.loc[len(df)] = total_row

    # DISPLAY
    print("\n" + "-"*100)
    print("STUDENT PROGRESS REPORT".center(100))
    print("-"*100)
    print(f"Name: {name}\tClass: {cls}\tRoll No: {roll}\n")
    print(df.to_string(index=False))
    print("-"*100)

    # Optional Excel export
    save = input("\nSave report as Excel? (y/n): ")
    if save.lower() == "y":
        df.to_excel(f"{name}_report.xlsx", index=False)
        print(f"Report saved as {name}_report.xlsx")





def view_data():
    conn = connect()
    cur = conn.cursor()
    
    # Fetch all students
    cur.execute("SELECT student_id, name, roll_no, class FROM students ORDER BY roll_no")
    rows = cur.fetchall()
    
    if not rows:
        print("No students found.")
    else:
        print("\nALL STUDENTS:\n")
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Name", "Roll No", "Class"))
        print("-"*50)
        for r in rows:
            print("{:<5} {:<20} {:<10} {:<10}".format(r[0], r[1], r[2], r[3]))
    
    conn.close()
