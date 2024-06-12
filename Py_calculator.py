from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Create buttons
        self.create_buttons(master)

    def create_buttons(self, master):
        buttons = [
            ('1', 0, 100), ('2', 90, 100), ('3', 180, 100), ('+', 270, 100),
            ('4', 0, 170), ('5', 90, 170), ('6', 180, 170), ('-', 270, 170),
            ('7', 0, 240), ('8', 90, 240), ('9', 180, 240), ('*', 270, 240),
            ('C', 0, 310), ('0', 90, 310), ('=', 180, 310), ('/', 270, 310),
        ]

        for (text, x, y) in buttons:
            Button(master, text=text, width=10, height=4, command=lambda t=text: self.show(t) if t != '=' else self.solve() if t == '=' else self.clear() if t == 'C' else self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')
            self.entry_value = ''

root = Tk()
calc = Calculator(root)
root.mainloop()
