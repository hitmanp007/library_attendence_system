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
    from attendence import button


def all():
    import search_attendence
# all tkinter input buttons 


b1  = Button(root,text="register",command=details)
b1.place(x=130, y=50, width=150 , height= 50)
b2 = Button(root,text="capture",command=cap)
b2.place(x=130, y=110, width=150 , height= 50)
b3 = Button(root,text="trainer",command=train)
b3.place(x=130, y=170, width=150 , height= 50)
b4 = Button(root,text="reccognize",command=recognize)
b4.place(x=130, y=230, width=150 , height= 50)
b5 = Button(root,text="show all attendence",command=attend)
b5.place(x=130, y=290, width=150 , height= 50)
b6 = Button(root,text="search attendence")
b6.place(x=130, y=350, width=150 , height= 50)


mainloop()

