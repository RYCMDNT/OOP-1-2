import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.buttonA = tk.Button(self.root,
                                 text = "Click to change color",
                                 bg = "pink",
                                 fg = "black",
                                 command=self.changeColor)

        self.buttonA.pack()
        self.root.mainloop()

    def changeColor(self):
        self.buttonA.configure(bg="red")

app=Test()