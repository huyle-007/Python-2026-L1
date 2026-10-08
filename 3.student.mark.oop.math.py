import math
import numpy as np
import curses

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_mark(self, c_id, score):
        self.marks[c_id] = math.floor(score * 10) / 10.0

    def get_gpa(self, courses):
        c_dict = {c.id: c.credits for c in courses}
        m_list = [self.marks[cid] for cid in self.marks if cid in c_dict]
        c_list = [c_dict[cid] for cid in self.marks if cid in c_dict]

        if not c_list or sum(c_list) == 0:
            return 0.0
        return float(np.sum(np.array(m_list) * np.array(c_list)) / np.sum(c_list))

class Course:
    def __init__(self, c_id, name, credits=3):
        self.id = c_id
        self.name = name
        self.credits = credits

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

def show_ranking(stdscr, students, courses):
    stdscr.clear()
    sorted_st = sorted(students, key=lambda s: s.get_gpa(courses), reverse=True)
    stdscr.addstr(1, 2, "=== GPA RANKING ===")
    for idx, s in enumerate(sorted_st):
        stdscr.addstr(3 + idx, 2, f"Rank {idx+1} | {s.name} | GPA: {s.get_gpa(courses):.2f}")
    get_str(stdscr, len(sorted_st) + 4, "Press Enter to return...")

def main_curses(stdscr):
    students, courses = [], []
    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "1. Input Students & Courses")
        stdscr.addstr(2, 2, "2. Input Marks")
        stdscr.addstr(3, 2, "3. Show GPA Ranking")
        stdscr.addstr(4, 2, "0. Exit")
        choice = get_str(stdscr, 6, "Choice: ")

        if choice == "1":
            input_data(stdscr, students, courses)
        elif choice == "2":
            input_marks(stdscr, students, courses)
        elif choice == "3":
            show_ranking(stdscr, students, courses)
        elif choice == "0":
            break

if __name__ == "__main__":
    curses.wrapper(main_curses)
