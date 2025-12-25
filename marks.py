""" Marks Management Module """

from database import connect

def add_marks():
    roll = input("Enter Roll No: ").strip()

    conn = connect()
    cur = conn.cursor()

    # Find student
    cur.execute("SELECT student_id FROM students WHERE roll_no=?", (roll,))
    student = cur.fetchone()
    if not student:
        print(f"Student with roll no {roll} not found. Please add student first.")
        conn.close()
        return

    student_id = student[0]

    


    # fecth number of subjects
    num_subjects = int(input("Enter number of subjects: "))

    for i in range(num_subjects):
        print(f"\n--- Enter marks for Subject {i+1} ---")
        subject = input("Enter Subject Name: ")

        fa1 = int(input("FA1 (20): "))
        fa2 = int(input("FA2 (20): "))
        sa1 = int(input("SA1 (80): "))

        fa3 = int(input("FA3 (20): "))
        fa4 = int(input("FA4 (20): "))
        sa2 = int(input("SA2 (80): "))

        t1 = (fa1 + fa2) / 2 + sa1
        t2 = (fa3 + fa4) / 2 + sa2
        final = int((t1 + t2) / 2)

        # Grade calculation
        if final >= 90:
            grade = "A+"
        elif final >= 75:
            grade = "A"
        elif final >= 60:
            grade = "B"
        elif final >= 50:
            grade = "C"
        else:
            grade = "D"

        result = "PASS" if final >= 40 else "FAIL"

        # Insert into DB
        cur.execute("""
            INSERT INTO marks
            (student_id, subject, fa1, fa2, sa1, fa3, fa4, sa2, final, grade, result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (student_id, subject, fa1, fa2, sa1, fa3, fa4, sa2, final, grade, result))

        print(f"Marks for {subject} added successfully.")

    conn.commit()
    conn.close()
    print("\nAll subjects added successfully.")

