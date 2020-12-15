import tkinter as tk
from main import CloseWindow as c

r = tk.Tk()
r.title("name")
closing_win = c(r)
r.protocol('WM_DELETE_WINDOW', lambda p=r, c=closing_win: c.show_window(p))

tk.mainloop()


