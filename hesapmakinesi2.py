import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        root.title("Hesap Makinesi - Taha Karayel")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.num1 = tk.Entry(root, borderwidth="1px", justify="center")
        self.num1.place(x=140, y=270, width=70, height=25)

        self.num2 = tk.Entry(root, borderwidth="1px", justify="center")
        self.num2.place(x=220, y=270, width=70, height=25)

        self.result = tk.Entry(root, borderwidth="1px", justify="center", state="readonly")
        self.result.place(x=300, y=270, width=70, height=25)

        self.add_button = tk.Button(root, text="+", command=self.add, bg="#f0f0f0", font=tkFont.Font(size=10))
        self.add_button.place(x=140, y=370, width=35, height=25)

        self.sub_button = tk.Button(root, text="-", command=self.subtract, bg="#f0f0f0", font=tkFont.Font(size=10))
        self.sub_button.place(x=230, y=370, width=35, height=25)

        self.mul_button = tk.Button(root, text="*", command=self.multiply, bg="#f0f0f0", font=tkFont.Font(size=10))
        self.mul_button.place(x=320, y=370, width=35, height=25)

        self.div_button = tk.Button(root, text="/", command=self.divide, bg="#f0f0f0", font=tkFont.Font(size=10))
        self.div_button.place(x=410, y=370, width=35, height=25)

    def get_inputs(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            return num1, num2
        except ValueError:
            self.result.configure(state="normal")
            self.result.delete(0, tk.END)
            self.result.insert(0, "Error")
            self.result.configure(state="readonly")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.display_result(num1 + num2)

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.display_result(num1 - num2)

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.display_result(num1 * num2)

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                self.display_result("Div by 0!")
            else:
                self.display_result(num1 / num2)

    def display_result(self, value):
        self.result.configure(state="normal")
        self.result.delete(0, tk.END)
        self.result.insert(0, str(value))
        self.result.configure(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
