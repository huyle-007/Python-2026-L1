# Practical work 2: Student Mark Management with OOP

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # course_id -> mark

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        try:
            n = int(input("Input number of students: "))
        except ValueError:
            print("Invalid number!")
            return

        for i in range(n):
            print(f"\nEnter student {i + 1} info:")
            s_id = input("Student ID: ").strip()
            name = input("Student name: ").strip()
            dob = input("Date of Birth (DoB): ").strip()
            self.students.append(Student(s_id, name, dob))

    def input_courses(self):
        try:
            n = int(input("Input number of courses: "))
        except ValueError:
            print("Invalid number!")
            return

        for i in range(n):
            print(f"\nEnter course {i + 1} info:")
            c_id = input("Course ID: ").strip()
            name = input("Course name: ").strip()
            self.courses.append(Course(c_id, name))

    def list_students(self):
        print("\n--- Student List ---")
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\n--- Course List ---")
        if not self.courses:
            print("No courses found.")
            return
        for c in self.courses:
            print(c)

    def input_marks(self):
        if not self.courses:
            print("No courses available. Please input courses first.")
            return
        if not self.students:
            print("No students available. Please input students first.")
            return

        self.list_courses()
        c_id = input("\nSelect course ID to input marks: ").strip()

        course = next((c for c in self.courses if c.get_id() == c_id), None)
        if not course:
            print("Course ID not found!")
            return

        print(f"\nInput marks for course {course.get_name()} ({c_id}):")
        for s in self.students:
            while True:
                try:
                    score = float(input(f"Mark for student {s.get_name()} (ID: {s.get_id()}): "))
                    s.set_mark(c_id, score)
                    break
                except ValueError:
                    print("Invalid input, please enter a numeric mark.")

    def show_student_marks(self):
        if not self.courses:
            print("No courses available.")
            return

        self.list_courses()
        c_id = input("\nEnter course ID to view marks: ").strip()

        course = next((c for c in self.courses if c.get_id() == c_id), None)
        if not course:
            print("Course ID not found!")
            return

        print(f"\n--- Marks for course {course.get_name()} ({c_id}) ---")
        for s in self.students:
            mark = s.get_mark(c_id)
            mark_str = f"{mark:.1f}" if mark is not None else "N/A"
            print(f"ID: {s.get_id()} | Name: {s.get_name()} | Mark: {mark_str}")

    def run(self):
        while True:
            print("\nSTUDENT MARK MANAGEMENT (OOP)")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show marks for a course")
            print("0. Exit")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.input_marks()
            elif choice == "6":
                self.show_student_marks()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")


