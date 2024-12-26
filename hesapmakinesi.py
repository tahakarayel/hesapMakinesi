import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        root.title("Hesap Makinesi - Taha Karayel")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_516=tk.Button(root)
        GButton_516["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#000000"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "/"
        GButton_516.place(x=410,y=370,width=35,height=25)
        GButton_516["command"] = self.GButton_516_command

        GButton_200=tk.Button(root)
        GButton_200["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_200["font"] = ft
        GButton_200["fg"] = "#000000"
        GButton_200["justify"] = "center"
        GButton_200["text"] = "+"
        GButton_200.place(x=140,y=370,width=35,height=25)
        GButton_200["command"] = self.GButton_200_command

        GLineEdit_699=tk.Entry(root)
        GLineEdit_699["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_699["font"] = ft
        GLineEdit_699["fg"] = "#333333"
        GLineEdit_699["justify"] = "center"
        GLineEdit_699["text"] = "Entry"
        GLineEdit_699.place(x=140,y=270,width=70,height=25)

        GLineEdit_474=tk.Entry(root)
        GLineEdit_474["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_474["font"] = ft
        GLineEdit_474["fg"] = "#333333"
        GLineEdit_474["justify"] = "center"
        GLineEdit_474["text"] = "Entry"
        GLineEdit_474.place(x=220,y=270,width=70,height=25)

        GButton_921=tk.Button(root)
        GButton_921["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#000000"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "-"
        GButton_921.place(x=230,y=370,width=35,height=25)
        GButton_921["command"] = self.GButton_921_command

        GButton_100=tk.Button(root)
        GButton_100["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_100["font"] = ft
        GButton_100["fg"] = "#000000"
        GButton_100["justify"] = "center"
        GButton_100["text"] = "*"
        GButton_100.place(x=320,y=370,width=35,height=25)
        GButton_100["command"] = self.GButton_100_command

        GLineEdit_428=tk.Entry(root)
        GLineEdit_428["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_428["font"] = ft
        GLineEdit_428["fg"] = "#333333"
        GLineEdit_428["justify"] = "center"
        GLineEdit_428["text"] = "Entry"
        GLineEdit_428.place(x=300,y=270,width=70,height=25)

    def GButton_516_command(self):
        print("Buton 4e basıldı")


    def GButton_200_command(self):
        print("Buton 1e basıldı")


    def GButton_921_command(self):
        print("Buton 2ye basıldı")


    def GButton_100_command(self):
        print("Buton 3e basıldı")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    
    textBoxYazilanlar1 = tk.StringVar() #Değişken Tanımlama
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()
    
    
    root.mainloop()
