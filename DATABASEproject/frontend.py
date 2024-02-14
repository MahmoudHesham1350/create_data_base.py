import controlDATA
from tkinter import *
from tkinter import ttk

db = controlDATA.DataBase()
# db.connect_database()


def go_log():
    pass


root = Tk()
root.title("college system")
root.geometry("1920x1080+0+0")
# root.resizable(False, False)
root.config(background="#F2F3F4")

fr = Frame(width=640, height=820, background="#F7F9F9")
fr.place(x=240, y=100)

login_str = Label(fr, text="LOGIN MENU", font=100, bg="#F7F9F9", foreground="black")
login_str.place(x=220, y=50)


choice = StringVar()
choice.set("control")
login_type = ttk.Combobox(fr, values=("control", "students"), state="readonly")
login_type.place(x=220, y=500)

button_log = Button(fr, text="LOGIN", background="white", command=go_log, width=11, height=1)
button_log.place(x=200, y=620)

button_exit = Button(fr, text="EXIT", background="white", command=exit, width=11, height=1)
button_exit.place(x=290, y=620)


root.mainloop()
