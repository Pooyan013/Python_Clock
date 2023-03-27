from tkinter import *
from datetime import datetime

window = Tk()
window.title("Clock013")

window.minsize(400 , 80)

def format_time(num):
    if num < 10:
        return f"0{num}"
    else:
        return num

def clock():
    hours = datetime.now().hour
    minutes = datetime.now().minute
    seconds = datetime.now().second
    hours_lbl["text"] = format_time(hours)
    minutes_lbl["text"] = format_time(minutes)
    seconds_lbl["text"] = format_time(seconds)
    window.after(1000,clock) 


frm = Frame(window)

mystyle1 = ('Eccentric Std',20,"bold")

hours_lbl = Label(master=frm,text="",font=mystyle1)
minutes_lbl = Label(master=frm,text="",font=mystyle1)
seconds_lbl = Label(master=frm,text="",font=mystyle1)

hours_lbl.grid(row=0,column=0,sticky="nsew")
minutes_lbl.grid(row=0,column=1,sticky="nsew")
seconds_lbl.grid(row=0,column=2,sticky="nsew")
frm.pack()

clock()

window.mainloop()