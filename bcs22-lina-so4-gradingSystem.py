def calculate_status(grades):
    for grade in grades:
        if grade < 70:
            return 'Failed'
    return 'Passed'


def display_2d_array(students_data):
    print("\n2D Array Grading System:")
    print("-------------------------------------------------------------------------------")
    print("Name\t| Q1\t| Q2\t| Q3\t| Final Exam\t| Class Participation  | Status")
    print("------------------------------------------------------------------------")
    for student_data in students_data:
        grades = [int(student_data[i]) for i in range(1, len(student_data) - 1)]
        status = calculate_status(grades)
        print(f"{student_data[0]}\t| {student_data[1]}\t| {student_data[2]}\t| {student_data[3]}\t| {student_data[4]}\t\t| {student_data[5]}\t\t| {status}")
        print("-------------------------------------------------------------------------------")


students_data = []

while True:
    student_data = []
    print("\nOUTPUT:")
    print("Name:")
    name = input()
    student_data.append(name)
    print("Q1:")
    q1 = input()
    student_data.append(q1)
    print("Q2:")
    q2 = input()
    student_data.append(q2)
    print("Q3:")
    q3 = input()
    student_data.append(q3)
    print("Final Examination:")
    final_exam = input()
    student_data.append(final_exam)
    print("Class Participation:")
    participation = input()
    student_data.append(participation)

    # Display the 2D array grading system for the current student
    display_2d_array([student_data])

    students_data.append(student_data)

    if input("Enter new student? (Y/N): ").strip().lower() == 'n':
        break

# Display all records
print("\n2D Array Grading System for All Students:")
display_2d_array(students_data)
