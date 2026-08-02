from tkinter import *
root = Tk()

def details():
    
    from register_data import detail

def cap():
    
    import capture

def train():
    
    import train

def recognize():
    
    import recognizer

def attend():
    pass

# all tkinter input buttons 


b1  = Button(root,text="register",command=details)
b1.pack()
b2 = Button(root,text="capture",command=cap)
b2.pack()
b3 = Button(root,text="trainer",command=train)
b3.pack()
b4 = Button(root,text="reccognize")
b4.pack()
b5 = Button(root,text="show all attendence")
b5.pack()
b6 = Button(root,text="search attendence")
b6.pack()


mainloop()

