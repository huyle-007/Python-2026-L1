import curses
from input import get_str, input_data, input_marks
from output import show_ranking

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

def main():
    curses.wrapper(main_curses)

if __name__ == "__main__":
    main()
