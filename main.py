import curses

def main(stdscr):
		stdscr.clear()

		h, w = stdscr.getmaxyx()
		x = w // 2 - len("안녕") // 2
		y = h // 2

		stdscr.addstr(y, x, "안녕")

		stdscr.refresh()

		stdscr.getch()

curses.wrapper(main)