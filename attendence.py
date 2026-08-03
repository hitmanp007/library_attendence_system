import pymysql
from tkinter import *
root = Tk()

def attendence():

    db = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="college_info"
)
    sql = "select * from attendance"
    cursor = db.cursor()
    cursor.execute(sql,)
    result = cursor.fetchall()
    print(result)


def button():
    l1 = Label(root,text="id")
    l1.grid(row=0,column=0)
    l2 = Label(root,text="date ")
    l2.grid(row=1,column=1)

button()
root.mainloop()


