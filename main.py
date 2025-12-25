""" Student Management System Main Module """

from database import create_tables
from student import add_student, view_students , delete_student
from marks import add_marks
from report import generate_report , view_data

create_tables()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Add Marks")
    print("5. Generate Report")
    print("6. View All Data")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        add_marks()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        view_data()
    elif choice == "7":
        break
    else:
        print("Invalid choice.")
