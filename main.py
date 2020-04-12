import tkinter as tk
import re
import math

root = tk.Tk()
root.title('calculator')

ans_val = 0
just_equal = False
b_h = 3
b_w = 3
screen = tk.StringVar()
screen.set('0')
frame = tk.Frame(root)
text = tk.Label(frame, anchor=tk.W, padx=29, bg='#0ABAB5', width=20, height=4, textvariable=screen, font=('helvetica', 15),
                fg='black', wraplength=200)
text.pack(side= tk.LEFT)

ans_text = tk.Label(root)

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

def check(c):
    # grab last 2 characters to see if the last input is an operator,
    # if it is, return True
    l = c.strip().split(" ")
    print(l)
    char = l[-1]
    print(char)

    # char =  c[-2:].strip()
    if (char.startswith("-")):
        return False
    if ("x" in char) or ("-" in char) or ("/" in char) or ("+" in char) or ("!" in char):
        return True
    if char.endswith("."):
        return True

    return False

def ans(c):
    global ans_val
    equal(c)
    screen.set("0")

def divide(c):
    if check(c):
        return
    screen.set("%s / " % c)

def times(c):
    if check(c):
        return
    screen.set("%s x " % c)

def dot(c):
    if check(c):
        return
    l = c.split(" ")
    char = l[-1]
    print(char)

    if ("." in char):
        return

    screen.set("%s." % c)

def plus(c):
    if check(c):
        if (c.strip().split(" ")[-1] == "/") or (c.strip().split(" ")[-1] == "x") or (c.strip().split(" ")[-1] == "-"):
            d = list(c.strip())
            d[-1] = "x"
            screen.set("%s " % ("".join(d)))
        return
    screen.set("%s + " % c)

def minus(c):
    if (c == ""):
        screen.set("%s -" % c)
        return
    if check(c):
        screen.set("%s -" % c)
        return
    if ("Zero!" in screen.get()):
        return
    screen.set("%s - " % c)


def equal(c):
    global ans_val
    global just_equal
    nums = re.findall(r'\-?\d+\.?\d*', c)
    nums = [float(x) for x in nums]

    just_equal = True

    # edge case: only one number on screen
    if (len(nums) <= 1):
        return
    # nums.insert(0, ans_val)
    operators = re.findall(r'\s(\+|\-|\/|x)\s', c)
    if ((len(nums)-1) != len(operators)):
        del nums[0]

    print(nums)
    print(operators)
    while True:
        if len(nums) == 1:
            rs = nums[0]
            break
        if ("/" in operators) or ("x" in operators):
            for i,op in enumerate(operators):
                if (op == "/"):
                    try:
                        temp = nums[i] / nums[i+1]
                        nums[i] = temp
                        del nums[i+1]
                        del operators[i]
                        break
                    except ZeroDivisionError:
                        screen.set("Division by Zero!")
                        rs = 0
                        return rs

                if (op == "x"):
                    temp = nums[i] * nums[i + 1]
                    nums[i] = temp
                    del nums[i + 1]
                    del operators[i]
                    break
        elif ("+" in operators) or ("-" in operators):
            for i,op in enumerate(operators):
                if (op == "+"):
                    print("the index is ", i)
                    print(len(nums))
                    temp = nums[i] + nums[i + 1]
                    nums[i] = temp
                    del nums[i + 1]
                    del operators[i]
                    break

                if (op == "-"):
                    temp =  nums[i] - nums[i+1]
                    nums[i] = temp
                    del nums[i+1]
                    del operators[i]
                    break

    if rs.is_integer():
        screen.set(int(rs))
    else:
        screen.set(rs)
    ans_val = rs


def handle_clicks(btn):
    global screen
    global ans_val
    global just_equal
    current = screen.get()

    if (just_equal == True):
        if (btn.isdigit()):
            current = ""
        elif (btn == "-"):
            current = ""
        just_equal = False

    if btn.isdigit():
        if current == "0":
            screen.set(btn)
        else:
            screen.set(current+btn)
    else:
        ops = {".":dot, "ans":ans, "+":plus, "-":minus, "=":equal, "x":times, "/":divide}
        ops[btn](current)


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

    frame.grid(row=4, column=0, columnspan=3)

    root_close = CloseWindow(root)
    root.protocol('WM_DELETE_WINDOW', lambda p=root, c=root_close: show_close_window(c, p))

    root.resizable(False, False)
    tk.mainloop()


if __name__ == "__main__":
    main()

