from tkinter import *
import pymysql
root = Tk()

class detail:

    l1 = Label(root,text="Student Data")
    l1.pack()


    l2 = Label(root,text="Name")
    l2.pack()
    t1 = Entry(root)
    t1.pack()
    l3 = Label(root,text="ID")
    l3.pack()
    t2 = Entry(root)
    t2.pack()

    l4 = Label(root,text="Mobile")
    l4.pack()
    t3 = Entry(root)
    t3.pack()

    l5 = Label(root,text="Branch")
    l5.pack()
    t4= Entry(root)
    t4.pack()

    l6 = Label(root,text="Sem")
    l6.pack()
    t5 = Entry(root)
    t5.pack()

def show():
        try:
            db = pymysql.connect(
                host="localhost",
                user="root",
                password="password",   # Replace with your MySQL password
                database="college_info"
            )

            cursor = db.cursor()

            sql = """
            INSERT INTO det(name, id, mobile, branch, sem)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                    detail.t1.get(),
                    detail.t2.get(),
                    detail.t3.get(),
                    detail.t4.get(),
                    detail.t5.get()
                )

            cursor.execute(sql, values)
            db.commit()

            print("Student saved successfully!")

            cursor.close()
            db.close()

        except Exception as e:
            print("Error:", e)
    
    

        
    
# Submit Button
Button(root,text="Submit", command=show).pack(pady=20)
mainloop()            