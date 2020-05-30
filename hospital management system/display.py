# import modules

from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import tkinter.messagebox
import sqlite3
import pyttsx3

#connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments ORDER BY scheduled_time ASC"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=200, y=0)

        # button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=300, y=500)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=343, y=85)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=317, y=330)

    # function to speak the text and update the text
    def func(self):
        try:
            self.n.config(text=str(number[self.x]))
            self.pname.config(text=str(patients[self.x]))
        except IndexError:
            print("The appointment list is completed :")
            tkinter.messagebox.showinfo("completed :","The appointment list is  completed")
        try:
            pass
            # engine = pyttsx3.init('sapi5')
            # voices = engine.getProperty('voices')
            # rate = engine.getProperty('rate')
            # engine.setProperty('rate', rate-50)
            # engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
            # engine.runAndWait()
        except:
            print("An Error occured in text to speech :")
        self.x += 1

root = Tk()
b = Application(root)
root.geometry("900x568+0+0")
root.resizable(False, False)
root.title("Hospital management system")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))
root.mainloop()