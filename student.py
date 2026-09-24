students = []  # keeps all student records in memory


def add_student():
    print("\n--- Add Student ---")

    reg_no = input("Enter registration number: ")
    name = input("Enter student name: ")

    # performance stats, all as percentages
    attendance = float(input("Enter attendance percentage: "))
    marks = float(input("Enter marks percentage: "))
    quiz = float(input("Enter quiz percentage: "))
    assignment = float(input("Enter assignment percentage: "))
    previous_result = float(input("Enter previous result percentage: "))

    student = {
        "reg_no": reg_no,
        "name": name,
        "attendance": attendance,
        "marks": marks,
        "quiz": quiz,
        "assignment": assignment,
        "previous_result": previous_result
    }

    students.append(student)
    print("Student added successfully.")


def show_students():
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("Registration No:", student["reg_no"])
        print("Name:", student["name"])
        print("Attendance:", student["attendance"])
        print("Marks:", student["marks"])
        print("Quiz:", student["quiz"])
        print("Assignment:", student["assignment"])
        print("Previous Result:", student["previous_result"])
        print("------------------------")


def search_student():
    print("\n--- Search Student ---")
    reg_no = input("Enter registration number: ")

    for student in students:
        if student["reg_no"] == reg_no:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Attendance:", student["attendance"])
            print("Marks:", student["marks"])
            print("Quiz:", student["quiz"])
            print("Assignment:", student["assignment"])
            print("Previous Result:", student["previous_result"])
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    reg_no = input("Enter registration number: ")

    for student in students:
        if student["reg_no"] == reg_no:
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")