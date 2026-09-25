# Practical work 1: Student Mark Management

students = []
courses = []
marks = {}

def input_students():
    n = int(input("Input number of students: "))
    for i in range(n):
        print(f"\nEnter student {i + 1} info:")
        s_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of Birth (DoB): ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    n = int(input("Input number of courses: "))
    for i in range(n):
        print(f"\nEnter course {i + 1} info:")
        c_id = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id": c_id, "name": name})

def list_students():
    print("\n--- Student List ---")
    if len(students) == 0:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def list_courses():
    print("\n--- Course List ---")
    if len(courses) == 0:
        print("No courses found.")
        return
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def input_marks():
    if len(courses) == 0:
        print("No courses available. Please input courses first.")
        return
    if len(students) == 0:
        print("No students available. Please input students first.")
        return

    list_courses()
    c_id = input("\nSelect course ID to input marks: ")
    
    course_found = False
    for c in courses:
        if c["id"] == c_id:
            course_found = True
            break
            
    if not course_found:
        print("Course ID not found!")
        return

    if c_id not in marks:
        marks[c_id] = {}

    print(f"\nInput marks for course {c_id}:")
    for s in students:
        score = float(input(f"Mark for student {s['name']} (ID: {s['id']}): "))
        marks[c_id][s["id"]] = score

def show_student_marks():
    if len(marks) == 0:
        print("No marks have been entered yet.")
        return

    list_courses()
    c_id = input("\nEnter course ID to view marks: ")
    
    if c_id not in marks:
        print("No marks recorded for this course.")
        return

    print(f"\n Marks for course {c_id} ")
    for s in students:
        s_id = s["id"]
        if s_id in marks[c_id]:
            print(f"ID: {s_id} | Name: {s['name']} | Mark: {marks[c_id][s_id]}")
        else:
            print(f"ID: {s_id} | Name: {s['name']} | Mark: N/A")

def main():
    while True:
        print("\nSTUDENT MARK MANAGEMENT")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show marks for a course")
        print("0. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            input_marks()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if 1 == 1:
    main()