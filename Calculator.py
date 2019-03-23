from tkinter import *

class Calculator:
    def __init__(self, master):
        def calc(event):
            master.final_value.configure(text=str(eval(master.main_entry.get())))
            master.ans_number.configure(text="ans:" + master.final_value.cget("text"))

        class Buttonnum:

            def __init__(self, num, row_loc, column_loc):
                def input_num(event):

                    master.main_entry.insert(END, str(num))

                self.int_button = Button(text=num, bg="#9999cc", height=3, width=5, font=1)
                self.int_button.grid(row=row_loc, column=column_loc, sticky=N+E+S+W)
                self.int_button.bind("<Button-1>", input_num)

        def clear(event):
            master.final_value.configure(text="")
            master.main_entry.delete(0, END)

        class Buttoncalc:
            def __init__(self, sign, row_loc, column_loc):
                def input_arithmetic(event):

                    master.main_entry.insert(END, sign)

                self.sign_button = Button(text=str(sign), bg="#555588", height=3, width=5, font=1)
                self.sign_button.grid(row=row_loc, column=column_loc, sticky=N+E+S+W)
                self.sign_button.bind('<Button-1>', input_arithmetic)\

        self.master = master
        master.title("Calculator")
        self.one = Buttonnum(1, 5, 0)
        self.two = Buttonnum(2, 5, 1)
        self.three = Buttonnum(3, 5, 2)
        self.four = Buttonnum(4, 4, 0)
        self.five = Buttonnum(5, 4, 1)
        self.six = Buttonnum(6, 4, 2)
        self.seven = Buttonnum(7, 3, 0)
        self.eight = Buttonnum(8, 3, 1)
        self.nine = Buttonnum(9, 3, 2)
        self.zero = Buttonnum(0, 6, 1)
        master.main_entry = Entry(master, bg="#9999cc", font=1)
        master.final_value = Label(master, font=1, bg=top_color)
        self.temp_button = Button(master, text="clc", bg="#555588", font=1)
        self.temp_button.bind("<Button-1>", calc)
        self.clear_button = Button(master, text="ac", bg="#555588", font=1)
        self.clear_button.bind("<Button-1>", clear)
        self.addition_button = Buttoncalc("+", 3, 3)
        self.subtraction_button = Buttoncalc("-", 4, 3)
        self.multiply_button = Buttoncalc("*", 5, 3)
        self.Divide_button = Buttoncalc("/", 6, 3)
        self.left_par_button = Buttoncalc("(", 3, 5)
        self.right_par_button = Buttoncalc(")", 4, 5)
        self.ans_button = Button(text="ans", font=1, command=lambda: master.main_entry.insert(END, master.ans_number.cget("text")[4:]), bg=top_color)
        master.ans_number = Label(text="", bg=top_color)
        self.ans_clear_button = Button(text="c ans", font=1, command=lambda: master.ans_number.configure(text=""), bg=top_color)


        self.ans_clear_button.grid(row=6, column=5, sticky=N+E+S+W)
        self.clear_button.grid(row=6, column=0, sticky=N+S+E+W)
        master.main_entry.grid(row=1, column=0, columnspan=10, sticky=N+S+E+W)
        master.final_value.grid(row=0, column=1, columnspan=4)
        self.temp_button.grid(row=6, column=2, sticky=N+S+E+W)
        self.ans_button.grid(row=5, column=5, sticky=N+S+E+W)
        master.ans_number.grid(row=0, column=0)

top_color = '#555588'

root = Tk()
my_gui = Calculator(root)
root['bg'] = top_color
root.mainloop()
