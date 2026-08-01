from tkinter import *
import pymysql
root = Tk()

class detail:

    def __init__(self):
        self.win = Toplevel()
        self.win.title("Student Details")
        self.win.geometry("350x350")

        # Name
        Label(self.win, text="Name").pack()
        self.name_entry = Entry(self.win)
        self.name_entry.pack()

        # ID
        Label(self.win, text="ID").pack()
        self.id_entry = Entry(self.win)
        self.id_entry.pack()

        # Mobile
        Label(self.win, text="Mobile").pack()
        self.mobile_entry = Entry(self.win)
        self.mobile_entry.pack()

        # Branch
        Label(self.win, text="Branch").pack()
        self.branch_entry = Entry(self.win)
        self.branch_entry.pack()

        # Semester
        Label(self.win, text="Semester").pack()
        self.sem_entry = Entry(self.win)
        self.sem_entry.pack()

        # Submit Button
        Button(
            self.win,
            text="Submit",
            command=self.show
        ).pack(pady=20)

    def show(self):
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
                self.name_entry.get(),
                self.id_entry.get(),
                self.mobile_entry.get(),
                self.branch_entry.get(),
                self.sem_entry.get()
            )

            cursor.execute(sql, values)
            db.commit()

            print("Student saved successfully!")

            cursor.close()
            db.close()

        except Exception as e:
            print("Error:", e)


root.mainloop()            