from tkinter import *
# from details import detail
root = Tk()
def details():
    root.destroy()
    # import detail

def cap():
    root.destroy()
    import capture

def train():
    root.destroy()
    import train

def recognize():
    root.destroy()
    import recognizer

def attend():
    root.destroy()
    # import attendence
b1  = Button(root,text="register")
b1.pack()
b2 = Button(root,text="capture",command=cap)
b2.pack()
b3 = Button(root,text="trainer",command=train)
b3.pack()
b4 = Button(root,text="reccognize")
b4.pack()
b5 = Button(root,text="show all attendence")
b5.pack()
b5.pack()
b6 = Button(root,text="search attendence")
b6.pack()
root.mainloop()

