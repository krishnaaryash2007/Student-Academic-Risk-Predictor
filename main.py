from student import add_student
from student import show_students
from student import search_student
from student import delete_student
from student import students

from attendance import attendance_status
from marks import marks_status
from analysis import calculate_score
from risk import find_risk
from recommendation import give_recommendation


# analyze a single student by registration no.
def analyze_one_student():
    if len(students) == 0:
        print("No students available.")
        return

    reg_no = input("Enter registration number: ")
    found = False

    for student in students:
        if student["reg_no"] == reg_no:
            found = True
            att_result = attendance_status(student["attendance"])
            marks_result = marks_status(student["marks"])

            score = calculate_score(
                student["attendance"],
                student["marks"],
                student["quiz"],
                student["assignment"],
                student["previous_result"]
            )

            risk = find_risk(score)
            recommendation = give_recommendation(risk)

            print("\n--- Student Analysis ---")
            print("Student Name:", student["name"])
            print("Attendance:", att_result)
            print("Marks:", marks_result)
            print("Performance Score:", round(score, 2))
            print("Risk Level:", risk)
            print("Recommendation:", recommendation)
            break

    if not found:
        print("Student not found.")

def class_summary():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n--- Class Summary ---")
    total = 0

    for student in students:
        score = calculate_score(
            student["attendance"],
            student["marks"],
            student["quiz"],
            student["assignment"],
            student["previous_result"]
        )
        total += score
        print(student["name"], ":", round(score, 2))

    avg = total / len(students)
    print("Class Average:", round(avg, 2))

def main():
    while True:
        print("\n__________________________________")
        print(" STUDENT ACADEMIC RISK SYSTEM")
        print("__________________________________")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Analyze Student")
        print("5. Class Summary")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            analyze_one_student()
        elif choice == "5":
            class_summary()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")


main()