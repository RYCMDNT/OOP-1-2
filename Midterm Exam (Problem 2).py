from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

def demoColorChange():
 btn1.configure(bg="Yellow", fg="black")

btn1 = Button(window, text = "Click to Change Color", command= demoColorChange)
btn1.pack()
btn1.place(x=180,y=180)

window.mainloop()