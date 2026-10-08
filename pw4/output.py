from input import get_str

def show_ranking(stdscr, students, courses):
    stdscr.clear()
    sorted_st = sorted(students, key=lambda s: s.get_gpa(courses), reverse=True)
    stdscr.addstr(1, 2, "=== GPA RANKING ===")
    for idx, s in enumerate(sorted_st):
        stdscr.addstr(3 + idx, 2, f"Rank {idx+1} | {s.name} | GPA: {s.get_gpa(courses):.2f}")
    get_str(stdscr, len(sorted_st) + 4, "Press Enter to return...")
