""" Student Management Module """

from database import connect

def add_student():
    name = input("Enter Name: ").strip()
    roll = input("Enter Roll No: ").strip()
    cls = input("Enter Class: ").strip()

    conn = connect()
    cur = conn.cursor()

    # Check if student already exists
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    if cur.fetchone():
        print(f"Roll number {roll} already exists. You cannot add student again.")
        conn.close()
        return

    # Insert new student
    cur.execute(
        "INSERT INTO students(name, roll_no, class) VALUES (?, ?, ?)",
        (name, roll, cls)
    )
    conn.commit()
    conn.close()
    print(f"Student {name} added successfully.")


def view_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    conn.close()

def delete_student():
    roll = input("Enter Roll No of student to delete: ")

    conn = connect()
    cur = conn.cursor()

    # Check if student exists
    cur.execute("SELECT student_id, name FROM students WHERE roll_no=?", (roll,))
    student = cur.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    student_id, name = student

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.")
        conn.close()
        return

    # Delete marks first (foreign key dependency)
    cur.execute("DELETE FROM marks WHERE student_id=?", (student_id,))
    # Delete student
    cur.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    
    conn.commit()
    conn.close()
    print(f"Student {name} and all associated marks have been deleted.")

