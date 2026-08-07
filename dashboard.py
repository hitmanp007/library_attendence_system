from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Library Attendance System")
root.geometry("900x600")
root.resizable(False, False)

# ---------------- Color palette ----------------
DARK_BG     = "#1E2A38"   # sidebar / header background
LIGHT_BG    = "#F4F6F9"   # main content background
ACCENT      = "#2E86DE"   # primary accent (buttons)
ACCENT_HOV  = "#1B5FA8"   # accent hover
TEXT_LIGHT  = "#FFFFFF"
TEXT_DARK   = "#2C3A47"
SUBTEXT     = "#B0BEC5"

root.configure(bg=LIGHT_BG)

# ---------------- Original function calls (UNCHANGED) ----------------
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


# ---------------- Header ----------------
header = Frame(root, bg=DARK_BG, height=90)
header.pack(side=TOP, fill=X)

title_lbl = Label(
    header,
    text="📚  Library Attendance System",
    bg=DARK_BG,
    fg=TEXT_LIGHT,
    font=("Segoe UI", 22, "bold")
)
title_lbl.pack(side=LEFT, padx=30, pady=20)

subtitle_lbl = Label(
    header,
    text="Face Recognition Based Attendance Portal",
    bg=DARK_BG,
    fg=SUBTEXT,
    font=("Segoe UI", 10)
)
subtitle_lbl.place(x=32, y=58)

# ---------------- Sidebar (decorative) ----------------
sidebar = Frame(root, bg=DARK_BG, width=200)
sidebar.pack(side=LEFT, fill=Y)

Label(
    sidebar, text="MENU", bg=DARK_BG, fg=SUBTEXT,
    font=("Segoe UI", 10, "bold")
).pack(pady=(30, 10), padx=20, anchor="w")

for i, step in enumerate(["1. Register", "2. Capture", "3. Train", "4. Recognize", "5. Attendance"]):
    Label(
        sidebar, text=step, bg=DARK_BG, fg=TEXT_LIGHT,
        font=("Segoe UI", 10), anchor="w"
    ).pack(fill=X, padx=25, pady=6)

Label(
    sidebar, text="", bg=DARK_BG
).pack(expand=True, fill=BOTH)

Label(
    sidebar, text="v1.0", bg=DARK_BG, fg=SUBTEXT,
    font=("Segoe UI", 8)
).pack(pady=15)

# ---------------- Main content area ----------------
content = Frame(root, bg=LIGHT_BG)
content.pack(side=LEFT, fill=BOTH, expand=True)

Label(
    content, text="Quick Actions", bg=LIGHT_BG, fg=TEXT_DARK,
    font=("Segoe UI", 16, "bold")
).place(x=40, y=30)

Label(
    content, text="Choose an action below to manage attendance records.",
    bg=LIGHT_BG, fg="#607080", font=("Segoe UI", 10)
).place(x=40, y=62)


# ---------------- Reusable hover-styled button ----------------
def make_button(parent, text, command, x, y, w=340, h=55, icon=""):
    btn = Button(
        parent,
        text=f"{icon}   {text}",
        command=command,
        bg=ACCENT,
        fg=TEXT_LIGHT,
        activebackground=ACCENT_HOV,
        activeforeground=TEXT_LIGHT,
        font=("Segoe UI", 12, "bold"),
        relief=FLAT,
        bd=0,
        cursor="hand2",
        anchor="w",
        padx=20
    )
    btn.place(x=x, y=y, width=w, height=h)

    def on_enter(e):
        btn.config(bg=ACCENT_HOV)

    def on_leave(e):
        btn.config(bg=ACCENT)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn


# ---------------- Buttons (same command bindings as original) ----------------
b1 = make_button(content, "Register Student", details, x=40, y=110, icon="🧑‍🎓")
b2 = make_button(content, "Capture Face Data", cap, x=40, y=180, icon="📷")
b3 = make_button(content, "Train Model", train, x=40, y=250, icon="🧠")
b4 = make_button(content, "Recognize & Mark Attendance", recognize, x=40, y=320, icon="✅")
b5 = make_button(content, "Show All Attendance", attend, x=40, y=390, icon="📋")
b6 = make_button(content, "Search Attendance", None, x=40, y=460, icon="🔍")
# NOTE: b6 had no command assigned in the original code, so it is left as None
# here to keep function-calling behavior unchanged. Assign command=all
# if you want it wired to search_attendence, e.g.:
#     b6.config(command=all)

# ---------------- Footer / status bar ----------------
footer = Frame(root, bg="#DDE3EA", height=28)
footer.pack(side=BOTTOM, fill=X)
Label(
    footer, text="Ready", bg="#DDE3EA", fg="#607080",
    font=("Segoe UI", 9)
).pack(side=LEFT, padx=10)

mainloop()