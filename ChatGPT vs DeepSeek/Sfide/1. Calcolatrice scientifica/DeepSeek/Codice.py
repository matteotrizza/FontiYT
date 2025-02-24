import tkinter as tk
from tkinter import font
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatrice Scientifica")
        self.root.geometry("400x600")
        self.root.configure(bg="#2E3440")

        self.equation = ""
        self.result_var = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#2E3440")
        display_frame.pack(pady=20)

        display_font = font.Font(size=24)
        self.display = tk.Entry(display_frame, textvariable=self.result_var, font=display_font, bd=0, insertwidth=4, width=20, justify='right', state='readonly', readonlybackground="#3B4252", fg="#ECEFF4")
        self.display.pack(ipady=10)

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root, bg="#2E3440")
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('^', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('log', 5, 4),
            ('π', 6, 0), ('e', 6, 1), ('ln', 6, 2), ('!', 6, 3), ('AC', 6, 4)
        ]

        button_font = font.Font(size=14)
        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=button_font, bg="#4C566A", fg="#ECEFF4", bd=0, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == '=':
            try:
                self.equation = self.equation.replace('^', '**')
                self.equation = self.equation.replace('√', 'math.sqrt')
                self.equation = self.equation.replace('π', 'math.pi')
                self.equation = self.equation.replace('e', 'math.e')
                self.equation = self.equation.replace('sin', 'math.sin')
                self.equation = self.equation.replace('cos', 'math.cos')
                self.equation = self.equation.replace('tan', 'math.tan')
                self.equation = self.equation.replace('log', 'math.log10')
                self.equation = self.equation.replace('ln', 'math.log')
                self.equation = self.equation.replace('!', 'math.factorial')

                result = str(eval(self.equation))
                self.result_var.set(result)
                self.equation = result
            except:
                self.result_var.set("Errore")
                self.equation = ""
        elif value == 'C':
            self.equation = self.equation[:-1]
            self.result_var.set(self.equation)
        elif value == 'AC':
            self.equation = ""
            self.result_var.set("")
        else:
            self.equation += str(value)
            self.result_var.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
