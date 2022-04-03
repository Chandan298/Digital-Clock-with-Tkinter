from sqlite3 import Timestamp
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Clock")
from time import strftime
def clock():
    # timestorage = strftime("%H : %M : %S %p")
    hourstorage = int(strftime("%H"))
    minutestorage = int(strftime("%M"))
    secondsstorage = int(strftime("%S"))
    timestamp = strftime("%p")
    if hourstorage > 12:
        hourstorage = hourstorage - 12
    if hourstorage < 10:
        hourstorage = "0" + str(hourstorage)
    if minutestorage < 10:
        minutestorage = "0" + str(minutestorage)
    if secondsstorage < 10:
        secondsstorage = "0" + str(secondsstorage)       
    actualtime = f"{hourstorage}:{minutestorage}:{secondsstorage} {timestamp}"
    label.config(text = actualtime)
    label.after(1000, clock)
   # frm = Frame(root, padding = 10)
   # frm.grid()
label = Label(root, font = ("Times New Roman", 40), background="#9b870c", foreground="blue")
label.pack(anchor="center")
clock()
root.mainloop()