import tkinter as tk
import re
import math

root = tk.Tk()
root.title('calculator')

b_h = 3
b_w = 3
screen = tk.StringVar()
screen.set('0')
text = tk.Label(root, anchor=tk.W, padx=29, bg='white', width=20, height=5, textvariable=screen, font=('helvetica', 15),
                fg='black', wraplength=200)

class CloseWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        la = tk.Label(self, text="Close window?")
        la.place(anchor='n', relx=0.5, rely=0.25)
        parent.update()
        btn1 = tk.Button(self, width=b_w, height=b_h, command=parent.quit, text='Yes', padx=30, pady=5)
        btn2 = tk.Button(self, width=b_w, height=b_h, command=self.hide, text='No', padx=30, pady=5)
        btn1.place(anchor='n', relx=0.5, rely=0.35, x=-la.winfo_width()/2)
        btn2.place(anchor='n', relx=0.5, rely=0.35, x=la.winfo_width()/2)
        self.protocol('WM_DELETE_WINDOW', self.hide)
        self.update_idletasks()
        self.hide()

    def hide(self):
        self.withdraw()
        self.grab_release()

def center(toplevel, parent):
    # parent.update_idletasks()
    # get root's x + y:
    x = parent.winfo_x()
    y = parent.winfo_y()

    # find offsets:
    off_x = (parent.winfo_width()/2) - (toplevel.winfo_width()/2)

    toplevel.geometry("+%d+%d" % (x + off_x, y))


def show_close_window(c, p):
    center(c, p)
    c.update()
    c.deiconify()
    c.grab_set()

def handle_clicks(btn):
    global screen

    if btn.isdigit():
        screen.set('is a digit')
    else:
        screen.set('not')


def main():
    btns = {}

    # creating buttons
    for x in range (0, 17):
        if x <= 9:
            current_btn_content = str(x)
            current_btn_str = 'b_{}'.format(x)
        else:
            current_btn_content = '-' if x == 10 else current_btn_content
            current_btn_content = '+' if x == 11 else current_btn_content
            current_btn_content = 'x' if x == 12 else current_btn_content
            current_btn_content = '/' if x == 13 else current_btn_content
            current_btn_content = 'ans' if x == 14 else current_btn_content
            current_btn_content = '=' if x == 15 else current_btn_content
            current_btn_content = '.' if x == 16 else current_btn_content
            current_btn_str = 'b_{}'.format(current_btn_content)

        btns[current_btn_str] = tk.Button(root, height=b_h, width=b_w, padx=30, pady=20, text=current_btn_content)
        btns[current_btn_str].configure(command=lambda y=current_btn_content: handle_clicks(y))

    btns['b_9'].grid(row=0, column=2)
    btns['b_8'].grid(row=0, column=1)
    btns['b_7'].grid(row=0, column=0)

    btns['b_6'].grid(row=1, column=2)
    btns['b_5'].grid(row=1, column=1)
    btns['b_4'].grid(row=1, column=0)

    btns['b_3'].grid(row=2, column=2)
    btns['b_2'].grid(row=2, column=1)
    btns['b_1'].grid(row=2, column=0)

    btns['b_ans'].grid(row=3, column=2)
    btns['b_.'].grid(row=3, column=1)
    btns['b_0'].grid(row=3, column=0)

    btns['b_/'].grid(row=0, column=3)
    btns['b_x'].grid(row=1, column=3)
    btns['b_-'].grid(row=2, column=3)
    btns['b_+'].grid(row=3, column=3)
    btns['b_='].grid(row=4, column=3, columnspan=1)

    text.grid(row=4, column=0, columnspan=3)

    root_close = CloseWindow(root)
    root.protocol('WM_DELETE_WINDOW', lambda p=root, c=root_close: show_close_window(c, p))

    tk.mainloop()


if __name__ == "__main__":
    main()

