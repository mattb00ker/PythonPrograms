import Tkinter
import tkMessageBox

top =Tkinter.Tk()

def hellocallsback():
    tkMessageBox.showinfo("hello python", "hello world")

B = Tkinter.Button(top, text = "hello", command = hellocallback)

B.pack()
top.mainloop()
