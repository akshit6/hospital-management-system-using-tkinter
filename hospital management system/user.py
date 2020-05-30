# import modules

from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import sqlite3
import tkinter.messagebox
import re 

# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move in the database
c = conn.cursor()

designation = ["System Administrator","Doctor","Guest"]

regex = '^[a-z0-9]+[.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# tkinter window
class App:
    def __init__(self, master):
        self.master = master

        # creating the format in master
        self.left = Frame(master, width=800, height=720, bg='lightblue')
        self.left.pack(side = LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side = RIGHT)

        # labels for the window
        # self.heading = Label(self.left, text="Techmirtz Hospital Appointment Application", font=('arial 25 bold'), fg='black', bg='lightblue')
        # self.heading.place(x=5, y=0)

        # id
        self.email_id = Label(self.left, text="Email-ID", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.email_id.place(x=100, y=100)

        # name
        self.name = Label(self.left, text="Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=100, y=140)

        # password
        self.password = Label(self.left, text="Password", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.password.place(x=100, y=180)

        # designation
        self.designation = Label(self.left, text="Designation", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.designation.place(x=100, y=220)

        

        

        # Enteries for all labels==============================================================

        self.email_id_ent = Entry(self.left, width=30)
        self.email_id_ent.place(x=350, y=105)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=350, y=145)

        self.password_ent = Entry(self.left, width=30)
        self.password_ent.place(x=350, y=185)

        self.designation_ent = Entry(self.left, width=30)
        self.designation_ent.place(x=350, y=225)

        # button to perform a command
        self.submit = Button(self.left, text="Add Admin", width=20, height=2, bg='steelblue', command=self.add_admin)
        self.submit.place(x=365, y=320)


        # displaying the logs in right frame
        self.logs = Label(self.right, text="Appointment Log", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=20, y=0)

        self.box = Text(self.right, width=40, height=30)
        self.box.place(x=20, y=60)
        # self.box.insert(END, "Total Appointments till now :  " + str(self.count))

    # function to call when the submit button is clicked
    def add_admin(self):
        # getting the user inputs
        self.val1 = self.email_id_ent.get()
        self.val2 = self.name_ent.get()
        self.val3 = self.password_ent.get()
        self.val4 = self.designation_ent.get()
        
        

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' :
            tkinter.messagebox.showwarning("Warning","Please fill up all the boxes !")
        if(not re.search(regex,self.val1)):  
            tkinter.messagebox.showwarning("Warning","Please enter a valid email !")  
        if(' ' in self.val3):
            tkinter.messagebox.showwarning("Warning","Please enter a password without Spaces !")
        if(self.val4 not in designation):
            tkinter.messagebox.showwarning("Warning","Please enter designation from "+designation[0] + ", "+designation[1]+ ", "+designation[2])

        else:
            # pass
            # now we add to the database
            try:
                sql = "INSERT INTO 'credentials' (email, name, pass, designation) VALUES(?, ?, ?, ?)"
                c.execute(sql, (self.val1,self.val2,self.val3,self.val4))
                conn.commit()
                tkinter.messagebox.showinfo("Success", str(self.val4)+" "+str(self.val2)+" has been created")
            except Exception as e:
                tkinter.messagebox.showerror("Error",e)

#creating the object
root = tk.Tk()
b = App(root)

# resolution of the window
root.geometry("1200x620+0+0")

# preventing the resize feature
root.resizable(False, False)

# title of the window
root.title("Hospital management system")

# icon of the application
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()