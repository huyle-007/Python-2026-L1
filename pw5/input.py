import curses
from domains.student import Student
from domains.course import Course

def get_str(stdscr, y, prompt):
    stdscr.addstr(y, 2, prompt)
    curses.echo()
    val = stdscr.getstr(y, 2 + len(prompt)).decode("utf-8").strip()
    curses.noecho()
    return val

def input_data(stdscr, students, courses):
    stdscr.clear()
    ns = int(get_str(stdscr, 1, "Number of students: "))
    for i in range(ns):
        stdscr.clear()
        sid = get_str(stdscr, 1, f"Student {i+1} ID: ")
        name = get_str(stdscr, 2, "Name: ")
        dob = get_str(stdscr, 3, "DoB: ")
        students.append(Student(sid, name, dob))

    stdscr.clear()
    nc = int(get_str(stdscr, 1, "Number of courses: "))
    for i in range(nc):
        stdscr.clear()
        cid = get_str(stdscr, 1, f"Course {i+1} ID: ")
        name = get_str(stdscr, 2, "Name: ")
        cre = float(get_str(stdscr, 3, "Credits: "))
        courses.append(Course(cid, name, cre))

def input_marks(stdscr, students, courses):
    stdscr.clear()
    cid = get_str(stdscr, 1, "Enter Course ID to input marks: ")
    for i, s in enumerate(students):
        score = float(get_str(stdscr, 3 + i, f"Mark for {s.name}: "))
        s.set_mark(cid, score)
