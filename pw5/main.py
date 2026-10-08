import os
import zipfile
import curses
from domains.student import Student
from domains.course import Course
from input import get_str, input_data, input_marks
from output import show_ranking

STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"
MARKS_FILE = "marks.txt"
DAT_FILE = "students.dat"

def save_data(students, courses):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

    with open(COURSES_FILE, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credits}\n")

    with open(MARKS_FILE, "w", encoding="utf-8") as f:
        for s in students:
            for c_id, score in s.marks.items():
                f.write(f"{c_id},{s.id},{score}\n")

    with zipfile.ZipFile(DAT_FILE, "w") as zipf:
        for file in [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]:
            if os.path.exists(file):
                zipf.write(file)

def load_data():
    students, courses = [], []

    if os.path.exists(DAT_FILE):
        with zipfile.ZipFile(DAT_FILE, "r") as zipf:
            zipf.extractall()

    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], float(parts[2])))

    st_dict = {}
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    s = Student(parts[0], parts[1], parts[2])
                    students.append(s)
                    st_dict[s.id] = s

    if os.path.exists(MARKS_FILE):
        with open(MARKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[1] in st_dict:
                    st_dict[parts[1]].marks[parts[0]] = float(parts[2])

    return students, courses

def main_curses(stdscr):
    students, courses = load_data()

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "1. Input Students & Courses")
        stdscr.addstr(2, 2, "2. Input Marks")
        stdscr.addstr(3, 2, "3. Show GPA Ranking")
        stdscr.addstr(4, 2, "0. Save & Exit")
        choice = get_str(stdscr, 6, "Choice: ")

        if choice == "1":
            input_data(stdscr, students, courses)
        elif choice == "2":
            input_marks(stdscr, students, courses)
        elif choice == "3":
            show_ranking(stdscr, students, courses)
        elif choice == "0":
            save_data(students, courses)
            break

def main():
    curses.wrapper(main_curses)

if __name__ == "__main__":
    main()
